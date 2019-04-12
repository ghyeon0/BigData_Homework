from operator import itemgetter
import draw_wordcloud

def save_counts_wordcloud(unigram_data, bigram_data, trigram_data):
    unigram = save_unigram_count(unigram_data)
    bigram = save_bigram_count(bigram_data)
    trigram = save_trigram_count(trigram_data)
    draw_wordclouds(unigram, bigram, trigram)

def save_unigram_count(unigram_count):
    sorted_unigram_count = sorted(unigram_count.items(), key=itemgetter(1), reverse=True)
    
    total_length = len(sorted_unigram_count)
    upper_ten = 0
    upper_three = 0

    for key in unigram_count.keys():
        if unigram_count[key] >= 10:
            upper_ten += 1
        if unigram_count[key] >= 3:
            upper_three += 1
    f = open("./Unigram/unigram_frequency.txt", 'w', encoding="utf-8")
    f.write("총 Unigram 수: " + str(total_length) + "\n")
    f.write("빈도가 10 이상인 Unigram 수: " + str(upper_ten) + "\n")
    f.write("빈도가 3 이상인 Unigram 수: " + str(upper_three) + "\n")
    for each in sorted_unigram_count[:1000]:
        f.write(str(each) + "\n")
    f.close()
    return sorted_unigram_count

def save_bigram_count(bigram_count):
    sorted_bigram_count = sorted(bigram_count.items(), key=itemgetter(1), reverse=True)

    total_length = len(sorted_bigram_count)
    upper_ten = 0
    upper_three = 0

    for key in bigram_count.keys():
        if bigram_count[key] >= 10:
            upper_ten += 1
        if bigram_count[key] >= 3:
            upper_three += 1
    f = open("./Bigram/bigram_frequency.txt", 'w', encoding="utf-8")
    f.write("총 Bigram 수: " + str(total_length) + "\n")
    f.write("빈도가 10 이상인 Bigram 수: " + str(upper_ten) + "\n")
    f.write("빈도가 3 이상인 Bigram 수: " + str(upper_three) + "\n")
    for each in sorted_bigram_count[:1000]:
        f.write(str(each) + "\n")
    f.close()
    return sorted_bigram_count

def save_trigram_count(trigram_count):
    sorted_trigram_count = sorted(trigram_count.items(), key=itemgetter(1), reverse=True)

    total_length = len(sorted_trigram_count)
    upper_ten = 0
    upper_three = 0

    for key in trigram_count.keys():
        if trigram_count[key] >= 10:
            upper_ten += 1
        if trigram_count[key] >= 3:
            upper_three += 1
    f = open("./Trigram/trigram_frequency.txt", 'w', encoding="utf-8")
    f.write("총 Trigram 수: " + str(total_length) + "\n")
    f.write("빈도가 10 이상인 Trigram 수: " + str(upper_ten) + "\n")
    f.write("빈도가 3 이상인 Trigram 수: " + str(upper_three) + "\n")
    for each in sorted_trigram_count[:1000]:
        f.write(str(each) + "\n")
    f.close()
    return sorted_trigram_count

def draw_wordclouds(unigram_data, bigram_data, trigram_data):
    draw_wordcloud_bigram(unigram_data, bigram_data)
    draw_wordcloud_trigram(unigram_data, trigram_data)
    
def draw_wordcloud_bigram(unigram_data, bigram_data):
    keys = [unigram_data[0][0], unigram_data[1][0], unigram_data[2][0]]
    for key in keys:
        lst = []
        for each in bigram_data:
            k = each[0].split()[0]
            if k == key:
                lst.append(each)
        lst.sort(key=itemgetter(1), reverse=True)
        lst = lst[:20]
        dic = {}
        for each in lst:
            dic[each[0].split()[1]] = int(each[1])
        draw_wordcloud.make_ngram_wordcloud(dic, "Bigram", key)
     
def draw_wordcloud_trigram(unigram_data, trigram_data):
    keys = [unigram_data[0][0], unigram_data[1][0], unigram_data[2][0]]
    for key in keys:
        lst = []
        for each in trigram_data:
            k = each[0].split()[0]
            if k == key:
                lst.append(each)
        lst.sort(key=itemgetter(1), reverse=True)
        lst = lst[:20]
        dic = {}
        for each in lst:
            temp_key = each[0].split()
            temp_key = temp_key[1] + "_" + temp_key[2]
            dic[temp_key] = int(each[1])
        draw_wordcloud.make_ngram_wordcloud(dic, "Trigram", key)

