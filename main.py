import json
from pprint import pprint
def decorator(func):
    def wrapper(path:str):
        try:
            return(func(path))
        except:
            return("file path not found")

    return wrapper

@decorator
def redJson(path:str):
    f=open(path)
    data=json.load(f)
    return data
pprint(redJson('data.json'))