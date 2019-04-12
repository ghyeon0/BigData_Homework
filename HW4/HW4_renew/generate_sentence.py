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

def generate_sentence_bigram(data):
    parsed_bigram_data = parse_data_bigram(data)


def generate_sentence_trigram(data):
    parsed_trigram_data = parse_data_trigram(data)


def generate_sentence(data):
    generate_sentence_bigram(data)
    generate_sentence_trigram(data)