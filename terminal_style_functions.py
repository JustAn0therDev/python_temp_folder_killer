from colorama import Style

def print_message_with_color(message, color):
    print(color + message)
    print(Style.RESET_ALL)