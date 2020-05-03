import os
import glob
from colorama import Fore, Style
from temp_folder_path import PATH_TO_TEMP_FOLDER
from terminal_style_functions import print_message_with_color

def main():
    total_deleted = 0
    list_of_files_and_directories = glob.glob(PATH_TO_TEMP_FOLDER, recursive=True)
    total = len(list_of_files_and_directories)

    user_response = input('Do you want to see all temporary files/directories? (y - Y/n - N or any other character): ').lower()

    if (user_response == 'y'):
        print('Ok, this is the list of files currently: \n')
        for file in list_of_files_and_directories:
            print(f'{file}\n')

    user_response = input('Do you want to delete all of these files? (y - Y/n - N or any other character): ').lower()

    if (user_response == 'y'):
        print('Deleting files...\n')

        for file in list_of_files_and_directories:
            try:
                os.remove(file)
                print_message_with_color(f'File {str(file)} deleted!', Fore.GREEN)
                total_deleted += 1
            except Exception as exception_message:
                print_message_with_color(
                    f"Can't delete file {str(file)} because of the following error: {str(exception_message)}. Going for the next one.",
                    Fore.RED)

        print_message_with_color(f'Finished. Total of files/directories: {str(total)} | Total of deleted files/directories: {str(total_deleted)}',
        Fore.GREEN)
    else:
        print("Ok, I won't do anything to it.")
main()