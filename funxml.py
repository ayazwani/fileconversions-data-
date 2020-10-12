"""
author ayaz wani
modular code to convert xml files into csv


"""
import xml.etree.ElementTree as ET
import csv,glob


def get_nctid(root):
	id_info = root.find("id_info")
	nctid = id_info.find("nct_id")
	if nctid.text:
		nctid1=nctid.text
	else:
		nctid1="NA"

	return nctid1


def get_condition(root):
	for condition in root.findall("condition"):
		if condition.text:
			#print(condition.text)
			condition_list =(condition.text)
		else:
			condition_list = "NA"

		strcondition = list2string(condition_list)
		return strcondition


def list2string(list1):
	str1 = ''.join(map(str,list1))
	return str1

def get_enrollment(root):	
	if(root.findall("enrollment")):
		return(root.find("enrollment").text)
	else:
		return("NA")	

	

def get_eligibility_sampling(root):
	if(root.find("eligibility")):
		for c in root.find('eligibility').iter():
			if c.tag =="sampling_method":
				return(c.text)
	else:
		return("NA")	

def get_eligibility_gender(root):
	if(root.find("eligibility")):
		for c in root.find('eligibility').iter():
			if c.tag =="gender":
				return(c.text)
	else:
		return("NA")

def get_eligibility_healthy(root):
	if(root.find("eligibility")):
		for c in root.find('eligibility').iter():
			if c.tag =="healthy_volunteers":
				return(c.text)
	else:
		return("NA")

def get_location(root): 
	if(root.findall("location")):
		for c in root.find("location").iter():
			if c.tag =="name":
				return(c.text)
	else:
		return("NA")


def get_location_city(root):
	if(root.find("location")):
		for c in root.find("location").iter():
			if c.tag == "city":
				return(c.text)			
	else:
		return("NA")


def get_location_country(root):
	if(root.find("location")):
		for c in root.find("location").iter():
			if c.tag == "country":
				return(c.text)			
	else:
		return("NA")


data = []
testdata = open('comb.csv', 'w')
csvwriter = csv.writer(testdata)
csvwriter.writerow(["nct_id","condition","enrollment",
					"gender","facility_name","city","country"])

data_folder="search_result"
for filename in glob.iglob(data_folder+"/*.xml"):
	
	tree = ET.parse(filename)
	root = tree.getroot()

	data.append(get_nctid(root))
	data.append(get_condition(root))
	data.append(get_enrollment(root))
	
	data.append(get_eligibility_gender(root))

	data.append(get_location(root))
	data.append(get_location_city(root))

	data.append(get_location_country(root))
	#print(data)

	csvwriter.writerow(data)
	data.clear()

testdata.close()


