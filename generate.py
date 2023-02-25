from shutil import copyfile
import os



class_list = []
replace_list = []
data_type = 'class'



# ======================================
# 데이타 읽기
# ======================================
f = open("generate.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
	line = line.strip()
	if line.startswith('#'):
		if 'class' in line:
			data_type = 'class'
		elif 'replace' in line:
			data_type = 'replace'
	else:
		if line.strip() != '':
			if data_type == 'class':
				class_list.append(line.strip())
			elif data_type == 'replace':
				replace_list.append(line.strip())
f.close()



for src_path in class_list:
	dest_path = src_path
	for r in replace_list:
		r = r.split('\t')
		dest_path = dest_path.replace(r[0], r[1])
	os.makedirs(os.path.dirname(dest_path), exist_ok=True)
	copyfile(src_path, dest_path)
	filedata = ''
	with open(dest_path, 'r') as file:
		filedata = file.read()
		for r in replace_list:
			r = r.split('\t')
			filedata = filedata.replace(r[0], r[1])
	with open(dest_path, 'w') as file:
		file.write(filedata)
