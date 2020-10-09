import csv
import json
import os,sys

def makejson(csvfilepath):
	data={}
	

	with open(csvfilepath,encoding='utf-8') as csvf:
		
		csvreader=csv.DictReader(csvf)
		for index,row in enumerate(csvreader):
			condition=row["condition"]
			condition_cui=row["condition_cui"]
			if(index==0):
				data[condition]={}
				data[condition]["cui"]=condition_cui
				data[condition]["have_had"]={}
				data[condition]["looking_for"]={}

			data[condition][row["label_bucket"]][row["label"]]={}
			data[condition][row["label_bucket"]][row["label"]]["cui"]=row["label_cui"]
			data[condition][row["label_bucket"]][row["label"]]["score"]=row["label_score"]
			data[condition][row["label_bucket"]][row["label"]]["label_semantic_types"]=row["label_semantic_types"]
			data[condition][row["label_bucket"]][row["label"]]["label_ncts_counts"]=row["label_ncts_count"]
			data[condition][row["label_bucket"]][row["label"]]["ncts"]=row["label_ncts"]
	with open("combined.json",'w') as js:
		js.write(json.dumps(data,sort_keys=True,indent=4))
	
	return 


def makecsv(jfilepath):
	jsonfile=open(jfilepath,'r')
	jsondata = json.load(jsonfile)
	edata = open('1.csv', 'w')
	csvwriter = csv.writer(edata)
	data=[]
	csvwriter.writerow(["condition","condition_cui","label",
			"label_cui","label_score","label_semantic_types",
			"label_ncts","label_bucket","label_ncts_count"])
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

	return 


file_namescsv=sys.argv[1]
file_namesjson=sys.argv[2]

makejson(file_namescsv)

makecsv(file_namesjson)

