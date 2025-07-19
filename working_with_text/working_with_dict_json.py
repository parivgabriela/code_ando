import json
from collections import defaultdict

def generate_report_by_category(path_json_file, key_dict):
    """
    Read and return a report of hoy many elemenst are by the key_dict
    Parameters:
        path_json_file (str): Path to file .json

    Return:
        dict: Dict with the count for each key
    """
    with open(path_json_file, 'r', encoding='utf-8') as f:
        datos = json.load(f)

    conteo = defaultdict(int)

    for elemento in datos:
        categoria = elemento.get(key_dict)
        if categoria is not None:
            conteo[categoria] += 1

    return dict(conteo)

def add_attribute_dict_to_all_file(path_json_file: str, path_output_file: str, name_attribute: str, value_attribute):
    """
    Add name_Attribute to each dict element, set the default value to .

    Args:
        path_json_file (str): path to the file.
        path_output_file (str): path to save the new file.
    """
    try:
        with open(path_json_file, 'r', encoding='utf-8') as f_entrada:
            datos = json.load(f_entrada)

        if not isinstance(datos, list):
            print("El archivo JSON de entrada no contiene una lista en el nivel raíz.")
            return

        nuevos_datos = []
        for pregunta in datos:
            if isinstance(pregunta, dict):
                pregunta_actualizada = pregunta.copy()
                pregunta_actualizada[name_attribute] = value_attribute
                nuevos_datos.append(pregunta_actualizada)
            else:
                print(f"Advertencia: Se encontró un elemento no-diccionario en la lista y fue omitido: {pregunta}")
                nuevos_datos.append(pregunta) # Opcional: si quieres incluir los elementos que no son diccionarios

        with open(path_output_file, 'w', encoding='utf-8') as f_salida:
            json.dump(nuevos_datos, f_salida, indent=2, ensure_ascii=False)

        print(f"Archivo generado exitosamente en: {path_output_file}")

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{path_json_file}' no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo de entrada '{path_json_file}' no es un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llama a la función
add_attribute_dict_to_all_file("faq.json", "faq_1.json", "nivel", 1)


# {0: 7, 1: 4, 2: 23, 3: 16, 4: 41, 5: 48}