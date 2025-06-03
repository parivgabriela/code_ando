from transformers import pipeline
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def resumir_texto_lsa(texto, num_oraciones=5):
    """
    Resume un texto en español utilizando el método LSA.

    Parámetros:
    - texto (str): Texto a resumir.
    - num_oraciones (int): Número de oraciones en el resumen.

    Retorna:
    - str: Texto resumido.
    """
    parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
    summarizer = LsaSummarizer()
    resumen = summarizer(parser.document, num_oraciones)

    return " ".join(str(oracion) for oracion in resumen)

def adaptar_longitud_resumen(texto):
    """
    Ajusta la longitud del resumen según el tamaño del texto original.
    
    Parámetros:
    - texto (str): Texto de entrada.

    Retorna:
    - max_length (int), min_length (int): Parámetros adecuados para la longitud del resumen.
    """
    num_palabras = len(texto.split())

    if num_palabras <= 150:  # Textos cortos
        return 50, 20  # Resumen breve pero útil
    elif 150 < num_palabras <= 500:  # Textos medianos
        return 100, 40
    elif 500 < num_palabras <= 1000:  # Textos largos
        return 200, 80
    else:  # Textos muy extensos
        return 250, 100  # Se recomienda dividir el texto en segmentos

def resumir_texto_ai(texto, max_input_words=800):
    """
    Resume un texto en español utilizando modelos de IA como T5 o BART.

    Parámetros:
    - texto (str): Texto a resumir.
    - max_input_words (int): Límite de palabras de entrada.

    Retorna:
    - str: Resumen generado por IA.
    """
    modelo_resumidor = pipeline("summarization", model="facebook/bart-large-cnn")
    cant_palabras_input = len(texto)
    # Limitar el tamaño del texto de entrada
    palabras = texto.split()[:max_input_words]
    texto_recortado = " ".join(palabras)

    # Ajustar longitud de resumen
    max_length, min_length = adaptar_longitud_resumen(texto)

    resumen = modelo_resumidor(texto, max_length=max_length, min_length=min_length, do_sample=False)

    return resumen[0]['summary_text']

# **Ejemplo de uso**
texto = """
La inteligencia artificial es un campo de estudio que busca crear sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. 
Estas tareas incluyen el reconocimiento de voz, la toma de decisiones, la traducción de idiomas y la percepción visual. 
La inteligencia artificial se basa en algoritmos y modelos matemáticos que permiten a las máquinas aprender de los datos y mejorar su rendimiento con el tiempo.
"""

# resumir summy lsa
resumen = resumir_texto_lsa(texto, num_oraciones=3)
print(resumen)

# usando pipeline
resumen = resumir_texto_ai(texto, max_input_words=100)
print(resumen)
