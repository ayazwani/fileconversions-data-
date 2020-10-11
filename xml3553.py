"""
AUTHOR 
AYAZ WANI	
following program contains the code to parse and convert 3553 xml files to a single csv using python 

"""
import xml.etree.ElementTree as ET
import csv,glob


d=[]
d2=[]
testdata = open('combined.csv', 'w')
csvwriter = csv.writer(testdata)
csvwriter.writerow(["nct_id","overall_status","start_date","completion_date","primary_completion_date"
	,"has_expanded_access","enrollment","study_pop","criteria","gender","minimum_age""maximum_age"
	,"condition"])

data_folder="search_result"
for filename in glob.iglob(data_folder+"/*.xml"):
	tree = ET.parse(filename)
	root = tree.getroot()
	s1=''
	for i,c in enumerate(root):
		#print(c.tag)
		if c.tag == "id_info":
			for x in root[i]:
				#print(x.tag)
				if x.tag=="nct_id":
					if x.text:
						d.append(x.text)
					else:
						d.append("NA")
					break	

		if c.tag == "eligibility":
			for x in root[i]:
				#print(x.tag)
				#print("hello")
				if x.tag =="criteria":
				 	#print(x[0].text)
				 	if x[0].text:
				 		d.append(x[0].text)
				 	else:
				 		d.append("NA")
				if x.tag =="gender":
					if x.text:
						d.append(x.text)
					else:
						d.append("NA")
				if x.tag =="minimum_age":
					if x.text:
						d.append(x.text)
					else:
						d.append("NA")
				if x.tag =="maximum_age":
					if x.text:
						d.append(x.text)
					else:
						d.append("NA")
				if x.tag =="sampling_method":
					if x.text:
						d.append(x.text)
					else:
						d.append("NA")
				if x.tag =="study_pop":
					if x[0].text:
						d.append(x[0].text)
					else:
						d.append("NA")

		if c.tag == "overall_status":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")
		if c.tag == "start_date":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")

		if c.tag == "completion_date":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")

		if c.tag == "primary_completion_date":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")

		if c.tag == "has_expanded_access":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")

		if c.tag == "enrollment":
			if c.text:
				d.append(c.text)
			else:
				d.append("NA")
		if c.tag == "condition":
			if c.text:
				d2.append(c.text)
			else:
				d2.append(" ")

	listToStr = ' '.join(map(str, d2)) 
	d.append(listToStr)
	print(d)
	d2.clear()
	listToStr=''
	csvwriter.writerow(d)
	d.clear()


testdata.close()