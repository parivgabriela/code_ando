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


def group_json_by_attribute(input_file_path, output_file_path, group_by_key, collect_values_key):
    """
    Groups items from a JSON list of dictionaries by a specified attribute (group_by_key)
    and collects the values of another attribute (collect_values_key) for each group.

    Args:
        input_file_path (str): The path to the input JSON file.
        output_file_path (str): The path where the new grouped JSON file will be saved.
        group_by_key (str): The key by which to group the dictionaries.
        collect_values_key (str): The key whose values will be collected for each group.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f_input:
            data = json.load(f_input)

        if not isinstance(data, list):
            print(f"Error: The input JSON file '{input_file_path}' does not contain a list at the root level.")
            return

        grouped_data = {}

        for item in data:
            if not isinstance(item, dict):
                print(f"Warning: Non-dictionary item found in the list and skipped: {item}")
                continue

            group_value = item.get(group_by_key)

            # Get the value of the key we want to collect
            value_to_collect = item.get(collect_values_key)

            if group_value is not None:
                if group_value not in grouped_data:
                    grouped_data[group_value] = []
                # Add the collected value to the list for this group
                if value_to_collect is not None:
                    grouped_data[group_value].append(value_to_collect)
                else:
                    print(f"Warning: Key '{collect_values_key}' not found or had a None value in item: {item}. Skipping its collection.")
            else:
                print(f"Warning: Key '{group_by_key}' not found or had a None value in item: {item}. Item skipped from grouping.")

        # Save the grouped data to the output file
        with open(output_file_path, 'w', encoding='utf-8') as f_output:
            json.dump(grouped_data, f_output, indent=2, ensure_ascii=False)

        print(f"Data successfully grouped by '{group_by_key}' and saved to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The input file '{input_file_path}' is not a valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


from collections import defaultdict

def group_json_by_key(input_path: str, output_path: str, group_key: str) -> None:
    """
    Reads a JSON file containing a list of objects, groups them by `group_key`,
    and writes the result to a new JSON file.

    :param input_path: Path to the input .json (expects a list at top level).
    :param output_path: Path where the grouped JSON will be written.
    :param group_key: The key in each object to group by.
    """
    # Load data
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Input JSON must be an array of objects")

    # Group using defaultdict
    grouped = defaultdict(list)
    for item in data:
        key_value = item.get(group_key)
        grouped[key_value].append(item)

    # Optionally convert None key to a string like "__undefined"
    # grouped = {"__undefined" if k is None else k: v for k, v in grouped.items()}

    # Write result
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(grouped, f, indent=2, ensure_ascii=False)

categorias_faq = {1: "Programación", 2: "Ciencia de datos", 3: "IA", 4: "Estadistica", 5: "Inteligencia del negocio"}
