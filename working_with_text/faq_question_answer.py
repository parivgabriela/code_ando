import re
import json
import unicodedata
from os import path

FAQ_FILE = "faq.json"

def estandarizar_pregunta(pregunta: str) -> str:
    """Normaliza una pregunta para usarla como clave."""
    texto = pregunta.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'[^a-z0-9\s]', '', texto) # elimina los signos de puntuación
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def cargar_faq() -> dict:
    """Carga la base de datos de FAQ desde un archivo JSON."""
    if path.exists(FAQ_FILE):
        with open(FAQ_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def obtener_respuesta_faq(pregunta_usuario: str, faq_db: dict):
    """Busca una pregunta en la base de FAQ."""
    pregunta_estandarizada = estandarizar_pregunta(pregunta_usuario)
    return faq_db.get(pregunta_estandarizada)

def guardar_nueva_faq(pregunta_usuario: str, respuesta_generada: str, faq_db: dict):
    """
    Estandariza una nueva pregunta, la añade a la base de FAQ
    y guarda el archivo JSON actualizado.
    """
    pregunta_estandarizada = estandarizar_pregunta(pregunta_usuario)
    
    # Añade o actualiza la pregunta en el diccionario
    faq_db[pregunta_estandarizada] = respuesta_generada
    
    # Escribe el diccionario completo de vuelta al archivo JSON
    with open(FAQ_FILE, 'w', encoding='utf-8') as f:
        # indent=4 para que el JSON sea legible
        # ensure_ascii=False para guardar tildes y caracteres en español correctamente
        json.dump(faq_db, f, ensure_ascii=False, indent=4)
    
    print(f"✅ Pregunta nueva guardada en '{FAQ_FILE}'")


if __name__ == "__main__":

    faq_database = cargar_faq()

    print("\n" + "="*40 + "\n" + "--- FAQ ---" + "\n" + "="*40 + "\n")
    print("Para salir ingrese 0")

    pregunta_nueva = input("Ingrese una pregunta: ")

    while not pregunta_nueva == "0":

        respuesta = obtener_respuesta_faq(pregunta_nueva, faq_database)

        if respuesta:
            print(f"Respuesta de FAQ: {respuesta}")
        else:
            print("Respuesta no encontrada en FAQ. Generando una nueva...")

            # respuesta_rag = query(pregunta_nueva) llamar al sistema RAG (ChromaDB + LLM)
            #print(f"Respuesta generada por RAG: {respuesta_rag}")
            #guardar_nueva_faq(pregunta_nueva, respuesta_rag, faq_database)

        print("\n" + "="*40 + "\n")
        print("Para salir ingrese 0")

        pregunta_nueva = input("Ingrese una pregunta: ")
