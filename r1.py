
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
	person = None # 事先宣告 person的值為None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #有值才執行 避免 person 當掉
			new.append(person + ':' + line)
	return new
#寫入檔案
def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('input.txt')
	#print(lines)
	lines = convert(lines) #複寫回 lines清單
	write_file('output.txt', lines)

main()