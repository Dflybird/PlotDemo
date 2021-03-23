import json

if __name__ == "__main__":
    data = {'a': 1, 'd': 4,'b': 2, 'c': 3,  'e': 5}
    data2 = json.dumps(data, indent=4)
    print(data2)
    data3 = json.loads(data2)
    print(data3)