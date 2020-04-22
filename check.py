import os

labels = os.listdir('labels/esophagitis')
images = os.listdir('images/esophagitis')

for file in images:
	if file[:-4]+".txt" not in labels:
		os.remove('images/esophagitis/'+file)

labels = os.listdir('labels/polyps')
images = os.listdir('images/polyps')

for file in images:
	if file[:-4]+".txt" not in labels:
		os.remove('images/polyps/'+file)

for file in os.listdir('labels/esophagitis'):
	statinfo = os.stat('labels/esophagitis/'+file)
	if int(statinfo.st_size)==0:
		os.remove('labels/esophagitis/'+file)
		os.remove('images/esophagitis/'+file[:-4]+".jpg")
		print(file[:-4]+".jpg")

for file in os.listdir('labels/polyps'):
	statinfo = os.stat('labels/polyps/'+file)
	if int(statinfo.st_size)==0:
		os.remove('labels/polyps/'+file)
		os.remove('images/polyps/'+file[:-4]+".jpg")
		print(file[:-4]+".jpg")

###Final Check#####
labels = os.listdir('labels/esophagitis')
images = os.listdir('images/esophagitis')

if len(labels)!=len(images):
	print("LENGTH UNEQUAL")

for file in images:
	if file[:-4]+".txt" not in labels:
		print("LABEL NOT EXIST")

	else:
		statinfo = os.stat('labels/esophagitis/'+file[:-4]+".txt")
		if int(statinfo.st_size)==0:
			print("LABEL FILE EMPTY")

labels = os.listdir('labels/polyps')
images = os.listdir('images/polyps')

if len(labels)!=len(images):
	print("LENGTH UNEQUAL")

for file in images:
	if file[:-4]+".txt" not in labels:
		print("LABEL NOT EXIST")

	else:
		statinfo = os.stat('labels/polyps/'+file[:-4]+".txt")
		if int(statinfo.st_size)==0:
			print("LABEL FILE EMPTY")
