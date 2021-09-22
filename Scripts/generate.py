##
# This file is an early draft, it kinda works but nothing more.
##

from os import walk
import json

base_url_raw = "https://raw.githubusercontent.com/ELOWRO/Meter-Accuracy/main/Meters/"
base_url_blob = "https://github.com/ELOWRO/Meter-Accuracy/blob/main/Meters/"
meters_path = "Meters"
files = next(walk(meters_path), (None, None, []))[2] 
files.remove("index.json")
meters_index = []
meters_data = []
for file in files:
    if file.endswith(".json") == False:
        continue
    with open(meters_path + "/" + file,) as json_file:
        data = json.load(json_file)
        uid = data["uid"]
        url = base_url_raw + file
        data["url"] = base_url_blob + file
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
    print("> " + language)

    with open('METERS_%s.md' % language, 'w') as outfile:
        outfile.write("\n# %s\n\n" % i18n["general"]["dmms"])

        for meter in meters_data:
            print(meter["product_identifier"])
            outfile.write("\n## %s %s\n\n" % (meter["manufacturer"], meter["product_identifier"]))

            if "photo_url" in meter.keys():
                photo_url = meter["photo_url"]
                outfile.write("![%s](%s)\n\n" % (meter["product_identifier"], photo_url))
                
            

            outfile.write("- %s: %s\n" % (i18n["general"]["model"], meter["model_name"]))
            outfile.write("- %s: %s\n" % (i18n["general"]["manufacturer"], meter["manufacturer_full"]))
            outfile.write("- %s: [%s](%s)\n" % (i18n["general"]["source"], meter["source"], meter["source_url"]))
            outfile.write("- %s: [MACDRv1 JSON](%s)\n" % (i18n["general"]["data"], meter["url"]))



            ## Transfer
            outfile.write("\n### %s\n\n" % (i18n["uncertainties"]["transfer"]))

            
            for transfer_identifier in meter["transfer"].keys():
                meter_data = meter["transfer"][transfer_identifier]
                measurement = i18n["measurements"][transfer_identifier]
                measurement_description = measurement["description"]
                unit = measurement["unit"]
                symbol = measurement["symbol"]
                conditions = meter_data["conditions"]
                
   
                outfile.write("\n#### %s\n\n" % (measurement_description))
                outfile.write("##### %s\n\n" %  i18n["uncertainties"]["conditions"])

                if "resolution" in conditions.keys():
                    outfile.write("- %s: %.1f\n" % (i18n["uncertainties"]["resolution"], conditions["resolution"]))
                if "nplc" in conditions.keys():
                    outfile.write("- %s: %d\n" % (i18n["uncertainties"]["nplc"], conditions["nplc"]))

                if "warmup_hours" in conditions.keys():
                    outfile.write("- %s: %d\n" % (i18n["uncertainties"]["warmup_hours"], conditions["warmup_hours"]))
                if "readings_per_second" in conditions.keys():
                    outfile.write("- %s: %.2f\n" % (i18n["uncertainties"]["readings_per_second"], conditions["readings_per_second"]))
                if "with_acal" in conditions.keys():
                    if conditions["with_acal"] == True:
                        outfile.write("- %s\n" % (i18n["uncertainties"]["with_acal"]))
                temp = ""
                if "required_temperature_celsius" in conditions.keys():
                    temp += "T = "
                    temp += "%.1f " % conditions["required_temperature_celsius"]
                if "maximum_temperature_change_from_acal" in conditions.keys():
                    temp += "Tacal ±%.1f °C " % conditions["maximum_temperature_change_from_acal"]
                if "maximum_temperature_change" in conditions.keys():
                    temp += "Tref "
                    temp += "±%.1f °C " % conditions["maximum_temperature_change"]

                outfile.write("- %s\n" % temp)

                ranges = meter_data["ranges"]
                
                times = []
                for range in ranges:
                    accuracies = range["accuracy"]
                    for accuracy in accuracies:
                        seconds_between_measurements = accuracy["seconds_between_measurements"]
                        if seconds_between_measurements not in times:
                            times.append(seconds_between_measurements)

                for time in times:
                    seconds_between_measurements = time
                    outfile.write("\n")

                    outfile.write("**%s: %d %s**\n\n" % (i18n["uncertainties"]["time_between_measurements"], seconds_between_measurements/60, i18n["uncertainties"]["minutes"]))
                    outfile.write("| %s | %s ± (ppm %s + ppm %s) |\n"  % (i18n["uncertainties"]["range"], i18n["general"]["uncertainty"], i18n["uncertainties"]["of_reading"], i18n["uncertainties"]["of_range"]))
                    outfile.write("|--:|:--:|\n")

                    for data in ranges:
                        accuracies = data["accuracy"]
                        range = data["range"]

                        for accuracy in accuracies:
                            if accuracy["seconds_between_measurements"] != time:
                                continue
                            confidence = ""
                            if "confidence" in data.keys():
                                confidence_word = i18n["uncertainties"]["confidence"]
                                confidence = " (%s %d%%) " % (confidence_word, accuracy["confidence"]*100)
                            offset = ""
                            if accuracy["absolute"] > 0:
                                offset = "+ %.7f" % accuracy["absolute"]
                            zin = ""
                            if "impedance_ohms" in accuracy.keys():
                                zin = "[%s: %dMΩ] " % (i18n["uncertainties"]["impedance"], accuracy["impedance_ohms"]/1000000)
                            outfile.write("| %s%.7f%s | %.2f + %.2f %s%s|\n"  % (zin, range, symbol, accuracy["reading"] * 1000000, accuracy["range"] * 1000000, offset, confidence))
                
            ## Absolute        
            outfile.write("\n### %s\n\n" % (i18n["uncertainties"]["absolute"]))

            for absolute_identifier in meter["absolute"].keys():
                measurement = i18n["measurements"][absolute_identifier]
                measurement_description = measurement["description"]
                unit = measurement["unit"]
                symbol = measurement["symbol"]
                outfile.write("\n#### %s\n" % measurement_description)


                outfile.write("##### %s\n\n" %  i18n["uncertainties"]["conditions"])
                conditions = meter["absolute"][absolute_identifier]['conditions']

                if "resolution" in conditions.keys():
                    outfile.write("- %s: %.1f\n" % (i18n["uncertainties"]["resolution"], conditions["resolution"]))
                if "nplc" in conditions.keys():
                    outfile.write("- %s: %d\n" % (i18n["uncertainties"]["nplc"], conditions["nplc"]))
                if "warmup_hours" in conditions.keys():
                    outfile.write("- %s: %d\n" % (i18n["uncertainties"]["warmup_hours"], conditions["warmup_hours"]))
                if "readings_per_second" in conditions.keys():
                    outfile.write("- %s: %.2f\n" % (i18n["uncertainties"]["readings_per_second"], conditions["readings_per_second"]))
                if "with_acal" in conditions.keys():
                    if conditions["with_acal"] == True:
                        outfile.write("- %s\n" % (i18n["uncertainties"]["with_acal"]))

                temp = ""
                if "required_temperature_celsius" in conditions.keys():
                    temp += "T = "
                    temp += "%.1f " % conditions["required_temperature_celsius"]
                if "maximum_temperature_change_from_acal" in conditions.keys():
                    temp += "Tacal ±%.1f °C " % conditions["maximum_temperature_change_from_acal"]
                if "maximum_temperature_change" in conditions.keys():
                    temp += "Tref "
                    temp += "±%.1f °C " % conditions["maximum_temperature_change"]

                outfile.write("- %s\n" % temp)

                outfile.write("\n")

                outfile.write("**± (ppm %s + ppm %s)**\n\n"  % (i18n["uncertainties"]["of_reading"], i18n["uncertainties"]["of_range"]))
                

                data = meter["absolute"][absolute_identifier]['ranges']

                times = []
                ranges = []
                for item in data:
                    range = item["range"]
                    if range not in ranges:   
                        ranges.append(range)
                    accuracy = item["accuracy"]
                    for spec in accuracy: 
                        seconds_between_measurements = spec["hours_from_calibration"]
                        if seconds_between_measurements not in times:   
                            times.append(seconds_between_measurements)

                titles = " | ". join([str(int(number/24)) + " " +i18n["uncertainties"]["days"] for number in times] )
                outfile.write("| %s | %s |\n"  % (i18n["uncertainties"]["range"], titles))
                outfile.write("|--:" + "|:--:"*len(times) + "|\n")
                for range_processed in ranges:
                    outfile.write("| %.7f%s" % (range_processed, symbol))
                    for time in times:
                        for item in data:
                            range = item["range"]
                            if range_processed != range:
                                    continue
                            accuracy = item["accuracy"]
                            for spec in accuracy:
                                hours_from_calibration = spec["hours_from_calibration"]
                                if hours_from_calibration != time:
                                    continue

                                offset = ""
                                if spec["absolute"] > 0:
                                    offset = "+ %.7f%s %s" % (spec["absolute"], unit, i18n["uncertainties"]["absolute_offset"])
                                accuracy = "| %.2f + %.2f%s "  % (spec["reading"] * 1000000, spec["range"] * 1000000, offset)
                                outfile.write(accuracy) 
                    outfile.write("|\n")
                    
        outfile.flush()
        outfile.close()

print("DONE")