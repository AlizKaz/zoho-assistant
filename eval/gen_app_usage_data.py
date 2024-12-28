import os
from getpass import getpass

from dotenv import load_dotenv
load_dotenv()

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

GEN_TEMPLATE = """
You are an assistant that generates complex customer service questions. You will try to answer the question with the tool if possible,
do your best to answer, ask for more information only if needed.
The questions should often involve:

Please reference the product names, the product details, product IDS and product information.

Multiple Categories: Questions that could logically fall into more than one category (e.g., combining product details with a discount code).
Vague Details: Questions with limited or vague information that require clarification to categorize correctly.
Mixed Intentions: Queries where the customer’s goal or need is unclear or seems to conflict within the question itself.
Indirect Language: Use of indirect or polite phrasing that obscures the direct need or request (e.g., using "I was wondering if..." or "Perhaps you could help me with...").
For specific categories:

Track Package: Include vague timing references (e.g., "recently" or "a while ago") instead of specific dates.
Product Comparison and Product Search: Include generic descriptors without specific product names or IDs (e.g., "high-end smartphones" or "energy-efficient appliances").
Apply Discount Code: Include questions about discounts that might apply to hypothetical or past situations, or without mentioning if they have made a purchase.
Product Details: Ask for comparisons or details that involve multiple products or categories ambiguously (e.g., "Tell me about your range of electronics that are good for home office setups").
Examples of More Challenging Questions
Multiple Categories

"I recently bought a samsung 106i smart phone, and I was wondering if there's a way to check what deals I might have missed or if my order is on its way?"
"Could you tell me if the samsung 15H adapater in my last order are covered under warranty and if they have shipped yet?"
Vague Details

"There's an issue with one of the Vizio 14Y TV I think I bought last month—what should I do?"
"I need help with a iPhone 16H I ordered, or maybe I'm just looking for something new. Can you help?"
Mixed Intentions

"I'm not sure if I should ask for a refund or just find out when it will arrive. What do you suggest?"
"Could you help me decide whether to upgrade my product or just track the current one?"
Indirect Language

"I was wondering if you might assist me in figuring out a problem I have with an order, or maybe it's more of a query?"
"Perhaps you could help me understand the benefits of your premium products compared to the regular ones?"

Some questions should be straightforward uses of the provided functions

Respond with a list, one question per line. Do not include any numbering at the beginning of each line. Do not include any category headings.
Generate 20 questions.
"""

GEN_TEMPLATE = """
You are an assistant that generates complex invoicing queries or commands. You will try to answer the query/command with the 
tool if possible, do your best to answer, ask for more information only if needed.
The query/command should often involve:

Please reference the invoice ids, customer id, item ids, quantities, product names, commands about invoice states (void, delete, sent).

These are the operations that can be on on invoice:
1. create
2. update
3. delete
4. Mark as sent
5. Mark as draft
6. void 
7. email 
8. approve
8. update billing address
10. add comment to an invoice

Commands: Prompts that create, delete, update or make something change. (e.g., creating an invoice, emailing invoices)
Queries: Prompts that tend to ask about the state or fields or information about something. (e.g., search for invoices, get the detail about an invoice, its comments)
Multiple Categories: Questions that could logically fall into more than one category (e.g., combining create invoice and mark as sent).
Vague Details: Questions with limited or vague information that require clarification to categorize correctly.
Mixed Intentions: Queries where the customer’s goal or need is unclear or seems to conflict within the question itself.
Indirect Language: Use of indirect or polite phrasing that obscures the direct need or request (e.g., using "I was wondering if..." or "Perhaps you could help me with...").
For specific categories:

Create Invoice: Include generic descriptors without specific line items or customer id.
Update/Delete Invoice: Include vague references for invoice id
  

Track Package: Include vague timing references (e.g., "recently" or "a while ago") instead of specific dates.
Product Comparison and Product Search: Include generic descriptors without specific product names or IDs (e.g., "high-end smartphones" or "energy-efficient appliances").
Apply Discount Code: Include questions about discounts that might apply to hypothetical or past situations, or without mentioning if they have made a purchase.
Product Details: Ask for comparisons or details that involve multiple products or categories ambiguously (e.g., "Tell me about your range of electronics that are good for home office setups").
Examples of More Challenging Questions
Commands
"Create an invoice for the John Smith"
"Update reference_number to ref-1200450 for invoice id INV-222000"
"Mark the invoice with id INV-556000 as sent"
"Email invoice INV-333931 to John Smith and John Doe"
"I want to approve an invoice"
"Update the billing address for invoice INV-33333"

Queries
"list all the invoices that starts with INV-1000" 
"list all the invoices that contain 'window' in their line items"
"list all the invoices for John Doe"
"list all the invoices which are due by end of September 2025"
"what is the payments related to invoice INV-2000300"
"get the invoice attachments"
Commands with details

"Create an invoice for John Doe with the following line items: - window, 200$ - door, 500$ split the payment into to installment"
Multiple Categories

"Could you tell me if there's any not paid invoice by John Doe and if there are email those invoices to him?"
Mixed Intentions

"I'm not sure if I need to delete an invoice or make it void"
"Could you help me decide whether to update the invoice or just create a new one and delete the old one?"
Indirect Language

"I was wondering if you might assist me in figuring out a problem I have with an invoice, or maybe it's more of a query?"
"Perhaps you could help me understand the benefits of your premium products compared to the regular ones?"

Some questions should be straightforward uses of the provided functions

Respond with a list, one question per line. Do not include any numbering at the beginning of each line. Do not include any category headings.
Generate 40 questions.

"""

model = OpenAIModel(model="gpt-4o", max_tokens=2600)

resp = model(GEN_TEMPLATE)

split_response = resp.strip().split("\n")

questions_df = pd.DataFrame(split_response, columns=["questions"])
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.max_colwidth', None,
                       'display.precision', 3,
                       ):
    print(questions_df)
# serialize the questions to a file inside current directory
questions_df.to_csv("generated_questions.csv", index=False)
# deserialize the questions from a file
questions_df = pd.read_csv("generated_questions.csv")

