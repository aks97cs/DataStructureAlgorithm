"""
"""

info = None
try:
    if type(info) is not dict:
        raise Exception(f"Invalid data, info is {info.__class__.__name__}, expecting dict")
    age = info["age"]
    print(age)
except Exception as err:
    print(err)