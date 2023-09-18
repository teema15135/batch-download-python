import json
import os

from core.constant import DEFAULT_ALLOWED_MIMETYPE_FILE, URL_SPLITTER, HEADER_COLLECTION_DIRECTORY, DEFAULT_INPUT_DIRECTORY


def walk_input_directory():
    return [files for root, dirs, files in os.walk(DEFAULT_INPUT_DIRECTORY)]


def read_mimetype_allowed():
    with open(DEFAULT_ALLOWED_MIMETYPE_FILE, 'r') as input_file:
        return input_file.read().split(URL_SPLITTER)


def read_header_dict(name):
    if len(name.strip()) == 0:
        return {}
    with open(HEADER_COLLECTION_DIRECTORY + name + ".json", 'r') as header_json_file:
        return json.load(header_json_file)


def read_file(path):
    with open(path, 'r') as input_file:
        lines = input_file.read().split(URL_SPLITTER)
        urls = [url.strip() for url in lines if len(url.strip()) > 0]
        return urls
