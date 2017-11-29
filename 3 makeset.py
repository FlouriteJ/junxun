def set_create():
	import requests
	import re
	import cv2
	from time import sleep
	url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"

	data = {
		'api_key' : "",
		'api_secret' : "",
		'display_name' : "junzhuangzhao",
		'outer_id' : "junzhuangzhao"
	}

	r = requests.post(url,data = data)
		
	print(r.text)
	"""{"faceset_token": "deb742a6c8a1b18c4173fcc68beafa6d", "time_used": 125, "face_count": 0, "face_added": 0, "request_id": "1504469354,06dee5b3-e9f7-4a1a-b6fe-d33727ead0dc", "outer_id": "junzhuangzhao", "failure_detail": []}"""
set_create()