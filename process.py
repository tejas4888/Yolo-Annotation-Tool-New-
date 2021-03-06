import glob, os

# Current directory
#current_dir = os.path.dirname(os.path.abspath(__file__))

#print(current_dir)

#current_dir = 'images/cat'

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('valid.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = 0 #round(100 / percentage_test) ==> Uncomment if you need test set
classes=os.listdir('images')
for current_dir in classes:
	current_dir = 'images/'+current_dir
	for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
	    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

	    if counter == index_test:
	        counter = 1
	        file_test.write("data/custom/"+current_dir + "/" + title + '.jpg' + "\n")
	    else:
	        #file_train.write("data/custom/"+current_dir + "/" + title + '.jpg' + "\n")
	        #Commented for directing entire set to validation
	        file_test.write("data/custom/"+current_dir + "/" + title + '.jpg' + "\n")
	        
	        counter = counter + 1
