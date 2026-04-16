import sys
import traceback
from typing import Any, Optional

print(f"Python version: {sys.version}")

try:
    print("Importing LangChain Chain...")
    from langchain.chains.base import Chain
    print("LangChain Success!")
except Exception as e:
    print(f"LangChain Failed: {e}")
    traceback.print_exc()
