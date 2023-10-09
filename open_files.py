xml_file = open('data.xml', 'r')
# print(*xml_file)
xml_file.close()

txt_file = open('data.txt', 'r')
# print(*txt_file)
# Список для строчек в файле data.txt
list_lines_txt = []

while True:
    line = txt_file.readline()
    
    if not line:
        break
    
    # print(line.strip())
    list_lines_txt.append(line.strip())

print(list_lines_txt)    
txt_file.close()