import re
from operator import itemgetter
import random


def parse_data_trigram(data):
    sample_data = "<Start> <Start> " + data + " <End>"
    sample_data = sample_data.replace("\n", " ").replace("\r", " ")
    sample_data = sample_data.replace(".", "<End> <Start> <Start> ").replace("!", "<End> <Start> <Start> ").replace("?", "<End> <Start> <Start> ")
    sample_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]`\'…》]', '', sample_data)
    sample_data = sample_data.split()
    parsed_data = []

    for each in sample_data:
        if each != " ":
            parsed_data.append(each)

    return parsed_data


def calc_sentence_generation_probability_bigram(sentence, probability_dic):
    # print(sentence)
    sentence = "<Start> <Start> " + sentence + " <End>"
    sentence = sentence.split()
    total_probability = 1
    for i in range(len(sentence) - 2):
        temp_data = sentence[i] + " " + sentence[i + 1]
        next_data = sentence[i + 2]
        print(temp_data, next_data)
        total_probability *= probability_dic[temp_data][next_data]
    # print(total_probability)
    return total_probability


def count_and_calc_probability_trigram(parsed_data):
    count_dic = {}
    probability_dic = {}

    for i, data in enumerate(parsed_data[:-2]):
        temp_data = data + " " + parsed_data[i + 1]
        next_data = parsed_data[i + 2]
        if temp_data not in count_dic:
            count_dic[temp_data] = 1
            probability_dic[temp_data] = {next_data: 1}
        else:
            count_dic[temp_data] += 1
            if next_data not in probability_dic[temp_data]:
                probability_dic[temp_data][next_data] = 1
            else:
                probability_dic[temp_data][next_data] += 1
    
    for master_key in count_dic.keys():
        for slave_key in probability_dic[master_key].keys():
            probability_dic[master_key][slave_key] = probability_dic[master_key][slave_key] / count_dic[master_key]
            # print(master_key, slave_key, probability_dic[master_key][slave_key])

    return count_dic, probability_dic
            

def generate_sentence_trigram(data, candidate_size=10):
    parsed_trigram_data = parse_data_trigram(data)
    print("Trigram Data Parsing Complete")
    trigram_count, probability_dic = count_and_calc_probability_trigram(parsed_trigram_data)
    print("Trigram Probability Calculation Complete")
    start_tokens = sorted(probability_dic["<Start> <Start>"].items(), key=itemgetter(1), reverse=True)[:3]
    f = open("./Trigram/sentence.txt", 'w', encoding="utf-8")
    for start_token in start_tokens:
        f.write("Seed: " + start_token[0] + "\n")
        sentences = []
        for _ in range(10):
            current_token = "<Start> " + start_token[0]
            sentence = current_token + " "
            while "<End>" not in current_token:
                print(current_token)
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
                current_token = current_token.split()[1] + " " + token
            sentence = sentence[8:]
            sentence = sentence[:-6]
            print(sentence)
            sentences.append((sentence, calc_sentence_generation_probability_bigram(sentence, probability_dic)))
        sentences.sort(key=itemgetter(1), reverse=True)
        for each in sentences:
            f.write(each[0] + "\n")
        f.write("\n")
    f.close()