import re, os, shutil
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r'D:\政工\军装照\分班')
else:
	path_list.append(Path)

while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-6:-1][::-1] == "0.jpg":
		print(os.path.join(r"D:\政工\军装照\待识别",os.path.basename(path_i)[0:-6] + ".jpg"))
		shutil.copy(path_i,os.path.join(r"D:\政工\军装照\待识别",os.path.basename(path_i)[0:-6] + ".jpg"))
		
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass