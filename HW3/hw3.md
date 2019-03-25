## 빅데이터최신기술 과제 3 - 문장생성확률 계산(Unigram)

#### 20171701 정지현

전체 레포지토리 링크: https://github.com/ghyeon0/BigData_Homework/tree/master/HW3

혹시 보고서 형식이 많이 깨진다면 https://github.com/ghyeon0/BigData_Homework/blob/master/HW3/hw3.md 를 참조 부탁드립니다.



##### 1. 알고리즘

```python
f = open("sample.txt", "r")
sample_data = f.read()
f.close()
```

- 파일에서 텍스트를 불러옴.

```python
sample_data = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', sample_data)
sample_data = sample_data.split()
```

- 정규표현식을 이용해서 문장 부호 및 특수문자 등을 띄어쓰기로 치환한 다음, 띄어쓰기를 기준으로 단어를 분리한다.

```python
parsed_data = []

for each in sample_data:
    if each != " ":
        parsed_data.append(each)
```

- 위에서 치환하면서 띄어쓰기 한 칸이 단어로 인식되는 경우가 발생하여 그 경우를 제외해주었다.

```python
word_count = {}
total_word_count = 0

for each in sample_data:
    if each not in word_count:
        word_count[each] = 1
    else:
        word_count[each] += 1
    total_word_count += 1
```

- 각 단어의 개수와 전체 단어의 개수를 세어주었다.
- 각 단어는 dictionary를 이용하여 갯수를 세었다.

```python
probability_dic = {}
for key in word_count.keys():
    probability_dic[key] = word_count[key] / total_word_count
```

- 위에서 저장한 dictionary의 각 key별로 어절 출현 확률을 계산해서 저장했다.

```python
if len(sys.argv) == 2:
    input_string = sys.argv[1]
else:
    input_string = input("Input Text: ")
    
input_string = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', input_string)

input_data = input_string.split()
```

- 생성 확률을 계산할 문장에 대해서도 문장 부호 제거 후 띄어쓰기를 기준으로 분할하는 작업을 진행한다.

```python
sentence_probability = 1

for each in input_data:
    try:
        sentence_probability *= probability_dic[each]
    except KeyError:
        print("Key Not Found", "Key:", each)
        sys.exit()

print("문장 생성 확률:", sentence_probability)
```

- 각 단어에 대한 확률을 모두 곱하면서 최종 확률을 구한다.
- 단, 키가 존재하지 않는다면 Key Not Found를 출력하고 종료한다.



##### 2. 사용법

```python
python3 hw3.py {확률 계산할 문장}
```



##### 3. 실행결과

```bash
python3 hw3.py '컴퓨터가 고장나서 서비스센터에 갔는데, 아직 보증 기간이 지나지 않아서 돈을 내지 않고 수리를 받을 수 있었습니다.'
```

![Screen Shot 2019-03-24 at 2 20 10 PM](https://user-images.githubusercontent.com/13490996/54875313-0af1c100-4e40-11e9-9655-b72a5e46ee27.png)

```bash
python3 hw3.py '그는 루머에 대해 사실이 아니라고 밝혔다.' # 확률이 높은 몇 가지 단어를 합친 문장
```

![Screen Shot 2019-03-24 at 2 22 58 PM](https://user-images.githubusercontent.com/13490996/54875324-5c9a4b80-4e40-11e9-9b60-1250f85bcd59.png)

```bash
python3 hw3.py '어제 저녁에는 친구와 만나서 치킨을 먹었다.'
```

![Screen Shot 2019-03-24 at 2 29 22 PM](https://user-images.githubusercontent.com/13490996/54875372-40e37500-4e41-11e9-937c-5ddb6e1c093e.png)

```bash
python3 hw3.py '나는 밥을 먹고 학교에 간다'
```

![Screen Shot 2019-03-25 at 5 02 52 PM](https://user-images.githubusercontent.com/13490996/54903727-ecfb8d80-4f1f-11e9-8b8f-2f5e88413fdb.png)

```bash
python3 hw3.py '나는 법을 먹고 학교에 간다'
```

![Screen Shot 2019-03-25 at 5 04 23 PM](https://user-images.githubusercontent.com/13490996/54903810-187e7800-4f20-11e9-84c5-f6eceeadc1a0.png)

```bash
python3 hw3.py '나는 밥을 묵고 학교에 간다'
```

![Screen Shot 2019-03-25 at 5 05 26 PM](https://user-images.githubusercontent.com/13490996/54903860-377d0a00-4f20-11e9-81d9-f3a693159bab.png)

```bash
python3 hw3.py '너는 밥을 먹고 학교에 간다'
```

![Screen Shot 2019-03-25 at 5 06 23 PM](https://user-images.githubusercontent.com/13490996/54903910-59768c80-4f20-11e9-821b-2adaef4930d9.png)

```bash
python3 hw3.py '너는 법을 묵고 학교에 산다'
```

![Screen Shot 2019-03-25 at 5 07 31 PM](https://user-images.githubusercontent.com/13490996/54903962-832fb380-4f20-11e9-972d-5501c1f52678.png)

- Unigram 분석의 한계로 '밥을 먹고' 보다 '법을 먹고'의 확률이 더 높게 나오는 문제가 발생하였다.

##### 4. 아쉬웠던 점

문장부호만 제거하는것이 아닌 조사같은 불용어 부분도 제거했으면 좀 더 좋은 결과를 얻을 수  있었을 것 같다.



##### 5. 전체 소스코드

```python
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

input_string = sys.argv[1]
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
```

