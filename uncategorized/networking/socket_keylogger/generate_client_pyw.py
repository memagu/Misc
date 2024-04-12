import os
import shutil
import time


def bold(text: str):
    return f"\u001b[1m{text}\u001b[0m"


start = time.perf_counter()
print(f"Getting paths of {bold('client.py')} and {bold('client.pyw')}...")

client_py = os.path.join(os.getcwd(), "client.py")
print("\t-", client_py)

client_pyw = os.path.join(os.getcwd(), "client.pyw")
print("\t-", client_pyw)

"""
Unnecessary code

if os.path.exists(client_pyw):
    os.remove(client_pyw)
    print("Deleted already existing \u001b[1mclient.pyw\u001b[0m")
"""

print(f"Copying file content from {bold('client.py')} to {bold('client.pyw')}...")
shutil.copy(client_py, client_pyw)
print(f"Done ({(time.perf_counter() - start) * 1000} ms)")
