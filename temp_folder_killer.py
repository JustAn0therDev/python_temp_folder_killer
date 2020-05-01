import os
import glob
import admin

def main():
    total_of_deleted_files = 0
    list_of_files_in_directory = glob.glob('C:/Users/highl/AppData/Local/Temp/*')
    total_files = len(list_of_files_in_directory)
    user_response = input('Do you want to see all temporary files/directories? (y - Y/n - N): ')
    if (user_response.lower() == 'y'):
        print('Ok, this is the list of files currently: \n')
        for file in list_of_files_in_directory:
            print(file)

    user_response = input('Do you want to delete all of these files? (y - Y/n - N): ')

    if (user_response.lower() == 'y'):
        print('Deleting files...')
        for file in list_of_files_in_directory:
            if not admin.isUserAdmin():
                admin.runAsAdmin()
            try:
                os.remove(file)
                total_of_deleted_files += 1
            except Exception:
                print("Can't delete file " + file + ". Going for the next one.")
        
        print('Finished. Total of files: ' + str(total_files)  + ' | Total of deleted files: ' + str(total_of_deleted_files))
    else:
        print("Ok, I won't do anything to it.")

main()