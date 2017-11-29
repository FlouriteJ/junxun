d = {}
f = open("name.csv",'r')
for line in f:
	number , name = line.split(',')
	name = name.strip('\n')
	d[number] = name
f.close()

import re, os, shutil
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r"D:\政工\军装照\temp")
else:
	path_list.append(Path)

while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		number = os.path.basename(path_i)[0:-6]
		name = d[number]
		shutil.copy(path_i,os.path.join(os.path.join(r"D:\政工\分人汇总",name),os.path.basename(path_i)))
		print(path_i)
		
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass