import nltk
from nltk.corpus import stopwords

# revisar Descargar stopwords en español (solo la primera vez)
nltk.download("stopwords")
def remove_stopwords(text):
    """ Remove spanish stopwords from text"""
    stop_words = set(stopwords.words("spanish"))

    filter_words = [word for word in text.split() if word.lower() not in stop_words]
    return " ".join(filter_words)

def remove_new_line(text):
    new_text = []
    for line in text.splitlines():
        if line[-1] == '.':
            sentence = line + "\n"
            new_text.append(sentence)
        else:
            new_text.append(line)
    return " ".join(new_text)
