import pytest
from get_keywords_of_text import extract_keywords
from SpanishTextAnalyzerLibrary import count_spanish_sentences

# Ejemplo de uso
text = """
La inteligencia artificial es capaz de analizar grandes volúmenes de datos y detectar patrones que serían difíciles de identificar para los humanos.
Los modelos de inteligencia artificial han mejorado la precisión en el diagnóstico médico, ayudando a identificar enfermedades como el cáncer en etapas tempranas.
El aprendizaje automático, una rama de la inteligencia artificial, permite que los sistemas se entrenen con datos y mejoren su rendimiento sin intervención humana directa.
A pesar de sus avances, la inteligencia artificial aún enfrenta desafíos éticos y técnicos, como el sesgo algorítmico y la seguridad en la toma de decisiones."""


def test_basic_text():
    """Check if keywords are extracted correctly."""
    text = "La inteligencia artificial es capaz de analizar grandes volúmenes de datos"
    keywords = extract_keywords(text)
    
    assert isinstance(keywords, list)  # Ensure output is a list
    assert all(isinstance(pair, tuple) for pair in keywords)  # Ensure all elements are tuples
    assert len(keywords) > 0  # Ensure at least one keyword is extracted

def test_empty_text():
    """Check behavior with empty input."""
    text = ""
    keywords = extract_keywords(text)
    assert keywords == []  # Should return an empty list

def test_stop_words_filtering():
    """Check if stop words removal affects output."""
    text = "la de que en una"
    keywords = extract_keywords(text)
    assert keywords == []  # Should return empty list since only stop words are present

def test_keyword_scoring():
    """Ensure keywords have valid scores."""
    keywords = extract_keywords(text,num_keywords=10,is_dupla=True)

    for keyword, score in keywords:
        assert isinstance(keyword, str)  # Check keyword type
        assert isinstance(score, float)  # Check score type
        assert 0.0 <= score <= 1.0  # Ensure score is within valid range


def test_count_spanish_sentences_basic():
    text = "Hola. ¿Cómo estás? Estoy muy bien. Gracias."
    assert count_spanish_sentences(text) is 4

def test_count_spanish_sentences_abbreviations():
    text = "El Dr. García vive en la Av. Siempreviva 123. Es un experto en EE.UU. Su número es 123.456. Estudió en la U.N.A.C."
    assert count_spanish_sentences(text) is 4

def test_count_spanish_sentences_multiple_dots():
    text = "¡Qué alegría! Te lo dije... ¿Me escuchaste?? No lo sé."
    # For some reason this also could be 4 sentences
    assert count_spanish_sentences(text) is 3

def test_count_spanish_sentences_with_blank_lines():
    texto_ejemplo_1 = """
        Esta es la primera oración.
    
        Esta es la segunda. ¿Lo ves?    Sí.
    
        Y esta la última.
        """
    texto_hoja_demo = """
        La IA ofrece numerosas oportunidades y beneficios en la educación universitaria, tales
        como la personalización del aprendizaje, la mejora de la retroalimentación, el ahorro de
        tiempo, los recursos y herramientas educativas, entre otros. Sin embargo, también existen
        preocupaciones sobre la posible pérdida de empleos docentes, la falta de interacción humana
        y la privacidad de los datos de los estudiantes. La IA también plantea amenazas importantes,
        una de las principales preocupaciones es la pérdida de empleos debido a la automatización
        (Muñoz Arango; Márquez Villegas, 2023). Por lo tanto, es necesario analizar de manera crítica
        el impacto de la IA en el aprendizaje de los estudiantes universitarios y abordar los retos y
        cuestionamientos que surgen con su implementación.
        """
    assert count_spanish_sentences(texto_ejemplo_1) is 5
    assert count_spanish_sentences(texto_hoja_demo) is 4

def test_count_spanish_sentences_empty():
    texto_ejemplo_1 = ""
    assert count_spanish_sentences(texto_ejemplo_1) is 0
