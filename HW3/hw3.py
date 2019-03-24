import re
import sys

f = open("sample.txt", "r")
sample_data = f.read()
f.close()

sample_data = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', sample_data)
sample_data = sample_data.split()

parsed_data = []

for each in sample_data:
    if each != " ":
        parsed_data.append(each)

word_count = {}
total_word_count = 0

for each in sample_data:
    if each not in word_count:
        word_count[each] = 1
    else:
        word_count[each] += 1
    total_word_count += 1
    
probability_dic = {}
for key in word_count.keys():
    probability_dic[key] = word_count[key] / total_word_count

if len(sys.argv) == 2:
    input_string = sys.argv[1]
else:
    input_string = input("Input Text: ")

input_string = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', input_string)

input_data = input_string.split()

sentence_probability = 1

for each in input_data:
    try:
        sentence_probability *= probability_dic[each]
    except KeyError:
        print("Key Not Found", "Key:", each)
        sys.exit()

print("문장 생성 확률:", sentence_probability)