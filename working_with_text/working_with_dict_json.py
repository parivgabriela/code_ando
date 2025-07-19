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
