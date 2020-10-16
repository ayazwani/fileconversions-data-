import xml.dom.minidom

domtree = xml.dom.minidom.parse("NCT00571389.xml")

root = domtree.documentElement

print(root)	

nct_id = root.getElementsByTagName("nct_id")
print(nct_id[0].firstChild.data)

condition = root.getElementsByTagName("condition")
for i,tags in enumerate(condition):
	print(condition[i].firstChild.data)

name = root.getElementsByTagName("name")
print(name[0].firstChild.data)

city = root.getElementsByTagName("city")
print(city[0].firstChild.data)

criteria = root.getElementsByTagName("textblock")
print(criteria[0].firstChild.data)
print(criteria[1].firstChild.data)
print(criteria[2].firstChild.data)
print(criteria[3].firstChild.data)
