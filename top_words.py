import os
import chardet
import json


PATH_TO_FILES_DIR = 'news_files/'
WORDS_MIN_LENGTH = 7
TOP_NUMBER = 10


def get_filelist():
    filelist = os.listdir(path=PATH_TO_FILES_DIR)
    return filelist
