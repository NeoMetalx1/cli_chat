import os

username = input("Enter user name: ")

try:
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == "exit":
            break
        
        with open("chat.txt", "a", encoding="utf-8") as file:
            file.write(f"[{username}] => {user_input}\n\n")
        
        os.system("cat chat.txt")

finally:
    pass
