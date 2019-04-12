import re
import time
import save_counts_wordcloud
import generate_sentence

class Ngram:
    def __init__(self, data):
        self.data = data
        self.unigram_count = {}
        self.bigram_count = {}
        self.trigram_count = {}
        
    def parse_and_count(self):
        sample_data = self.data
        sample_data = sample_data.replace("\n", " ").replace("\r", " ")
        sample_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sample_data)
        sample_data = sample_data.split()
        parsed_data = []

        for each in sample_data:
            if each != " ":
                parsed_data.append(each)
                
        for i, data in enumerate(parsed_data[:-2]):
            temp_unigram = data
            temp_bigram = data + " " + parsed_data[i + 1]
            temp_trigram = data + " " + parsed_data[i + 1] + " " + parsed_data[i + 2]
            
            if temp_unigram not in self.unigram_count:
                self.unigram_count[temp_unigram] = 1
            else:
                self.unigram_count[temp_unigram] += 1
            
            if temp_bigram not in self.bigram_count:
                self.bigram_count[temp_bigram] = 1
            else:
                self.bigram_count[temp_bigram] += 1
            
            if temp_trigram not in self.trigram_count:
                self.trigram_count[temp_trigram] = 1
            else:
                self.trigram_count[temp_trigram] += 1
        
        if parsed_data[-2] not in self.unigram_count:
            self.unigram_count[parsed_data[-2]] = 1
        else:
            self.unigram_count[parsed_data[-2]] += 1
        if parsed_data[-1] not in self.unigram_count:
            self.unigram_count[parsed_data[-1]] = 1
        else:
            self.unigram_count[parsed_data[-1]] += 1
            
        if parsed_data[-2] + " " + parsed_data[-1] not in self.bigram_count:
            self.bigram_count[parsed_data[-2] + " " + parsed_data[-1]] = 1
        else:
            self.bigram_count[parsed_data[-2] + " " + parsed_data[-1]] += 1
        return parsed_data
    
    def main(self):
        start = time.time()
        self.parse_and_count()
        save_counts_wordcloud.save_counts_wordcloud(self.unigram_count, self.bigram_count, self.trigram_count)
        print("parse, count, wordcloud time:", time.time() - start)
        del self.unigram_count
        del self.bigram_count
        del self.trigram_count
        start = time.time()
        generate_sentence.generate_sentence(self.data)
        print("Generate sentence time:", time.time() - start)
        

if __name__ == "__main__":
    f = open("../KCCq28.txt", 'r', encoding="utf-8")
    txt = f.read()
    f.close()
    ngram = Ngram(txt)
    ngram.main()
    del ngram
