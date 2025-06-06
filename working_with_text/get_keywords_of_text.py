from keybert import KeyBERT
import nltk
from nltk.corpus import stopwords

# revisar Descargar stopwords en español (solo la primera vez)
nltk.download("stopwords")
def remove_stopwords(text):
    """ Remove spanish stopwords from text"""
    stop_words = set(stopwords.words("spanish"))

    filter_words = [word for word in text.split() if word.lower() not in stop_words]
    return " ".join(filter_words)

def extract_keywords(text, num_keywords=10, is_dupla=False, resaltar_palabras=False):
    """
    Get keywords from a spanish text use KeyBERT.
    
    Args:
    - text (str): text to find keywords.
    - num_keywords (int): number of words to extract.
    - is_dupla(bool): if True return a tupla of keywords else a single keyword
    
    Returns:
    - list: List of tuples with keyword and score of relevance.
    """
    basic_stopwords_sp = ["un", "una", "el", "la", "que", "de", "en"]

    kw_model = KeyBERT()

    if is_dupla:
        return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words=basic_stopwords_sp, top_n=num_keywords, highlight=resaltar_palabras)
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words=basic_stopwords_sp, top_n=num_keywords, highlight=resaltar_palabras)
