all = 0
least = 27
def search_faces(token):
	import requests
	import re
	import cv2
	from time import sleep
	url = "https://api-cn.faceplusplus.com/facepp/v3/search"

	data = {
		'api_key' : "",
		'api_secret' : "",
		'outer_id' : "junzhuangzhao",
		'return_result_count' : 5,
		'face_token' : token
	}
	try:
		r = requests.post(url,data = data,timeout = 5)
	except:
		print("timeout")
		sleep(1)
		return search_faces(token)
		
	if re.search("CONCURRENCY",r.text):
		print("busy")
		sleep(2)
		return search_faces(token)
	
	match = re.search(r"(?:\"confidence\": )(.+?)(?:,)",r.text)
	confidence = match.group(1)
	match = re.search(r"(?:\"face_token\": \")(.+?)(?:\")",r.text)
	face_token = match.group(1)
	return face_token, confidence

d = {}

def detect_faces(path,path_filename):
	import requests
	import re
	import cv2
	import numpy as np
	from time import sleep
	
	filename = path_filename[0:-4]
		
	url = "https://api-cn.faceplusplus.com/facepp/v3/detect"

	data = {
		'api_key' : "3AEvXiO2ucUXv2OZXxTe7QJn5hBCPurO",
		'api_secret' : "tGUpgsBLgfJWXlf3H5K2XkvmsUf9eLwD",
		'return_landmark' : 1,
	}

	files = {'image_file' :  open(path, 'rb')}
	try:
		r = requests.post(url,files = files,data = data,timeout = 5)
	except:
		print("timeout")
		sleep(1)
		detect_faces(path,path_filename)
		return 
	
	if re.search("CONCURRENCY",r.text):
		print("busy")
		sleep(2)
		detect_faces(path,path_filename)
		return
	rectangles = re.findall(r'(?:"face_rectangle": {"width": )(\d+?)(?:, "top": )(\d+?)(?:, "left": )(\d+?)(?:, "height": )(\d+?)(?:}, "face_token": ")(\w+?)(?:")',r.text)
	
	f1 = open(os.path.join(r'D:\政工\人脸检测\detected',filename + ".txt"),'w')

	img = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
	height, width = img.shape[:2]
	size = int(min(height,width)/20)
	num = 0
	name_list = []
	for rectangle in rectangles:
		num+=1
		w = int(rectangle[0])
		y = int(rectangle[1])
		x = int(rectangle[2])
		h = int(rectangle[3])
		token = rectangle[4]
		
		face_token, confidence = search_faces(token)
		name = d[face_token]
		if len(name_list) < 30:
			name_list.append(name)
		if float(confidence) > 80:
			cv2.imencode('.jpg',img[y:y+h,x:x+w])[1].tofile(os.path.join(r"D:\政工\人脸检测\face_detected", name + '_' + filename + ".jpg"))
		else:
			cv2.imencode('.jpg',img[y:y+h,x:x+w])[1].tofile(os.path.join(r"D:\政工\人脸检测\face_detected\else", name + '_' + filename + ".jpg"))
		
		f = open(os.path.join(r"D:\政工\人脸检测\value",name + '.csv'),'a')
		f.write(filename)
		f.write(',')
		f.write(confidence)
		f.write('\n')
		f.close()
		
		f1.write(name)
		f1.write(',')
		f1.write(confidence)
		f1.write('\n')
		print(path_filename,name,confidence)
		
	f1.close()
	# 画检测框	
	for rectangle in rectangles:
		w = int(rectangle[0])
		y = int(rectangle[1])
		x = int(rectangle[2])
		h = int(rectangle[3])
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), int(size/10))

	# 若存在，提取图像
	if len(rectangles):	
		cv2.imencode('.jpg',img)[1].tofile(os.path.join(r"D:\政工\人脸检测\detected", filename + '_' + '_'.join(name_list) + ".jpg"))

	else:
		print(r.text)
			
f = open("name_token.csv",'r')

for line in f:
	name , token = line.split(',')
	token = token.strip('\n')
	print(name,token)
	d[token] = name
f.close()

import re, os
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r'D:\政工\人脸检测\data')
else:
	path_list.append(Path)
while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		if least != 0:
			least-=1
		else:
			detect_faces(path_i,path_filename)
			print(all,path_i)
		all+=1
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass
input()		