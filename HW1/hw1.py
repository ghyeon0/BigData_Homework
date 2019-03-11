import sys

# ASCII 카운트
freq = [0 for i in range(128)]
# KS 완성형 카운트
hfreq = [[0 for i in range(94)] for j in range(25)]
# 유니코드 한글 카운트
unifreq = [0 for i in range(11172)]


# 인코딩이 utf-8인지 검증
def is_utf8(text):
    lst = []
    for each in text:
        if each >= 128:
            lst.append(each)
    for i in range(0, len(lst), 3):
        if lst[i] < 0b11100000:
            return False
    return True


# 파일이 KS 완성형인 경우
def if_ks(text):
    first = ""
    second = ""
    idx = 0
    while idx < len(text):
        first = text[idx]
        idx += 1

        if first & 0x80:
            second = text[idx]
            idx += 1

        # ASCII
        if first < 128:
            freq[first] += 1
        
        if first >= 0xB0 and first <= 0xC8 and second >= 0xA1 and second <= 0xFE:
            hfreq[first - 0xB0][second - 0xA1] += 1

    ks_print()


# KS 완성형 빈도 출력
def ks_print():
    for i in range(25):
        for j in range(94):
            if hfreq[i][j]:
                print(bytes([i + 0xB0, j + 0xA1]).decode('cp949') + ":", hfreq[i][j])
    print("KS 완성형")
            

# 파일이 UTF-8 인코딩인 경우
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

        if first < 128:
            freq[first] += 1
        
        if first >= 0xE0 and first <= 0xEF:
            count_idx = ((first & 0x0f) << 12) | ((second & 0x3f) << 6) | (third & 0x3f)
            count_idx -= 0xAC00
            unifreq[count_idx] += 1
    
    utf8_print()


# UTF-8 빈도 출력
def utf8_print():
    for i in range(11172):
        if unifreq[i]:
            num = i + 0xAC00
            first = num >> 12
            first = 0xE << 4 | first
            second = num >> 6 & 0b111111
            second = 0b10000000 | second
            third = num & 0b111111 | 0b10000000
            print(bytes([first, second, third]).decode("utf-8") + ":", unifreq[i])
    print("UTF-8")


def main(file_name):
    f = open(file_name, "rb")
    text = f.read()
    f.close()
    utf8_flag = is_utf8(text)
    if utf8_flag:
        if_utf8(text)
    else:
        if_ks(text)


if __name__ == "__main__":
    # 실행할 때 매개변수로 파일명 지정
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    # 아니면 입력 받음
    else:
        file_name = input("Input File Name: ")
    main(file_name)