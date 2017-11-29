def set_add(token):
	import requests
	import re
	import cv2
	from time import sleep
	url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"

	data = {
		'api_key' : "",
		'api_secret' : "",
		'outer_id' : "junzhuangzhao",
		'face_tokens' : token
	}
	r = requests.post(url,data = data)
	if re.search("CONCURRENCY",r.text):
		print("busy")
		sleep(2)
		set_add(token)
		return
	print(r.text)
	
		
import re, os
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r"D:\政工\军装照\token_detected")
else:
	path_list.append(Path)
while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		print(path_filename[0:-4])
		set_add(path_filename[0:-4])
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass
