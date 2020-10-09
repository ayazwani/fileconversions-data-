"""
@author ayaz wnai
following is the program that take file name as an command line argument and then writes on that file

"""
import sys

#if __name__ == "__main__":
print(f"Arguments count: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
     print(f"Argument {i:>6}: {arg}")

print(sys.argv[1])

file1 = sys.argv[1]

filebody = "this is the body of the file.In the progam we are using python cmd to pass filename as arguments to the python interpreter"

with open(file1,'w') as fp:
	fp.write(filebody)
	
