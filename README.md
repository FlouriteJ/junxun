# junxun
Last year, I took part in the military training(Jun Xun) as an ideological work staff(Zheng Gong). During the training, I took lots of pictures of my company. Near the end of the training, I would like to hand out each picture to anyone who is in it. However, the pictures are so many(~2000) that I cannot recognize everyone in each of them on my own. So I tried on an API of Face++. After taking photos of each classmate and running the code, I gave everyone who is in my company about 30 pictures he/she may be in the picture. 

2017年暑假军训时，作为政工拍摄照片，进行人脸检测后将它们分发给每个人。
## 详细计划
制定拍摄定妆照名单

拍摄&补拍

整理拍摄名单，备注班级
### 0 rename
处理照片，重命名  # 1班少1人	
### 1 copy
提取不戴帽照片
### PS cc
处理图片，缩小到2M以下，分辨率 2688*4032
### 2 detect
识别图像，将返回值和带框原图放在一个文件夹中，文件名为序号；将识别的人脸部分放在另一个文件夹中，文件名为图片代码token；将人脸代号，对应的token保存在csv文件中

将部分识别不出的照片人脸部位放大，然后重新识别
### 3 makeset
建立人脸图片集
### 4 addset
将识别出的token加入到人脸图片集中

*人脸序号：对人进行预先编号
### PS cc
处理待搜索照片
### number2name
把人脸序号对应token的csv转为人名对应token的csv
### 5 search
识别每张照片，对每张图片进行搜索，将识别的人脸部分放在一个文件夹中，文件名为可信度最高的人脸代号_原图片名称；最后，在人脸序号为名的txt文件下添加照片名字。对每张照片，保存带框照片，文件名为原图片名称_人脸1名字_人脸2名字。 
### 6 save
遍历某人脸序号的txt文件，保存其照片

由于两次拍摄有同名文件，将一部分重命名后重新检测
