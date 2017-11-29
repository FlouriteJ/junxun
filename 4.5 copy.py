import re, os, shutil
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r'D:\政工\照片&视频\军训第12天')
else:
	path_list.append(Path)

while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		print(os.path.join(r"D:\政工\人脸检测\data0",os.path.basename(path_i)[0:-4] + ".jpg"))
		shutil.copy(path_i,os.path.join(r"D:\政工\人脸检测\data0",os.path.basename(path_i)[0:-4] + ".jpg"))
		
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass