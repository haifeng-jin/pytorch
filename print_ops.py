import csv
import importlib

from torch._dynamo import trace_rules
import numpy as np

# for-loop copied from _dynamo/trace_rules.py#_numpy_function_ids() and modified to capture
# numpy ops that are included in numpy_function_ids() in numpy-1.x but not numpy-2.x
ops = []

for mod in trace_rules.NP_SUPPORTED_MODULES:
    for k, v in mod.__dict__.items():
        if callable(v):
            numpy_api_name = f"{mod.__name__}.{k}"
            ops.append([
                numpy_api_name,
                getattr(v, "__module__", None),
                mod.__name__,
                (getattr(v, "__module__", None) or mod.__name__) == mod.__name__,
            ])

with open('/tmp/my_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(ops)
