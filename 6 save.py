def save_name(name,path):
	import os
	filename_list = []	
	confidence_list = []
	f = open(os.path.join(r'D:\政工\人脸检测\value',name + '.csv'),'r')
	for line in f:
		filename , confidence = line.split(',')
		confidence = confidence.strip('\n')
		print(name,confidence)
		if float(confidence)>70:
			filename_list.append(filename)
			confidence_list.append(confidence)
	f.close()
	
	c = 0
	import re, os, shutil
	path_list=[]
	path_list.append(r'D:\政工\人脸检测\data')

	while path_list != []:
		path_i=path_list.pop()
		if not os.path.exists(path_i):
			continue
		path_filename=os.path.basename(path_i).lower()
		if path_filename[-1:-4:-1][::-1] == "jpg":
			filename = path_filename[0:-4]
			if filename in filename_list:
				shutil.copy(path_i,os.path.join(path,filename + '_' + confidence_list[c] + ".jpg"))
				c+=1
				print(filename)
				
		try:
			if os.path.isdir(path_i):
				path_i_list=os.listdir(path_i)
				if path_i_list != []:
					path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
		except:
			pass

			
import os

f = open("name.csv",'r')
for line in f:
	number , name = line.split(',')
	name = name.strip('\n')
	save_name(name,os.path.join(r"D:\政工\分人汇总",name))
	
f.close()