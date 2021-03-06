import os
import glob
from colorama import Fore, Style
from temp_folder_path import PATH_TO_TEMP_FOLDER
from terminal_style_functions import print_message_with_color

def temp_folder_killer():
    total_files_deleted = 0
    list_of_files_and_directories = glob.glob(PATH_TO_TEMP_FOLDER, recursive=True)
    total = len(list_of_files_and_directories)

    user_response = input('Do you want to delete all files in the temp folder? (y - Y/n - N or any other character): ').lower()

    if (user_response.lower() == 'y'):
        print('Attemping to delete files...\n')

        for file in list_of_files_and_directories:
            try:
                os.remove(file)
                print_message_with_color(f'File {str(file)} deleted!', Fore.GREEN)
                total_files_deleted += 1
            except Exception as exception_message:
                print_message_with_color(
                    f"Can't delete file {str(file)} because of the following error: {str(exception_message)}.",
                    Fore.RED)

        print_message_with_color(
            f'Process finished. Total of files/directories: {str(total)} | Total of deleted files/directories: {str(total_files_deleted)}',
            Fore.GREEN)

temp_folder_killer()