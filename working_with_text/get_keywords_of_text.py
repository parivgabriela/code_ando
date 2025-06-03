from keybert import KeyBERT

def extraer_palabras_clave(texto, num_keywords=10, is_dupla=False):
    """
    Extrae las palabras clave de un texto en español utilizando KeyBERT.
    
    Args:
    - texto (str): El texto del cual extraer las palabras clave.
    - num_keywords (int): Número de palabras clave a extraer.
    
    Returns:
    - list: Lista de tuplas con las palabras clave y su puntuación de relevancia.
    """
    kw_model = KeyBERT()

    if is_dupla:
        return kw_model.extract_keywords(texto, keyphrase_ngram_range=(1, 2), stop_words=None)
    return kw_model.extract_keywords(texto, top_n=num_keywords)

# Ejemplo de uso
texto = """
La inteligencia artificial es un campo de estudio que busca crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. 
Estas tareas incluyen el reconocimiento de voz, la toma de decisiones, la traducción de idiomas y la percepción visual. 
La inteligencia artificial se basa en algoritmos y modelos matemáticos que permiten a las máquinas aprender de los datos y mejorar su rendimiento con el tiempo.
"""

keywords = extraer_palabras_clave(texto)
print("Palabras clave extraídas:")
for palabra, puntuacion in keywords:
    print(f"{palabra}: {puntuacion}")
