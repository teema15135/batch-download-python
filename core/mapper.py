from core.constant import DEFAULT_INPUT_DIRECTORY, INPUT_FILE_PREFIX_SPLITTER, DEFAULT_INPUT_PREFIX
from core.file_reader import read_file


def get_input_file_url_map(prefix_filename_map):
    result = {}
    for k in prefix_filename_map.keys():
        for filename in prefix_filename_map[k]:
            if k not in result.keys():
                result[k] = []
            result[k].extend(read_file(DEFAULT_INPUT_DIRECTORY + filename))

    return result


def get_input_file_prefix_map(filenames):
    result = {}
    for filename in filenames:
        prefix = extract_input_file_prefix(filename)
        if prefix.strip() == "":
            prefix = DEFAULT_INPUT_PREFIX
        if prefix not in result.keys():
            result[prefix] = []
        result[prefix].append(filename)

    return result


def extract_input_file_prefix(filename):
    return filename.split(INPUT_FILE_PREFIX_SPLITTER)[0]
