from wordcloud import WordCloud
import re
from operator import itemgetter
import time


class Unigram:
    def __init__(self, data):
        self.data = data
        self.font_path = './d2coding.ttf'
    
    def process_data(self):
        sample_data = self.data
        sample_data = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', sample_data)
        sample_data = sample_data.replace("\n", " ").replace("\r", " ")
        sample_data = sample_data.split()
        parsed_data = []

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
        return parsed_data

    def main(self):
        parsed_data = self.process_data()
        start = time.time()
        count = self.get_unigram_data(parsed_data)
        print(time.time() - start)
        self.make_unigram_wordcloud(count)
    
    def get_unigram_data(self, parsed_data):
        word_count_dic = {}
        for each in parsed_data:
            if each not in word_count_dic:
                word_count_dic[each] = 1
            else:
                word_count_dic[each] += 1
        f = open("unigram_frequency.txt", 'w')
        sorted_word_count_dic = sorted(word_count_dic.items(), key=itemgetter(1), reverse=True)
        for each in sorted_word_count_dic:
            f.write(str(each) + "\n")
        f.close()
        return word_count_dic

    def get_unigram_data_multi(self, parsed_data):
        word_count_dic = {}
        

    def make_unigram_wordcloud(self, count):
        wordcloud = WordCloud(
            font_path = self.font_path,
            width = 800,
            height = 800,
            background_color = "white"
        )
        gen = wordcloud.generate_from_frequencies(count)
        array = gen.to_array()
        self.show_as_image(array)

    def show_as_image(self, data):
        import matplotlib.pyplot as plt
        plt.imshow(data, interpolation="bilinear")
        plt.axis("off")
        plt.show()