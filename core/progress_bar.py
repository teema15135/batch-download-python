from threading import Thread
from time import sleep

from core.constant import PROGRESS_BAR_LENGTH


def start_progress_bar_thread(thread_list):
    progress_bar_thread = Thread(target=_loop_print_progress_bar, args=(thread_list,))
    progress_bar_thread.start()
    return progress_bar_thread


def _loop_print_progress_bar(thread_list):
    total = len(thread_list)
    complete = 0
    while complete != total:
        complete = len([thread for thread in thread_list if not thread.is_alive()])
        rounded_progress_complete = int(complete * PROGRESS_BAR_LENGTH / total)
        print(f'\r{"*" * rounded_progress_complete}{"-" * (PROGRESS_BAR_LENGTH - rounded_progress_complete)}', end='')
        sleep(0.01)
