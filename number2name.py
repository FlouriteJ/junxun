f1 = open("token.csv",'r')
f2 = open("name.csv",'r')
f = open("name_token.csv",'w')
d = {}
for line in f2:
	number , name = line.split(',')
	name = name.strip('\n')
	d[number] = name
for line in f1:
	number , token = line.split(',')
	token = token.strip('\n')
	f.write(d[number])
	f.write(',')
	f.write(token)
	f.write('\n')
	
	
f.close()
f1.close()
f2.close()