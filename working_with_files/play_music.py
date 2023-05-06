import os
from playsound import playsound

def play_list_of_folder(folder:str):
    """play music in a specific folder

    Args:
        folder (str): path where the music is
    """
    list_in_folder = os.listdir(folder)
    included_extensions = ['.mp3', ".avi", ".m4a"]
    music_in_folder = [file for file in list_in_folder if any(file.endswith(ext) for ext in included_extensions)]
    print(music_in_folder)
    for music in music_in_folder:
        playsound(f'{folder}/{music}')
