import re

file = open("regex_sum_1890061.txt")

text = file.read()

number_final = re.findall('[0-9]+',text)

total = 0
for i in number_final:
    i = int(i)
    total = total + i;

print(total)

file.close()