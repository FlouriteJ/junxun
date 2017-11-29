import os

f = open("name.csv",'r')

for line in f:
	number , name = line.split(',')
	name = name.strip('\n')
	os.mkdir(os.path.join(r"D:\政工\分人汇总",name))
	
f.close()