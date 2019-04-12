import generate_sentence_bigram
import generate_sentence_trigram
from multiprocessing import Process


def generate_sentence(data):
    p1 = Process(target=generate_sentence_bigram.generate_sentence_bigram, args=(data))
    p2 = Process(target=generate_sentence_trigram.generate_sentence_trigram, args=data))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    # generate_sentence_bigram.generate_sentence_bigram(data)
    # generate_sentence_trigram.generate_sentence_trigram(data)