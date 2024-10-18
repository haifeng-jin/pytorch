import csv
import tabulate
import ast

def read_ops(filename):
    ret = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ret[row[0]] = row[1:]
    return ret


np1_ops = read_ops('np1_ops.csv')
np2_ops = read_ops('np2_ops.csv')

print("Supported in NumPy 1, but not iterated in NumPy 2: ")
print(tabulate.tabulate(
    [
        {"API": key, "__module__": np1_ops[key][0], "__name__": np1_ops[key][1]}
        for key in np1_ops.keys() - np2_ops.keys()
        if np1_ops[key][-1] == 'True'
    ],
    headers="keys",
    tablefmt="github",
))
print()
print("Supported in NumPy 2, but not iterated in NumPy 1: ")
print(tabulate.tabulate(
    [
        {"API": key, "__module__": np2_ops[key][0], "__name__": np2_ops[key][1]}
        for key in np2_ops.keys() - np1_ops.keys()
        if np2_ops[key][-1] == 'True'
    ],
    headers="keys",
    tablefmt="github",
))
print()
print("Supported in NumPy 1, but not supported in NumPy 2: ")
print(tabulate.tabulate(
    [
        {"API": key, "__module__(np1)": np1_ops[key][0], "__name__(np1)": np1_ops[key][1], "__module__(np2)": np2_ops[key][0], "__name__(np2)": np2_ops[key][1]}
        for key in np1_ops.keys()
        if np1_ops[key][-1] == 'True' and key in np2_ops and np2_ops[key][-1] == 'False'
    ],
    headers="keys",
    tablefmt="github",
))
print()
print("Supported in NumPy 2, but not supported in NumPy 1: ")
print(tabulate.tabulate(
    [
        {"API": key, "__module__(np1)": np1_ops[key][0], "__name__(np1)": np1_ops[key][1], "__module__(np2)": np2_ops[key][0], "__name__(np2)": np2_ops[key][1]}
        for key in np2_ops.keys()
        if np2_ops[key][-1] == 'True' and key in np1_ops and np1_ops[key][-1] == 'False'
    ],
    headers="keys",
    tablefmt="github",
))
