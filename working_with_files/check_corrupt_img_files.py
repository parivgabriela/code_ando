import os
from PIL import Image

folder_path = 'ruta/a/tu/carpeta/de/imagenes'

def check_corrupt_images_files(folder_path):
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file)
                try:
                    with Image.open(file_path) as img:
                        img.verify()  # Verifica si la imagen es válida
                except (IOError, SyntaxError) as e:
                    print(f"Archivo corrupto o no válido: {file_path}")
                    os.remove(file_path)  # Elimina el archivo corrupto
        else:
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verifica si la imagen es válida
            except (IOError, SyntaxError) as e:
                print(f"Archivo corrupto o no válido: {file_path}")
                os.remove(file_path)  # Elimina el archivo corrupto

import tensorflow as tf


from tensorflow.keras.preprocessing import image # Para cargar imágenes

def normalize_image(img):
    """ Cargamos la imagen y la redimensionamos al tamaño esperado por el modelo """
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) # Añadimos una dimensión extra para el batch
    img_array /= 255.0 # Normalizamos los valores de píxeles (0-1)
    return img_array

def get_image_url_tf(url_file):
    """  Descargamos la imagen usando tensorflow"""
    img_path = None
    try:
        img_path = tf.keras.utils.get_file(url_file)
    except Exception:
        print("No se pudo descargar la imagen, asegúrate que la URL es correcta.")
    return img_path
