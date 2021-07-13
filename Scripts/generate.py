##
# This file is an early draft, it kinda works but nothing more.
##

from os import walk
import json

base_url = "https://raw.githubusercontent.com/ELOWRO/Meter-Accuracy/main/Meters/"
meters_path = "Meters"
files = next(walk(meters_path), (None, None, []))[2] 
files.remove("index.json")
meters_index = []
meters_data = []
for file in files:
    with open(meters_path + "/" + file,) as json_file:
        data = json.load(json_file)
        uid = data["uid"]
        url = base_url + file
        data["url"] = url
        meters_data.append(data)
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

i18n_path = "I18n"
i18n_files = next(walk(i18n_path), (None, None, []))[2] 
for file in i18n_files:
    language = file.replace(".json", "")
    with open(i18n_path + "/" + file,) as json_file:
        i18n = json.load(json_file)

    with open('METERS_%s.md' % language, 'w') as outfile:
        outfile.write("\n# %s\n\n" % i18n["general"]["dmms"])

        for meter in meters_data:
            print(meter["product_identifier"])
            outfile.write("\n## %s %s\n" % (meter["manufacturer"], meter["product_identifier"]))
            outfile.write("- %s: %s\n" % (i18n["general"]["model"], meter["model_name"]))
            outfile.write("- %s: %s\n" % (i18n["general"]["manufacturer"], meter["manufacturer_full"]))
            outfile.write("- %s: [%s](%s)\n" % (i18n["general"]["source"], meter["source"], meter["source_url"]))
            outfile.write("- %s: [MACDRv1 JSON](%s)\n" % (i18n["general"]["data"], meter["url"]))

            ## Transfer
            outfile.write("\n### %s\n" % (i18n["uncertainties"]["transfer"]))

            
            for transfer_identifier in meter["transfer"].keys():
                meter_data = meter["transfer"][transfer_identifier]
                times = []
                for data in meter_data:
                    specs = data["specs"]
                    for spec in specs: 
                        seconds_between_measurements = spec["seconds_between_measurements"]
                        if seconds_between_measurements not in times:   
                            times.append(seconds_between_measurements)

                measurement = i18n["measurements"][transfer_identifier]
                measurement_description = measurement["description"]
                unit = measurement["unit"]
                symbol = measurement["symbol"]
                meter_data = meter["transfer"][transfer_identifier]

                for seconds_between_measurements in times:
                    outfile.write("\n#### %s\n" % measurement_description)
                    outfile.write("#####± (ppm %s + ppm %s)\n\n"  % (i18n["uncertainties"]["of_reading"], i18n["uncertainties"]["of_range"]))
                    outfile.write("| %s | %d %s |\n"  % (i18n["uncertainties"]["range"], seconds_between_measurements/60, i18n["uncertainties"]["minutes"]))
                    
                    outfile.write("|--:|:--:|\n")
                    for data in meter_data:
                        range = data["range"]
                        specs = data["specs"]
                        confidence = ""
                        if "confidence" in data.keys():
                            confidence_word = i18n["uncertainties"]["confidence"]
                            confidence = " (%s %d%%) " % (confidence_word, data["confidence"]*100)
                        for spec in specs:
                            offset = ""
                            if spec["absolute"] > 0:
                                offset = "+ %.7f" % spec["absolute"]
                            zin = ""
                            if "impedance_ohms" in spec.keys():
                                zin = "[%s: %dMΩ] " % (i18n["uncertainties"]["impedance"], spec["impedance_ohms"]/1000000)
                            outfile.write("| %s%.7f%s | %.2f + %.2f %s%s |\n"  % (zin, range, symbol, spec["reading"] * 1000000, spec["range"] * 1000000, offset, confidence))
                    
            ## Absolute        
            outfile.write("\n### %s\n" % (i18n["uncertainties"]["absolute"]))

            for absolute_identifier in meter["absolute"].keys():
                measurement = i18n["measurements"][absolute_identifier]
                measurement_description = measurement["description"]
                unit = measurement["unit"]
                symbol = measurement["symbol"]
                outfile.write("\n#### %s\n" % measurement_description)
                outfile.write("#####± (ppm %s + ppm %s)\n\n"  % (i18n["uncertainties"]["of_reading"], i18n["uncertainties"]["of_range"]))
                data = meter["absolute"][absolute_identifier]
                outfile.write("| %s | %s | XXX |\n"  % (i18n["uncertainties"]["range"], i18n["uncertainties"]["time_from_calibration_days"]))
                outfile.write("|--:|:--|--:|\n")
                for item in data:
                    range = item["range"]
                    specs = item["specs"]
                    for spec in specs: 
                        offset = ""
                        if spec["absolute"] > 0:
                            offset = "+ %.7f%s %s" % (spec["absolute"], unit, i18n["uncertainties"]["absolute_offset"])
                        outfile.write("| %.7f%s | %d | %.2f + %.2f%s |\n"  % (range, symbol, spec["hours_from_calibration"]/24, spec["reading"] * 1000000, spec["range"] * 1000000, offset))
                    
        outfile.flush()
        outfile.close()


print("DONE")