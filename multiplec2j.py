"""
@author ayaz wani
below is a python progam to convert multiple csv files to aa single json file 

"""
import csv,json
import glob
jsonFilePath = 'multiple.json'

data={}
data_folder="csvs"
for filename in glob.iglob(data_folder+"/*.csv"):
	with open(filename) as csvf:
		csv_reader = csv.DictReader(csvf)
		for index ,row in enumerate(csv_reader):
		condition = row['condition']
		condition_cui=row['condition_cui']
		if index == 0:
			pass
		
			data[condition]={}
			data[condition]['cui']=condition_cui
			data[condition]['have_had']={}
			data[condition]['looking_for']={}

		data[condition][row['label_bucket']][row['label']]={}
		data[condition][row['label_bucket']][row['label']]['cui']=row['label_cui']
		data[condition][row['label_bucket']][row['label']]['score']=row['label_score']
		data[condition][row['label_bucket']][row['label']]['label_semantic_types']=row['label_semantic_types']
		data[condition][row['label_bucket']][row['label']]['label_ncts_counts']=row['label_ncts_count']
		data[condition][row['label_bucket']][row['label']]['ncts']=row['label_ncts']				
with open(jsonFilePath,'w',encoding='utf-8') as jsf:
	jsf.write(json.dumps(data,sort_keys=True,indent=4))