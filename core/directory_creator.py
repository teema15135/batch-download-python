import os

from core.constant import DEFAULT_OUTPUT_DIRECTORY


def validate_and_create_output_sub_directories(directories):
    for directory in directories:
        output_directory = DEFAULT_OUTPUT_DIRECTORY + directory + "/"
        if not os.path.exists(os.path.dirname(output_directory)):
            try:
                os.makedirs(os.path.dirname(output_directory))
            except OSError:
                raise
