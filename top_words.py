import os
import chardet
import json


PATH_TO_FILES_DIR = 'news_files/'
WORDS_MIN_LENGTH = 7
TOP_NUMBER = 10


def get_filelist():
    filelist = []
    for file_name in os.listdir(path=PATH_TO_FILES_DIR):
        if not file_name.startswith('.'):
            filelist.append(file_name)
    return filelist


def encode_data():
    with open(PATH_TO_FILES_DIR + file_name, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        encoded_text = data.decode(result['encoding'])
    return encoded_text


def parse_json():
    country_news = encode_data()
    country_news_parsed_json = json.loads(country_news) 
    for item in country_news_parsed_json['rss']['channel']['items']:
        # print(item['description'])


for file_name in get_filelist():
    test()
    # get_news_description_only()
    # print_popular_words()