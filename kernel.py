import msvcrt
import threading
import os
import time

# options = 5
# index = 0
# list = ["Item"]*options
# while True:
#     os.system("cls")
#     if index > options-1:
#         index = 0
#     if index < 0:
#         index = options-1
#     for i in range(options):
#         temp = ["*", " "][i != index]
#         print(temp, list[i], temp)
#     char = msvcrt.getch()
#     if char == b'\xe0':
#         char = msvcrt.getch()
#         if char == b'H':
#             index -= 1
#         elif char == b'P':
#             index += 1
#     if char == b'\r':
#         print("AYEEEE YOU SELECTED!!")
#         break
#     if char == b'\b':
#         print("AYEEEE YOU NOT SELECTED!!")
#         break

def loadmodule(module_call):
    module_call()
    cls()


def slp(a: int):
    time.sleep(a)


def pause():
    os.system("PAUSE")


def cls():
    os.system("cls")

def menu_handler():
    cls()
    print('Escape key pressed')
    print('Paused. Press it again to resume.')
    msvcrt.getch()
    cls()

def fetch_input(prompt: str):
    input_str = ""
    cursor_pos = 0
    print(prompt+"-")
    while True:
        key = msvcrt.getch()
        if key == b'\x1b':
            menu_handler()
            print(prompt+"-")
        if key == b'\r':
            break
        elif key == b'\x08':
            if cursor_pos > 0:
                input_str = input_str[:cursor_pos-1] + input_str[cursor_pos:]
                cursor_pos -= 1
                print("\b \b" + input_str[cursor_pos:] + " " *
                      (len(input_str) - cursor_pos), end="", flush=True)
                print("\b" * (len(input_str) - cursor_pos), end="", flush=True)
        elif key == b'\xe0':
            arrow_key = msvcrt.getch()
            if arrow_key == b'K':
                if cursor_pos > 0:
                    cursor_pos -= 1
                    print("\b", end="", flush=True)
            elif arrow_key == b'M':
                if cursor_pos < len(input_str):
                    cursor_pos += 1
                    print("\r" + input_str[:cursor_pos] +
                          input_str[cursor_pos:], end="", flush=True)
                    print("\r" + input_str[:cursor_pos], end="", flush=True)
        else:
            input_str = input_str[:cursor_pos] + \
                key.decode() + input_str[cursor_pos:]
            cursor_pos += 1
            print("\r" + input_str[:cursor_pos] + input_str[cursor_pos:], end="", flush=True)
            print("\r" + input_str[:cursor_pos], end="", flush=True)
    print("")
    return input_str


def bootloader():
    print("Loading...")
    time.sleep(2)


def authwall():
    user_credentials = {'user': 'pass'}
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
        username = fetch_input("Username")
        password = fetch_input("Password")
        if username in user_credentials and user_credentials[username] == password:
            print('Loggging In...')
            slp(2)
            break
        else:
            print('Invalid username or password. Please try again.')


def system():
    print("Desktop")
    pause()

while True:
    cls()
    loadmodule(module_call=bootloader)
    loadmodule(module_call=authwall)
    loadmodule(module_call=system)
    break