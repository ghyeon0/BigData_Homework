import sys

# 유니코드 한글 카운트
unifreq = [0 for i in range(11172)]
# 유니코드 한글 확률
uni_probability = [0.0 for i in range(11172)]
# 전체 한글 갯수
total_hangul = 0

def if_utf8(text):
    first = ""
    second = ""
    third = ""
    idx = 0
    while idx < len(text):
        first = text[idx]
        idx += 1

        if first & 0x80:
            second = text[idx]
            idx += 1
            third = text[idx]
            idx += 1
        
        if first >= 0xE0 and first <= 0xEF and second >= 0x80 and second <= 0xBF and third >= 0x80 and third <= 0xBF:
            count_idx = ((first & 0x0f) << 12) | ((second & 0x3f) << 6) | (third & 0x3f)
            count_idx -= 0xAC00

            try:
                unifreq[count_idx] += 1
            except:
                pass
            global total_hangul
            total_hangul += 1


def utf8_calc():
    for i in range(11172):
        if unifreq[i]:
            uni_probability[i] = unifreq[i] / total_hangul


def calc_probability(sentence):
    first = ""
    second = ""
    third = ""
    idx = 0
    probability = 1
    while idx < len(sentence):
        first = sentence[idx]
        idx += 1

        if first & 0x80:
            second = sentence[idx]
            idx += 1
            third = sentence[idx]
            idx += 1
        
        if first >= 0xE0 and first <= 0xEF:
            prob_idx = ((first & 0x0f) << 12) | ((second & 0x3f) << 6) | (third & 0x3f)
            prob_idx -= 0xAC00
            probability *= uni_probability[prob_idx]

    return probability
    

def main(file_name, sentence):
    f = open(file_name, "rb")
    text = f.read()
    f.close()
    if_utf8(text)
    utf8_calc()
    sentence_probability = calc_probability(sentence.encode())
    print("생성 확률:", sentence_probability)


if __name__ == "__main__":
    # 실행할 때 매개변수로 파일명 지정
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        sentence = input("문장 입력: ")
    elif len(sys.argv) == 3:
        file_name = sys.argv[1]
        sentence = sys.argv[2]
    # 아니면 입력 받음
    else:
        file_name = input("Input File Name: ")
        sentence = input("문장 입력: ")
    main(file_name, sentence)