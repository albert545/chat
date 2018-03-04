
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename,'r',encoding = 'utf-8-sig') as f: #uth-8-sig 去掉先前字元
		for line in f:
			lines.append(line.strip())
	return lines

#轉換格式
def convert(lines):
	new = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		new.append(person + ':' + line)
	print(new)



def main():
	lines = read_file('input.txt')
	#print(lines)
	convert(lines)

main()