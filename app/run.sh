#!/bin/zsh

export PYTHONPATH="./app:$PYTHONPATH"
cwd ./app
echo $PYTHONPATH
echo "finished echoing"
streamlit run ./frontend/chat_ui.py