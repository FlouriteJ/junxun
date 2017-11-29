import re, os, shutil
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r'D:\政工\人脸检测\data0')
else:
	path_list.append(Path)
while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		filename = path_filename[0:-4]
		os.rename(path_i,os.path.join(r"D:\政工\人脸检测\data0",filename + '_3' + ".jpg"))
		print(filename)
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass
# 马鸿英