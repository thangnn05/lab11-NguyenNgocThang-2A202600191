import sys
import typing
from typing import Any, Optional, ForwardRef

print(f"Python version: {sys.version}")

# Simulate Pydantic V1's resolve_annotations call
def simulate_v1_eval(value, base_globals):
    # In 3.13, Pydantic V1 does:
    # return typing._eval_type(value, base_globals, None, type_params=())
    # Let's try it on 3.14
    try:
        print(f"Calling typing._eval_type({value}, globals, None, type_params=())...")
        res = typing._eval_type(value, base_globals, None, type_params=())
        print("Success!")
        return res
    except Exception as e:
        print(f"Failed with {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return None

# Try it with a complex type
base_globals = {'dict': dict, 'Optional': Optional, 'Any': Any}
value = ForwardRef('Optional[dict[str, Any]]')

simulate_v1_eval(value, base_globals)
