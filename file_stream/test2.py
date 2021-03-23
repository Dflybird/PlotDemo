import json

if __name__ == "__main__":
    with open("./all_population1.json", 'r') as f:
        jsonData = json.load(f)
        jsonData2 = json.dumps(jsonData, indent=2)
        print(jsonData2)