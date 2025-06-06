import nltk
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')

def count_spanish_sentences(text: str) -> int:
    """
    Count spanish sentences using NLTK.

    Args:
        text (str): text to analize.

    Returns:
        int: number of sentences.
    """
    if not text or not isinstance(text, str):
        return 0

    texto_limpio = ' '.join(text.split())

    oraciones = nltk.sent_tokenize(texto_limpio, language='spanish') # -> List

    # Filtramos oraciones que puedan ser solo espacios o muy cortas después de la tokenización
    # (Aunque sent_tokenize es bastante robusto, es una buena práctica defensiva)
    oraciones_validas = [oracion.strip() for oracion in oraciones if oracion.strip()]

    return len(oraciones_validas)
