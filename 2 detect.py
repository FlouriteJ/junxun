l = []
def detect_faces(path,path_filename):
	import requests
	import re
	import cv2
	import numpy as np
	from time import sleep
	
	number = path_filename[0:-4]
		
	url = "https://api-cn.faceplusplus.com/facepp/v3/detect"

	data = {
		'api_key' : "",
		'api_secret' : "",
		'return_landmark' : 1,
		'return_attributes' : "gender,age,smiling,headpose,facequality,blur,eyestatus,emotion,ethnicity,beauty,mouthstatus,eyegaze"
	}

	files = {'image_file' :  open(path, 'rb')}
	r = requests.post(url,files = files,data = data)
	
	if re.search("CONCURRENCY",r.text):
		print("busy")
		sleep(2)
		detect_faces(path,path_filename)
		return
	rectangles = re.findall(r'(?:"face_rectangle": {"width": )(\d+?)(?:, "top": )(\d+?)(?:, "left": )(\d+?)(?:, "height": )(\d+?)(?:}, "face_token": ")(\w+?)(?:")',r.text)
	f = open(os.path.join(r'D:\政工\军装照\detected',number + ".txt"),'w')
	f.write(r.text)
	f.close()
	
	# 中文路径读取
	img = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
	height, width = img.shape[:2]
	size = int(min(height,width)/20)
	num = 0
	for rectangle in rectangles:
		num+=1
		w = int(rectangle[0])
		y = int(rectangle[1])
		x = int(rectangle[2])
		h = int(rectangle[3])
		token = rectangle[4]
		cv2.imencode('.jpg',img[y:y+h,x:x+w])[1].tofile(os.path.join(r"D:\政工\军装照\token_detected", token + ".jpg"))
		f = open("token.csv",'a')
		f.write(number)
		f.write(',')
		f.write(token)
		f.write('\n')
		f.close()
		print(path_filename,token)
		
	# 画检测框	
	for rectangle in rectangles:
		w = int(rectangle[0])
		y = int(rectangle[1])
		x = int(rectangle[2])
		h = int(rectangle[3])
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), int(size/10))

	# 若存在，提取图像
	if len(rectangles):	
		cv2.imencode('.jpg',img)[1].tofile(os.path.join(r"D:\政工\军装照\detected", number + ".jpg"))

	else:
		print(r.text)
		l.append(path)
		
import re, os
path_list=[]
Path=input('Path:')
if Path == '':
	path_list.append(r'D:\政工\军装照\待识别')
else:
	path_list.append(Path)
while path_list != []:
	path_i=path_list.pop()
	if not os.path.exists(path_i):
		continue
	path_filename=os.path.basename(path_i).lower()
	if path_filename[-1:-4:-1][::-1] == "jpg":
		detect_faces(path_i,path_filename)
		print(path_i)
	try:
		if os.path.isdir(path_i):
			path_i_list=os.listdir(path_i)
			if path_i_list != []:
				path_list.extend([os.path.join(path_i, filename) for filename in path_i_list])
	except:
		pass

print("===================")		
for p in l:
	print (p)