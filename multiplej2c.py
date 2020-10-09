import csv
import json
import glob
"""
author ayaz wani

following is the code which converts the seven json file to an single csv file


"""

edata = open('multiple.csv', 'w')
csvwriter = csv.writer(edata)
data = []
csvwriter.writerow(["condition","condition_cui","label",
			"label_cui","label_score","label_semantic_types",
			"label_ncts","label_bucket","label_ncts_count"])
data_folder="jsons"
for filename in glob.iglob(data_folder+"/*.json"):
	jsonfile=open(filename)
	jsondata=json.load(jsonfile)
	for k,v in jsondata.items():
		for y,x in jsondata[k]["have_had"].items():
			data.append([k,v["cui"],y,jsondata[k]["have_had"][y]["cui"],
				jsondata[k]["have_had"][y]["score"],
				jsondata[k]["have_had"][y]["label_semantic_types"],
				jsondata[k]["have_had"][y]["label_ncts_counts"],
				"have_had",
				jsondata[k]["have_had"][y]["ncts"]])
		for y,x in jsondata[k]["looking_for"].items():
			data.append([k,v["cui"],y,jsondata[k]["looking_for"][y]["cui"],
				jsondata[k]["looking_for"][y]["score"],
				jsondata[k]["looking_for"][y]["label_semantic_types"],
				jsondata[k]["looking_for"][y]["label_ncts_counts"],
				"looking_for",
				jsondata[k]["looking_for"][y]["ncts"]])
for x in data:
	csvwriter.writerow(x)
edata.close()





