import os

def decision():
    print(f"Current working directory: {os.getcwd()}")
    user_decision = input("Do you want to save new credentials, or load already saved ones? (NEW/SAVED): ").strip().lower()
    if user_decision == "new":
        txt_file_creation()
    elif user_decision == "saved":
        load_new_credentials()
    else:
        print("Incorrect input")
        decision()

def txt_file_creation():
    newtxt_file_name = input("Enter the name of the website/server that you want to save the credentials under: ")
    filename = f"{newtxt_file_name}.txt"
    new_password = input("Enter the password: ")
    new_username = input("Enter the username: ")
    newcontent = f"Username: {new_username}\nPassword: {new_password}" 
    try:
        with open(filename, "w") as file:
            file.write(newcontent)
        print(f"Credentials saved to {filename}")
    except Exception as e:
        print(f"Error saving credentials: {e}")

def load_new_credentials():
    wanted_file_name = input("Enter the name of the website/server that you want to load the saved credentials from: ").strip().lower()
    filename = f"{wanted_file_name}.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error loading credentials: {e}")


decision()
