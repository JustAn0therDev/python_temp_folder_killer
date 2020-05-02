import os
import glob
from temp_folder_path import PATH_TO_TEMP_FOLDER

def main():
    path_to_temp_folder_without_asterisk = PATH_TO_TEMP_FOLDER[:-1]
    total_of_deleted_directories = 0
    total_of_deleted_files = 0
    list_of_files_in_directory = glob.glob(PATH_TO_TEMP_FOLDER)
    list_of_subdirectories_in_directory = os.listdir(path_to_temp_folder_without_asterisk)
    total_files = len(list_of_files_in_directory)
    total_directories = len(list_of_subdirectories_in_directory)

    user_response = input('Do you want to see all temporary files/directories? (y - Y/n - N): ')
    if (user_response.lower() == 'y'):
        print('Ok, this is the list of files currently: \n')
        for file in list_of_files_in_directory:
            print(file)

    user_response = input('Do you want to delete all of these files? (y - Y/n - N): ')

    if (user_response.lower() == 'y'):
        print('Deleting files...')
        for file in list_of_files_in_directory:
            try:
                os.remove(file)
                total_of_deleted_files += 1
            except Exception as exception_message:
                print("Can't delete file " + file + " because of the following error: " + str(exception_message) + ". Going for the next one.")

        for subdirectory in list_of_subdirectories_in_directory:
            try:
                os.remove(subdirectory)
                total_of_deleted_directories += 1
            except Exception as exception_message:
                print("Can't delete directory " + subdirectory + " because of the following error: " + str(exception_message) + ". Going for the next one.")
        
        print(f'Finished. Total of files: {str(total_files)} | Total of deleted files: {str(total_of_deleted_files)}\nTotal Directories: {total_directories} | Total of deleted directories: {total_of_deleted_directories}')
    else:
        print("Ok, I won't do anything to it.")

main()