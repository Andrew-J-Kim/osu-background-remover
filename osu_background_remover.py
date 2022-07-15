import os
root = "C:/Users/Andrew Kim/AppData/Local/osu!/Songs"
folders = os.listdir(root)
for folder in folders:
	main = root + '/' + folder
	try:
		files = os.listdir(main)
		for file in files:
			if (file.endswith('.jpg') or file.endswith('.png')):
				os.remove(os.path.join(main, file))
	except:
		pass