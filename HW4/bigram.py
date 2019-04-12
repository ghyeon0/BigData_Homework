from wordcloud import WordCloud
import re
from operator import itemgetter
import random

class Bigram:
    def __init__(self, data):
        self.data = data
        self.font_path = './d2coding.ttf'
        self.parsed_data = []
        self.count = {}
        self.probability = {}
    
    def process_data(self):
        sample_data = self.data
        sample_data = re.sub('[^가-힣0-9a-zA-Z\\s]', '', sample_data)
        sample_data = sample_data.replace("\n", " ").replace("\r", " ")
        sample_data = sample_data.split()
        parsed_data = []

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
        self.parsed_data = parsed_data
        return parsed_data

    def main(self):
        parsed_data = self.process_data()
        count = self.get_bigram_data(parsed_data)
        self.make_bigram_wordcloud(count)
        self.generate_sentence()
    
    def get_bigram_data(self, parsed_data):
        word_count_dic = {}
        for i in range(len(parsed_data) - 1):
            if parsed_data[i] in self.count:
                self.count[parsed_data[i]] += 1
            else:
                self.count[parsed_data[i]] = 1
            data = ""
            for j in range(i, i + 2):
                data += parsed_data[j] + " "
            data = data[:-1]
            if data in word_count_dic:
                word_count_dic[data] += 1
            else:
                word_count_dic[data] = 1
        
        if parsed_data[-1] in self.count:
            self.count[parsed_data[-1]] += 1
        else:
            self.count[parsed_data[-1]] = 1

        f = open("bigram_frequency.txt", 'w')
        sorted_word_count_dic = sorted(word_count_dic.items(), key=itemgetter(1), reverse=True)
        for each in sorted_word_count_dic:
            f.write(str(each) + "\n")
        f.close()

        return word_count_dic

    def make_bigram_wordcloud(self, count):
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

    def generate_sentence(self):
        sample_data = self.data
        sample_data = sample_data.replace(".", ". <End> <Start> ").replace("?", "? <End> <Start> ").replace("!", "! <End> <Start> ")
        sample_data = sample_data.replace("\n", " ").replace("\r", " ")
        sample_data = re.sub('[^가-힣0-9a-zA-Z<>\\s]', '', sample_data)
        sample_data = sample_data.split()
        self.count["<Start>"] = sample_data.count("<Start>")
        self.count["<End>"] = sample_data.count("<End>")
        parsed_data = []

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
        
        word_count_dic = {}
        for i in range(len(parsed_data) - 1):
            data = ""
            for j in range(i, i + 2):
                data += parsed_data[j] + " "
            data = data[:-1]

            if data == "<End> <Start>":
                continue
            if data in word_count_dic:
                word_count_dic[data] += 1
            else:
                word_count_dic[data] = 1
        
        probability_dic = {}
        for key in word_count_dic.keys():
            try:
                xy = key
                x = key.split()[0]
                temp_key = (x, xy)
                probability_dic[temp_key] = word_count_dic[xy] / self.count[x]
            except:
                pass

        sorted_probability_dic = sorted(probability_dic.items(), key=itemgetter(0))
        f = open("bigram_probability.txt", 'w')
        for each in sorted_probability_dic:
            f.write(str(each) + "\n")
        f.close()

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
        self.parsed_data = parsed_data

        word_information = {"<Start>": {}}
        for i in range(len(self.parsed_data) - 1):
            if self.parsed_data[i] in word_information:
                if self.parsed_data[i + 1] in word_information[self.parsed_data[i]]:
                    word_information[self.parsed_data[i]][self.parsed_data[i + 1]] += 1
                else:
                    word_information[self.parsed_data[i]][self.parsed_data[i + 1]] = 1
            else:
                word_information[self.parsed_data[i]] = {}

        for i in range(30):
            current_token = "<Start>"
            sentence = ""
            while current_token != "<End>":
                # print(current_token)
                next_words = word_information[current_token]
                sorted_next_words = sorted(next_words.items(), key=itemgetter(1), reverse=True)
                sorted_next_words = sorted_next_words[:5]
                try:
                    # idx = 0
                    idx = random.randint(0, len(sorted_next_words) - 1)
                except:
                    current_token = "<Start>"
                    sentence = ""
                else:
                    current_token = sorted_next_words[idx][0]
                    sentence += sorted_next_words[idx][0] + " "
            sentence = sentence[:-7]
            print(sentence)
            print()
