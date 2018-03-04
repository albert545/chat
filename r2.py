
#讀取檔案
def read_file(filename):
	lines = []
	with open(filename,'r',encoding = 'utf-8-sig') as f: #uth-8-sig 去掉先前字元
		for line in f:
			lines.append(line.strip())
	return lines

#轉換格式
def convert(lines):
	person = None # 事先宣告 person的值為None
	allen_word_count = 0
	viki_word_count = 0
	for line in lines:
		s = line.split(' ')  #分割清單
		time = s[0]          #取出0 欄
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				allen_word_count += len(m)
		if name == 'Viki':
			for m in s[2:]:
				viki_word_count += len(m)
	print('allen say:' , allen_word_count)	
	print('viki say:' , viki_word_count)

#寫入檔案
def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('[LINE]Viki.txt')
	#print(lines)
	lines = convert(lines) #複寫回 lines清單
	#write_file('output.txt', lines)

main()