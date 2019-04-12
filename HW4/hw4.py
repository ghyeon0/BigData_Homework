from unigram import Unigram
from bigram import Bigram

def get_data():
    f = open("sample.txt", "r")
    sample_data = f.read()
    f.close()
    return sample_data

def main():
    raw_data = get_data()
    # Unigram
    uni = Unigram(raw_data)
    uni.main()
    # Bigram
    bi = Bigram(raw_data)
    bi.main()

if __name__ == "__main__":
    main()
    