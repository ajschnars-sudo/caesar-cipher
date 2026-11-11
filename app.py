import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
valid_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
replay = False
def opt1():
        while True:
            shift = input("Enter the shift(ex. 2,8,6,): ").strip()
            if shift.isdigit():
                shift = int(shift)
                break
            else:
                clear()
                print("error, invalid input\n Try again")
        print(f"valid characters: {list(valid_chars)}")
        msg = input("Enter your message: ")
        converted = ""
        for i in msg:
            if i in valid_chars:
                idx = valid_chars.index(i)
                idxshift = (idx + shift)%len(valid_chars)
                converted += valid_chars[idxshift]
            else:
                converted+= i 
        return converted,shift
def opt2():
    while True:
        file_name = input("Enter the file name(m for main menu): ").strip()
        if file_name == "m" or file_name == "M":
            return file_name,0,0
        else:
            break
    converted = ""
    file_name += ".txt"
    with open(file_name, "r") as file:
        contents = file.readlines()
        valid_chars = contents[0]
        valid_chars = valid_chars.replace("\n","")
        shift = contents[1]
        shift = int(shift.replace("\n",""))
        shift = -shift
        msg = contents[2]
    for i in msg:
        if i in valid_chars:
            idx = valid_chars.index(i)
            idxshift = (idx + shift)%len(valid_chars)
            converted += valid_chars[idxshift]
        else:
            converted+= i 
    return converted,contents,file_name

def file_check():
    file_path  = input("pick a name for your file: ").strip()
    file_path += ".txt"
    return file_path
def restart():
    clear()
    print("error, invalid input")
    for i in ["resterting",".",".","."]:
        print(i,end = " ",flush = True)
        time.sleep(1)
    clear()
clear()
while True:
    while True:
        print("---CAESAR CIPHER MESSAGING---")
        play = input("\nStart a message(1)\nRead and reply to a message(2)\nQuit(3)\nanswer here: ").strip()
        if play == "1":
            msg,shift = opt1()
            file_path = file_check()
            with open(file_path, "w") as file:
                file.write(f"{valid_chars}\n{shift}\n{msg}")
            break
        elif play == "2":
            msg,text,file_path = opt2()
            if msg.strip().lower() == "m":
                break
            else:
                pass
            valid_chars = text[0].replace("\n","")
            shift = int(text[1].replace("\n",""))
            print(msg)
            reply = input("How would you like to respond(m to go back to menu): ").strip()
            if reply == "m" or reply == "M":
                break
            else:
                pass
            converted = ""
            for i in reply:
                if i in valid_chars:
                    idx = valid_chars.index(i)
                    idxshift = (idx + shift)%len(valid_chars)
                    converted += valid_chars[idxshift]
                else:
                    converted+= i
            print(f"this is your reply encrypted: {converted}")
            with open(file_path, "a") as file:
                file.write(f" \n \n {converted}")
            print("reply sent")
        elif play == "3":
            print("bye bye")
            break
    if play == "3":
        break
    else:
        pass