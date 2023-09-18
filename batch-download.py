from core.configuration import get_allowed_mimetype
from core.directory_creator import validate_and_create_output_sub_directories
from core.downloader import download_files
from core.file_reader import read_header_dict, walk_input_directory
from core.mapper import get_input_file_url_map, get_input_file_prefix_map
from core.progress_bar import start_progress_bar_thread

global selected_header

if __name__ == "__main__":
    prefix_filename_map = get_input_file_prefix_map(walk_input_directory()[0])

    selected_header_name = input("Header file (empty is no header): ")

    urls_map = get_input_file_url_map(prefix_filename_map)
    allowed_mime_types = get_allowed_mimetype()
    header = read_header_dict(selected_header_name)

    validate_and_create_output_sub_directories(urls_map.keys())

    download_thread_list = download_files(urls_map, allowed_mime_types, header)

    start_progress_bar_thread(download_thread_list).join()

    print()
    print("Complete...")
