# python_temp_folder_killer
Simple python program to delete the contents inside the Windows temporary folder.

## Notes

It was made to delete the temp folder on my computer because that's something I need to do often and manually. The admin.py file that can be found in previous commits was not made entirely by me and can be found [in this StackOverflow answer](https://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows).

I adapted the script mentioned above to Python 3 so I could use it in the context I needed. 

It looks like Windows doesn't let Python deal with it's files so easily, so a lot of configurations must be made before applying the code to usage. The easiest and most recommended thing to do was just to execute the script as admin.
