import xml.dom.minidom,csv,glob

class X:
	def get_nctid(self,root):
		nct_id=root.getElementsByTagName("nct_id")
		return(nct_id[0].firstChild.data)

	def get_condition(self,root):
		l1=[]
		condition=root.getElementsByTagName("condition")
		for i,tags in enumerate(condition):
			l1.append(condition[i].firstChild.data)
			#str1 = list2string(l1)
			str1 = ''.join(map(str,l1))
			return str1

	def get_name(self,root):
		if(root.getElementsByTagName("name")):
			name = root.getElementsByTagName("name")
			return(name[0].firstChild.data)
		else:
			return("NA")

	def get_city(self,root):
		if(root.getElementsByTagName("city")):
			city = root.getElementsByTagName("city")
			return(city[0].firstChild.data)
		else:
			return("NA")





ob1 = X()

data = []




testdata = open('classcsv.csv', 'w')
csvwriter = csv.writer(testdata)
csvwriter.writerow(["nct_id","condition","facility_name","city"])

data_folder="search_result"
for filename in glob.iglob(data_folder+"/*.xml"):

	domtree = xml.dom.minidom.parse(filename)

	root = domtree.documentElement

	data.append(ob1.get_nctid(root))

	data.append(ob1.get_condition(root))

	data.append(ob1.get_name(root))

	data.append(ob1.get_city(root))




	csvwriter.writerow(data)
	print(data)
	data.clear()



testdata.close()




