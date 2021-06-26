from os import walk
import json
import unittest
base_url = "https://raw.githubusercontent.com/ELOWRO/Meter-Accuracy/main/Meters/"
meters_path = "Meters"
files = next(walk(meters_path), (None, None, []))[2] 
files.remove("index.json")

class TestJSONFiles(unittest.TestCase):
    def test_format_id(self):
        for file in files:
            with open(meters_path + "/" + file,) as json_file:
                data = json.load(json_file)
                assert("org.macdr.v1" == data["format"])
    def test_mandatory_properties(self):
        for file in files:
            with open(meters_path + "/" + file,) as json_file:
                data = json.load(json_file)
                uid = data["uid"]
                manufacturer = data["manufacturer"]
                manufacturer_full = data["manufacturer_full"]
                model_name = data["model_name"]
                product_identifier = data["product_identifier"]
                source = data["source"]
                source_url = data["source_url"]

if __name__ == '__main__':
    unittest.main()