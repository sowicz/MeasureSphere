import user
import json
import submenu


#Get user input for main menu operations
def get_user_choice():
    user_choice = input("Your choice: ")
    return user_choice

#function to show users list to log in
def choose_id():
    print("-"*20)
    print("Chose Id: ")
    user.show_users()
    print("r: return")


# ---- main menu of program ----
# ------------------------------


wait_for_input = True

while wait_for_input:
    print("Please choose:")
    print("1: Log In")
    print("2: Log out")
    print("3: Show who is logged in")
    print("q: exit and save")
    user_choice_level1 = get_user_choice()

    if user_choice_level1 == "1":
        choose_id()
        user_choice_level2 = get_user_choice()
        if user_choice_level2 != "r":
            user.welcome(user_choice_level2)
            print("-"*20)

            submenu.submenu1()
        print("-"*20)


    elif user_choice_level1 == "2":
        print("-"*20)
        user.show_who_login()
        if user.x == True:
            user_choice_level2 = get_user_choice()
            if user_choice_level2 != "r":
                user.goodbye(user_choice_level2)
        print("-"*20)

    elif user_choice_level1 == "3":
        print("-"*20)
        user.show_logged()
        print("-"*20)

    elif user_choice_level1 == "q":
        break

    else:
        print("Wrong choice, please write correct value")
        print("-"*20)


