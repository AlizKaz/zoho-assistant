import sys

type(sys.path)

print("all paths in sys.path")
for path in sys.path:
    print(path)
print("---------")

from frontend import chat_ui

# chat_ui.start
