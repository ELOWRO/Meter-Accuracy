from os import walk
import json

base_url = "https://raw.githubusercontent.com/ELOWRO/Meter-Accuracy/main/Meters/"
meters_path = "Meters"
files = next(walk(meters_path), (None, None, []))[2] 
files.remove("index.json")
meters_index = []
for file in files:
    with open(meters_path + "/" + file,) as json_file:
        data = json.load(json_file)
        uid = data["uid"]
        url = base_url + file
        meters_index.append({
            "uid": uid,
            "manufacturer": data["manufacturer"],
            "model_name": data["model_name"],
            "url": url
        })

index_json = {}
index_json["meters"] = meters_index

with open(meters_path + '/index.json', 'w') as outfile:
    json.dump(index_json, outfile)

print("DONE")