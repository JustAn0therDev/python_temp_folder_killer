import os
import glob
from temp_folder_path import PATH_TO_TEMP_FOLDER

def main():
    total_deleted = 0
    list_of_files_and_directories = glob.glob(PATH_TO_TEMP_FOLDER, recursive=True)
    total = len(list_of_files_and_directories)

    user_response = input('Do you want to see all temporary files/directories? (y - Y/n - N): ')
    if (user_response.lower() == 'y'):
        print('Ok, this is the list of files currently: \n')
        for file in list_of_files_and_directories:
            print(file)

    user_response = input('Do you want to delete all of these files? (y - Y/n - N): ')

    if (user_response.lower() == 'y'):
        print('Deleting files...')
        for file in list_of_files_and_directories:
            try:
                os.remove(file)
                total_deleted += 1
            except Exception as exception_message:
                print(f"Can't delete file {str(file)} because of the following error: {str(exception_message)}. Going for the next one.")

        print(f'Finished. Total of files/directories: {str(total)} | Total of deleted files/directories: {str(total_deleted)}')
    else:
        print("Ok, I won't do anything to it.")

main()