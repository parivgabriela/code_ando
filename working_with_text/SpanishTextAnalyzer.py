import re
import math
from typing import Dict, Union
from pathlib import Path
from SpanishTextAnalyzerLibrary import count_spanish_sentences

class SpanishTextAnalyzer:
    """
    Analizador de texto en español para calcular tokens y estadísticas
    """
    
    def __init__(self):
        # Factores de conversión aproximados para español
        self.CHARS_PER_TOKEN_ES = 4.5  # Promedio para español (más alto que inglés)
        self.WORDS_PER_TOKEN_ES = 0.75  # Español tiene palabras más largas
        self.CHARS_PER_PAGE = 2000     # Caracteres por página estándar
        self.WORDS_PER_PAGE = 400      # Palabras por página estándar
        
        # Patrones específicos del español
        self.spanish_patterns = {
            'contractions': r"\b(del|al|conmigo|contigo|consigo)\b",
            'compound_words': r"\b\w+[-]\w+\b",
            'special_chars': r"[ñáéíóúü¿¡]",
            'punctuation': r"[.,;:!¡?¿()\"'\-\[\]{}]"
        }
    
    def count_tokens_by_characters(self, text: str) -> int:
        """
        Estima tokens basado en conteo de caracteres (método más simple)
        """
        # Limpiar texto pero conservar espacios significativos
        clean_text = re.sub(r'\s+', ' ', text.strip())
        char_count = len(clean_text)
        
        # Ajuste para español - caracteres especiales cuentan más
        spanish_chars = len(re.findall(self.spanish_patterns['special_chars'], text, re.IGNORECASE))
        adjusted_chars = char_count + (spanish_chars * 0.2)  # Ligero ajuste
        
        return max(1, math.ceil(adjusted_chars / self.CHARS_PER_TOKEN_ES))
    
    def count_tokens_by_words(self, text: str) -> int:
        """
        Estima tokens basado en conteo de palabras (más preciso para español)
        """
        # Tokenizar palabras considerando patrones españoles
        words = re.findall(r'\b[a-záéíóúüñ]+\b', text.lower())
        
        # Contar contracciones y palabras compuestas
        contractions = len(re.findall(self.spanish_patterns['contractions'], text, re.IGNORECASE))
        compound_words = len(re.findall(self.spanish_patterns['compound_words'], text))
        
        # Palabras base
        base_words = len(words)
        
        # Ajuste para características del español
        total_word_units = base_words + (contractions * 0.5) + compound_words
        
        return max(1, math.ceil(total_word_units / self.WORDS_PER_TOKEN_ES))
    
    def count_tokens_advanced(self, text: str) -> int:
        """
        Método avanzado que combina múltiples heurísticas para español
        """
        # Limpieza inicial
        clean_text = text.strip()
        
        if not clean_text:
            return 0
        
        # Múltiples estimaciones
        char_tokens = self.count_tokens_by_characters(clean_text)
        word_tokens = self.count_tokens_by_words(clean_text)
        
        # Factores de ajuste para español
        punctuation_count = len(re.findall(self.spanish_patterns['punctuation'], text))
        punctuation_tokens = math.ceil(punctuation_count / 4)  # Puntuación también cuenta
        
        # Promedio ponderado favoreciendo el método de palabras para español
        estimated_tokens = math.ceil(
            (word_tokens * 0.7) + 
            (char_tokens * 0.3) + 
            punctuation_tokens
        )
        
        return max(1, estimated_tokens)
    
    def analyze_text_content(self, text: str) -> Dict:
        """
        Analiza el contenido de un texto y devuelve estadísticas completas
        """
        if not text:
            return self._empty_stats()
        
        # Estadísticas básicas
        char_count = len(text)
        char_count_no_spaces = len(re.sub(r'\s', '', text))
        
        # Conteo de palabras (método mejorado para español)
        words = re.findall(r'\b[a-záéíóúüñ]+\b', text, re.IGNORECASE)
        word_count = len(words)
        
        # Conteo de oraciones
        sentences = count_spanish_sentences(text)
        sentence_count = len([s for s in sentences if s.strip()])
        
        # Conteo de párrafos
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)
        
        # Estimación de páginas
        pages_by_chars = math.ceil(char_count / self.CHARS_PER_PAGE)
        pages_by_words = math.ceil(word_count / self.WORDS_PER_PAGE)
        estimated_pages = max(pages_by_chars, pages_by_words)
        
        # Cálculo de tokens con diferentes métodos
        tokens_simple = self.count_tokens_by_characters(text)
        tokens_word_based = self.count_tokens_by_words(text)
        tokens_advanced = self.count_tokens_advanced(text)
        
        # Estadísticas adicionales
        avg_word_length = sum(len(word) for word in words) / len(words) if words else 0
        avg_sentence_length = word_count / sentence_count if sentence_count > 0 else 0
        
        return {
            'characters': char_count,
            'characters_no_spaces': char_count_no_spaces,
            'words': word_count,
            'sentences': sentence_count,
            'paragraphs': paragraph_count,
            'estimated_pages': estimated_pages,
            'tokens': {
                'simple_estimate': tokens_simple,
                'word_based_estimate': tokens_word_based,
                'advanced_estimate': tokens_advanced,
                'recommended': tokens_advanced  # El más preciso para español
            },
            'ratios': {
                'chars_per_token': round(char_count / tokens_advanced, 2) if tokens_advanced > 0 else 0,
                'words_per_token': round(word_count / tokens_advanced, 2) if tokens_advanced > 0 else 0,
                'tokens_per_page': round(tokens_advanced / estimated_pages, 2) if estimated_pages > 0 else 0
            },
            'language_stats': {
                'avg_word_length': round(avg_word_length, 2),
                'avg_sentence_length': round(avg_sentence_length, 2),
                'spanish_chars': len(re.findall(r'[ñáéíóúü¿¡]', text, re.IGNORECASE))
            }
        }
    
    def analyze_file(self, file_path: Union[str, Path]) -> Dict:
        """
        Analiza un archivo de texto y devuelve estadísticas completas
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"El archivo {file_path} no existe")
        
        if not file_path.is_file():
            raise ValueError(f"{file_path} no es un archivo")
        
        # Información del archivo
        file_info = {
            'file_path': str(file_path.absolute()),
            'file_name': file_path.name,
            'file_size_bytes': file_path.stat().st_size,
            'file_extension': file_path.suffix
        }
        
        # Leer archivo con encoding apropiado
        try:
            encodings = ['utf-8', 'latin-1', 'cp1252']
            text_content = None
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        text_content = file.read()
                    break
                except UnicodeDecodeError:
                    continue
            
            if text_content is None:
                raise ValueError("No se pudo leer el archivo con ninguna codificación")
            
        except Exception as e:
            raise ValueError(f"Error al leer el archivo: {str(e)}")
        
        # Analizar contenido
        content_stats = self.analyze_text_content(text_content)
        
        # Combinar información
        result = {**file_info, **content_stats}
        
        # Agregar métricas específicas del archivo
        result['file_metrics'] = {
            'kb_size': round(file_info['file_size_bytes'] / 1024, 2),
            'compression_ratio': round(content_stats['characters'] / file_info['file_size_bytes'], 2) if file_info['file_size_bytes'] > 0 else 0
        }
        
        return result
    
    def _empty_stats(self) -> Dict:
        """Devuelve estadísticas vacías"""
        return {
            'characters': 0, 'characters_no_spaces': 0, 'words': 0,
            'sentences': 0, 'paragraphs': 0, 'estimated_pages': 0,
            'tokens': {'simple_estimate': 0, 'word_based_estimate': 0, 
                      'advanced_estimate': 0, 'recommended': 0},
            'ratios': {'chars_per_token': 0, 'words_per_token': 0, 'tokens_per_page': 0},
            'language_stats': {'avg_word_length': 0, 'avg_sentence_length': 0, 'spanish_chars': 0}
        }

# Funciones de conveniencia
def analyze_spanish_text(text: str) -> Dict:
    """
    Función simple para analizar texto español
    
    Args:
        text: Texto en español a analizar
    
    Returns:
        Diccionario con estadísticas completas del texto
    """
    analyzer = SpanishTextAnalyzer()
    return analyzer.analyze_text_content(text)

def analyze_text_file(file_path: str) -> Dict:
    """
    Función simple para analizar archivo de texto
    
    Args:
        file_path: Ruta al archivo de texto
    
    Returns:
        Diccionario con estadísticas completas del archivo
    """
    analyzer = SpanishTextAnalyzer()
    return analyzer.analyze_file(file_path)

def get_token_count(text: str) -> int:
    """
    Función rápida para obtener solo el conteo de tokens
    
    Args:
        text: Texto en español
    
    Returns:
        Número estimado de tokens
    """
    analyzer = SpanishTextAnalyzer()
    return analyzer.count_tokens_advanced(text)

def print_analysis_report(stats: Dict, include_file_info: bool = True):
    """
    Imprime un reporte formateado de las estadísticas
    """
    print("=" * 60)
    print("ANÁLISIS DE TEXTO EN ESPAÑOL")
    print("=" * 60)
    
    if include_file_info and 'file_name' in stats:
        print(f"\n📁 INFORMACIÓN DEL ARCHIVO:")
        print(f"   Nombre: {stats['file_name']}")
        print(f"   Tamaño: {stats['file_metrics']['kb_size']} KB")
        print(f"   Ruta: {stats['file_path']}")
    
    print(f"\n📊 ESTADÍSTICAS BÁSICAS:")
    print(f"   Caracteres: {stats['characters']:,}")
    print(f"   Caracteres (sin espacios): {stats['characters_no_spaces']:,}")
    print(f"   Palabras: {stats['words']:,}")
    print(f"   Oraciones: {stats['sentences']:,}")
    print(f"   Párrafos: {stats['paragraphs']:,}")
    print(f"   Páginas estimadas: {stats['estimated_pages']:,}")
    
    print(f"\n🔢 ESTIMACIÓN DE TOKENS:")
    print(f"   Método simple: {stats['tokens']['simple_estimate']:,}")
    print(f"   Método por palabras: {stats['tokens']['word_based_estimate']:,}")
    print(f"   Método avanzado: {stats['tokens']['advanced_estimate']:,}")
    print(f"   → RECOMENDADO: {stats['tokens']['recommended']:,} tokens")
    
    print(f"\n📐 PROPORCIONES:")
    print(f"   Caracteres por token: {stats['ratios']['chars_per_token']}")
    print(f"   Palabras por token: {stats['ratios']['words_per_token']}")
    print(f"   Tokens por página: {stats['ratios']['tokens_per_page']}")
    
    print(f"\n🇪🇸 CARACTERÍSTICAS DEL ESPAÑOL:")
    print(f"   Longitud promedio de palabra: {stats['language_stats']['avg_word_length']}")
    print(f"   Palabras promedio por oración: {stats['language_stats']['avg_sentence_length']}")
    print(f"   Caracteres especiales del español: {stats['language_stats']['spanish_chars']}")
    
    print("=" * 60)

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con texto directo
    sample_text = """
    La inteligencia artificial está transformando el mundo de manera acelerada. 
    Esta revolución tecnológica presenta tanto oportunidades extraordinarias como 
    desafíos únicos para la humanidad. Los algoritmos de aprendizaje automático 
    pueden procesar información a velocidades impresionantes, pero también plantean 
    preguntas importantes sobre ética y responsabilidad.
    
    En España, las universidades están incorporando estas tecnologías en sus 
    programas académicos. Los estudiantes necesitan comprender no solo cómo 
    funcionan estas herramientas, sino también sus implicaciones sociales y éticas.
    """
    texto2 = """como calculo cuantos tokens tiene un texto en español? Genera una funcion para reutilizar el codigo dado un input, la ruta del archivo txt me diga cantidad de paginas, cantidad de palabras, cantidad de caracteres y tokens"""
    texto_3 = """cual es el error AttributeError: module 'posixpath' has no attribute 'spbasedlitext' codigo output_path = os.path.spbasedlitext(filename)[0] + ".txt"""
    texto_4 = """Como estimo el gasto de un instituto que va a usar api de un modelo ia siendo que sale $5 input por millon de tokens y $10 output 1- como poner un limite para los usuarios. Lo recomendado 2- El usuario puede enviar archivos para el procesamiento maximo 10 paginas."""
    
    print("Ejemplo 1: Análisis de texto directo")
    stats = analyze_spanish_text(texto_4)
    print_analysis_report(stats, include_file_info=False)
    
    print("\n" + "="*60 + "\n")
    
    # Ejemplo con archivo (descomenta si tienes un archivo)
    # print("Ejemplo 2: Análisis de archivo")
    # try:
    #     path_files = "../archivos_prueba/"
    #     filename = "hoja-demo.txt"
    #     file_stats = analyze_text_file(path_files + filename)
    #     print_analysis_report(file_stats)
    # except FileNotFoundError:
    #     print("Archivo 'mi_documento.txt' no encontrado")
    
    # Función rápida para obtener solo tokens
    print("Función rápida - Solo tokens:")
    token_count = get_token_count(sample_text)
    print(f"Tokens estimados: {token_count}")