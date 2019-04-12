from wordcloud import WordCloud
from PIL import Image

def make_ngram_wordcloud(count, target, filename):
    wordcloud = WordCloud(
    font_path = '../d2coding.ttf',
        width = 800,
        height = 800,
        background_color = "white"
    )
    gen = wordcloud.generate_from_frequencies(count)
    array = gen.to_array()
    save_as_image(array, target, filename)

def save_as_image(data, target, filename):
    im = Image.fromarray(data)
    im.save("./" + target + "/" + filename + ".jpg")