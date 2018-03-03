#Print all files in the given dir & subdirs

import os
'''
f = list(os.walk(os.getcwd()))

for i in range(len(f)):
  print(f[i][2])
'''
  
#############################

def dir1(path):
	list1=[]
	files = os.listdir(path)
	for i in files:
		new_path = os.path.join(path,i)
		if(os.path.isdir(new_path)):
			d = dir1(new_path)
			if d:
				list1 = list1 + d
		else:
			list1.append(i)
	return list1

print(dir1("f:\\Kotul"))