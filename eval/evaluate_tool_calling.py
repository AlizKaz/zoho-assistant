from dotenv import load_dotenv

load_dotenv()

import os
from getpass import getpass

if not (openai_api_key := os.getenv("OPENAI_API_KEY_ZOHO_ASSISTANT_PROJECT")):
    openai_api_key = getpass("🔑 Enter your OpenAI API key: ")

os.environ["OPENAI_API_KEY"] = openai_api_key

import nest_asyncio
import pandas as pd

from phoenix.evals import (
    TOOL_CALLING_PROMPT_RAILS_MAP,
    TOOL_CALLING_PROMPT_TEMPLATE,
    OpenAIModel,
    llm_classify,
)

nest_asyncio.apply()

from langchain.agents import AgentType, initialize_agent
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from openinference.instrumentation.langchain import LangChainInstrumentor

import phoenix as px
from phoenix.otel import register

# (session := px.launch_app()).view()
tracer_provider = register()
LangChainInstrumentor(tracer_provider=tracer_provider).instrument(skip_dep_check=True)

from langchain.tools import StructuredTool

# convert invoice_tools.tools formatted as Iterable[ChatCompletionToolParam] to a list of StructuredTool objects
# tools = invoice_tools_2.tools

from langchain.agents import Tool

import invoice_tools
from convert_to_structured_tool import create_structured_tool_from_function


def example_func(*args, **kwargs):
    print("function called with the following arguments")
    print(kwargs)


tools = [create_structured_tool_from_function(function_def=tool["function"], tool_logic=example_func) for tool in
         invoice_tools.tools]

llm = ChatOpenAI(model="gpt-4o")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent_executor = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS)

questions_df = pd.read_csv("generated_questions.csv")

questions_df["response"] = questions_df["questions"].apply(agent_executor.invoke)

# evaluate tool calls
from phoenix.trace import SpanEvaluations
from phoenix.trace.dsl import SpanQuery
from langchain.tools import StructuredTool

query = (
    SpanQuery()
    .where(
        # Filter for the `LLM` span kind.
        # The filter condition is a string of valid Python boolean expression.
        "span_kind == 'LLM'",
    )
    .select(
        # Extract and rename the following span attributes
        question="llm.input_messages",
        tool_call="llm.function_call",
    )
)
trace_df = px.Client().query_spans(query)
trace_df["tool_call"] = trace_df["tool_call"].fillna("No tool used")

tool_definitions = ""

for current_tool in tools:
    tool_definitions += f"""
    {current_tool.name}: {current_tool.description}
    """

print(tool_definitions)

eval_model = OpenAIModel(model="gpt-4o")

rails = list(TOOL_CALLING_PROMPT_RAILS_MAP.values())

response_classifications = llm_classify(
    dataframe=trace_df,
    template=TOOL_CALLING_PROMPT_TEMPLATE.template.replace("{tool_definitions}", tool_definitions),
    model=eval_model,
    rails=rails,
    provide_explanation=True,
)
response_classifications["score"] = response_classifications.apply(
    lambda x: 1 if x["label"] == "correct" else 0, axis=1
)

px.Client().log_evaluations(
    SpanEvaluations(eval_name="Tool Calling Eval", dataframe=response_classifications),
)
print("View your evals in the Spans section of the UI here:", px.Client().web_url)
