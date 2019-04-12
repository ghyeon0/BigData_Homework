import re


def parse_data_bigram(data):
    sample_data = "<Start> " + data + " <End>"
    sample_data = sample_data.replace("\n", " ").replace("\r", " ")
    sample_data = sample_data.replace(".", ". <End> <Start> ").replace("!", "! <End> <Start> ").replace("?", "? <End> <Start> ")
    sample_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sample_data)
    sample_data = sample_data.split()
    parsed_data = []

    for each in sample_data:
        if each != " ":
            parsed_data.append(each)

    return parsed_data


def parse_data_trigram(data):
    sample_data = "<Start> <Start> " + data + " <End>"
    sample_data = sample_data.replace("\n", " ").replace("\r", " ")
    sample_data = sample_data.replace(".", ". <End> <Start> <Start> ").replace("!", "! <End> <Start> <Start> ").replace("?", "? <End> <Start> <Start> ")
    sample_data = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sample_data)
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


def count_and_calc_probability_trigram(parsed_data):
    count_dic = {}
    probability_dic = {}

    for i, data in enumerate(parsed_data[:-2]):
        temp_data = data + parsed_data[i + 1]
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
            print(master_key, slave_key, probability_dic[master_key][slave_key])

    return count_dic, probability_dic


def generate_sentence_bigram(data):
    parsed_bigram_data = parse_data_bigram(data)
    bigram_count, probability_dic = count_and_calc_probability_bigram(parsed_bigram_data)


def generate_sentence_trigram(data):
    parsed_trigram_data = parse_data_trigram(data)
    trigram_count, probability_dic = count_and_calc_probability_trigram(parsed_trigram_data)


def generate_sentence(data):
    generate_sentence_bigram(data)
    generate_sentence_trigram(data)