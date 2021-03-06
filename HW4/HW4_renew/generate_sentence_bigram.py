import re
from operator import itemgetter
import random


def parse_data_bigram(data):
    sample_data = "<Start> " + data + " <End>"
    sample_data = sample_data.replace("\n", " ").replace("\r", " ")
    sample_data = sample_data.replace(".", " <End> <Start> ").replace("!", " <End> <Start> ").replace("?", " <End> <Start> ")
    sample_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]`\'…》]', '', sample_data)
    sample_data = sample_data.split()
    parsed_data = []

    for each in sample_data:
        if each != " ":
            parsed_data.append(each)

    return parsed_data


def count_and_calc_probability_bigram(parsed_data):
    count_dic = {}
    probability_dic = {}

    for i, data in enumerate(parsed_data[:-1]):
        if data not in count_dic:
            count_dic[data] = 1
            probability_dic[data] = {parsed_data[i + 1]: 1}
        else:
            count_dic[data] += 1
            if parsed_data[i + 1] not in probability_dic[data]:
                probability_dic[data][parsed_data[i + 1]] = 1
            else:
                probability_dic[data][parsed_data[i + 1]] += 1

    for master_key in count_dic.keys():
        for slave_key in probability_dic[master_key].keys():
            probability_dic[master_key][slave_key] = probability_dic[master_key][slave_key] / count_dic[master_key]

    return count_dic, probability_dic


def calc_sentence_generation_probability_bigram(sentence, probability_dic):
    # print(sentence)
    sentence = "<Start> " + sentence + " <End>"
    sentence = sentence.split()
    total_probability = 1
    for i in range(len(sentence) - 1):
        # print(sentence[i], sentence[i + 1])
        total_probability *= probability_dic[sentence[i]][sentence[i + 1]]
    # print(total_probability)
    return total_probability


def generate_sentence_bigram(data, candidate_size=10):
    parsed_bigram_data = parse_data_bigram(data)
    print("Bigram Data Parsing Complete")
    bigram_count, probability_dic = count_and_calc_probability_bigram(parsed_bigram_data)
    print("Bigram Probability Calculation Complete")
    start_tokens = sorted(probability_dic["<Start>"].items(), key=itemgetter(1), reverse=True)[:3]
    f = open("./Bigram/sentence.txt", 'w', encoding="utf-8")
    for start_token in start_tokens:
        f.write("Seed: " + start_token[0] + "\n")
        sentences = []
        for _ in range(10):
            current_token = start_token[0]
            sentence = start_token[0] + " "
            while current_token != "<End>":
                raw_candidate = sorted(probability_dic[current_token].items(), reverse=True, key=itemgetter(1))[:candidate_size]
                candidate = []
                for each in raw_candidate:
                    candidate.append(each[0])
                if "<End>" in candidate[:3]:
                    token = "<End>"
                else:
                    token = candidate[random.randint(0, min(candidate_size - 1, len(candidate) - 1))]
                # print(token)
                sentence += token + " "
                current_token = token
            sentences.append((sentence[:-7], calc_sentence_generation_probability_bigram(sentence[:-7], probability_dic)))
        sentences.sort(key=itemgetter(1), reverse=True)
        for i, each in enumerate(sentences):
            f.write(str(i + 1) + ": " + each[0] + "\n\n")
        f.write("\n\n")
    f.close()