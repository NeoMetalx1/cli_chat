import os
from time import gmtime, strftime

username = input("Enter user name: ")
current_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())


try:
    while True:
        os.system("cat chat.txt")
        user_input = input("Enter text: ")
        if user_input.lower() == "exit":
            break
        
        with open("chat.txt", "a", encoding="utf-8", errors="replace") as file:
            file.write(f"[{username}] => {user_input}\n {current_time} \n\n")
        
        os.system("cat chat.txt")

finally:
    pass
