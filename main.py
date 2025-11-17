import time
import json
import random
import os
from pathlib import Path

print("EXECUTING...")
time.sleep(10)
print(" -> DONE!")

print("INPUTS:")
input_dir = Path("/input")
input_list = []
for path in input_dir.rglob("*"):
    if path.is_file():
        rel_path = path.absolute()
        input_list.append(str(rel_path))

rnd_list = [random.random() for i in range(10)]
json_data = {
    "numbers": rnd_list,
    "input_files": input_list
}
json_str = json.dumps(json_data, indent=4)

print("OUTPUT:")
print(json_str)


out_file = os.environ.get("OUT_FILE", "/output/results.json")
with open(out_file, "w") as f:
    f.write(json_str)
