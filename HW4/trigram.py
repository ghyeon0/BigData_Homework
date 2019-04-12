from wordcloud import WordCloud
import re

class Trigram:
    def __init__(self, data):
        self.data = data
        self.font_path = './d2coding.ttf'
    
    def process_data(self):
        sample_data = "<Start> " + self.data
        # sample_data = re.sub('[^가-힣0-9a-zA-Z\\s]', ' ', sample_data)
        sample_data = sample_data.replace(".", ". <End> <Start>").replace("?", ". <End> <Start>").replace("!", ". <End> <Start>")
        sample_data = sample_data.replace("\n", " ").replace("\r", " ")
        sample_data = sample_data.split(" ")
        parsed_data = []

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
        return parsed_data

    def main(self):
        parsed_data = self.process_data()
        count = self.get_trigram_data(parsed_data)
        self.make_trigram_wordcloud(count)
    
    def get_trigram_data(self, parsed_data):
        word_count_dic = {}
        for i in range(len(parsed_data) - 1):
            data = ""
            for j in range(i, i + 3):
                data += parsed_data[j] + " "
            data = data[:-1]
            if "<End> <Start>" in data:
                continue
            elif data in word_count_dic:
                word_count_dic[data] += 1
            else:
                word_count_dic[data] = 1
        return word_count_dic

    def make_trigram_wordcloud(self, count):
        wordcloud = WordCloud(
            font_path = self.font_path,
            width = 800,
            height = 800,
            background_color = "white"
        )

        # temp_count = {}

        # for key in count.keys():
        #     if "<Start>" in key:
        #         temp_key = key.replace(" <Start>", "").replace("<Start> ", "")
        #         temp_count[temp_key] = count[key]
        #     elif "<End>" in key:
        #         temp_key = key.replace(" <End>", "").replace("<End> ", "")
        #         temp_count[temp_key] = count[key]
        #     else:
        #         temp_count[key] = count[key]

        # count = temp_count
        gen = wordcloud.generate_from_frequencies(count)
        array = gen.to_array()
        self.show_as_image(array)

    def show_as_image(self, data):
        import matplotlib.pyplot as plt
        plt.imshow(data, interpolation="bilinear")
        plt.axis("off")
        plt.show()

