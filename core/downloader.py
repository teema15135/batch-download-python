from threading import Thread
from time import sleep

import magic
import requests

from core.constant import DEFAULT_OUTPUT_DIRECTORY


def is_mime_type_match(mime_type, allowed_mime_types):
    return mime_type in allowed_mime_types


def _download_file(url, output_sub_directory, allowed_mime_types, header):
    output_directory = DEFAULT_OUTPUT_DIRECTORY + output_sub_directory + "/"

    output_path = get_output_path_from_url(url, output_directory)

    is_invalid = True
    while is_invalid:
        response = requests.get(url, stream=True, headers=header)
        if response.status_code == 404:
            break
        with open(output_path, 'wb') as local_file:
            if is_mime_type_match(magic.from_buffer(response.content, mime=True), allowed_mime_types):
                local_file.write(response.content)
                is_invalid = False
            else:
                sleep(1)


def download_files(urls_map, allowed_mime_types, header):
    """
    Creates and starts download threads

    :param header: Dict for requests header
    :param urls_map: URLs map key is batch name, value is array of url
    :param allowed_mime_types: Array of mimetypes allowed (e.g., ["image/jpeg", "image/png"]
    :return: Started download threads
    """
    thread_list = []

    for k in urls_map.keys():
        for url in urls_map[k]:
            thread_list.append(Thread(target=_download_file, args=(url, k, allowed_mime_types, header)))

    for thread in thread_list:
        thread.start()

    return thread_list


def get_output_path_from_url(url, output_directory):
    filename = url.split("/")[-1].split("?")[0]
    output_path = f'{output_directory}{filename}'
    return output_path
