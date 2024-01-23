import time
import json
import random
import os

print("EXECUTING...")
time.sleep(10)
print(" -> DONE!")

rnd_list = [random.random() for i in range(10)]
json_data = {
    "numbers": rnd_list
}
json_str = json.dumps(json_data, indent=4)

print("OUTPUT:")
print(json_str)


out_file = os.environ.get("OUT_FILE", "/output/results.json")
with open(out_file, "w") as f:
    f.write(json_str)
