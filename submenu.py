import json
import user
import data.lines as lines
import data.machines as machines

def user_choice():
    print("-"*20)
    user_choice = input("Your choice: ")
    return user_choice


def choose_id():
    print("-"*20)
    print("Chose Id: ")
    user.show_users()
    print("r: return")



def submenu1():
    """function that is imported to main program, loads json user data, 
    check if someone is logged in, then show submenu"""
    with open("users_data.json", "r") as f:
        userdata = json.load(f)
        for key in userdata:
            if key["is_logged"] == False:
                continue
            elif key["is_logged"] == True:
                show_submenu()



submenu_work = True

def show_submenu():
    """sumbmenu, normal menu + options that is showed after someone is logged in"""
    while submenu_work == True:
        print("Please choose:")
        print("1: Log In")
        print("2: Log out")
        print("3: Show who is logged in")
        print("4: Start measuring")
        print("5: Export measuring data")
        print("6: Add production line")
        print("7: Add production machine")
        print("8: Add measuring model/element")
        print("q: Close program - logout all users ")

        user_choice_level3 = user_choice()

        if user_choice_level3 == "1":
            choose_id()
            user_choice_level4 = user_choice()
            if user_choice_level4 != "r":
                user.welcome(user_choice_level4)
            print("-"*20)
        

        elif user_choice_level3 == "2":
            user.show_who_login()
            if user.x == True:
                user_choice_level4 = user_choice()
                if user_choice_level4 != "r":
                    user.goodbye(user_choice_level4)

            with open("users_data.json", "r") as f:
                userdata = json.load(f)
                users_logged = []
                for key in userdata:
                    users_logged.append(key["is_logged"])
                if not any(users_logged):
                    # submenu_work == False
                    break
            print("-"*20)


        elif user_choice_level3 == "3":
            user.show_logged()
            print("-"*20)


        elif user_choice_level3 == "q":
            print("Program closed")
            print("-"*20)
            # submenu_work == False
            with open("users_data.json", "r") as f:
                users = json.load(f)
                for key in users:
                    if key["is_logged"] == True:
                       key["is_logged"] = False
                       print("Good Bye {} {}".format(key["name"], key["surname"]))
                    else:
                        continue
                user.save_user_to_json(users)

            break
        elif user_choice_level3 == "6":
            lines.prod_1.add_prod_line()

        elif user_choice_level3 == "7":
            machines.machine_1.add_machine()


        else:
            print("-"*20)
            print("Wrong choice, please write correct value")
            print("-"*20)


# def check_logged_in():
#     with open("users_data.json", "r") as f:
#         userdata = json.load(f)
#         for key in userdata:
#             print(key)
#             print(key["is_logged"])
#             if key["is_logged"] == False:
#                 continue
#             else:
#                 return True
