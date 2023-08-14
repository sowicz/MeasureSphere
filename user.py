import json


class User():
    def __init__(self):
        self.user = {}
        self.user_list = []
        self.id = 1


    def add_user(self, name, surname, pin, key_user):
        self.user = {
        "id": self.id,
        "name" : name,
        "surname" : surname,
        "pin": pin,
        "key_user": key_user,
        "is_logged": False
        }
        self.user_list.append(self.user)
        self.id += 1

    
    def delete_user():
        pass

    
# ---- functionc outside class ----
# ---------------------------------


# with open("users_data.json", mode="r") as f:
#     users_json = json.load(f)

def show_users():
    """func to print user id and user name to LOG in inside app"""
    with open("users_data.json", mode="r") as f:
        users_json = json.load(f)
    for key in users_json:
        print("Id: {}, Name: {}".format(key["id"], key["name"]))


def printall():
    """Func to pring all users with all parameters dev use only"""
    for key in users_db.user_list:
        print(key)



def welcome(num):
    """func to welcome user after log in and switch parameter is_logged to true
    more than 1 user can be logged in 
    """
    with open("users_data.json", "r") as f:
        users_json_data = json.load(f)
        wrong_id = []
        try:
            for key in users_json_data:
                if key["id"] == int(num):
                    key["is_logged"] = True
                    print("Hello {} {}".format(key["name"], key["surname"]))
                    wrong_id.append(True)
                else:
                    wrong_id.append(False)
            if not any(wrong_id):
                    print("Wrong ID, please choose correct Id number")
        except:
            print("Choosed id is not number, please choose correct id number")
        save_user_to_json(users_json_data)


x = False

def show_who_login():
    """function to show who is logged now with possible return 
    if don't want to choose account to log out"""
    global x
    with open("users_data.json", mode="r") as f:
        users_json_data = json.load(f)
        print("Users are logged in:")
        users_logged = []
        for key in users_json_data:
            users_logged.append(key["is_logged"])
            if key["is_logged"] == True:
                print("id: {}, name: {}, surname: {} ".format(key["id"], key["name"], key["surname"]))
                x = True
        if x == True:
            print("r: return")
        if not any(users_logged):
            print("No users are logged in")
            x = False

def show_logged():
    """function to show logged in accout without possible return just show"""
    global x
    with open("users_data.json", mode="r") as f:
        users_json_data = json.load(f)
        print("Users are logged in:")
        users_logged = []
        for key in users_json_data:
            users_logged.append(key["is_logged"])
            if key["is_logged"] == True:
                print("id: {}, name: {}, surname: {} ".format(key["id"], key["name"], key["surname"]))
        if not any(users_logged):
            print("No users are logged in")
            x = False


def goodbye(num):
    """logout user"""
    global x
    with open("users_data.json", mode="r") as f:
        users_json_data = json.load(f)
        wrong_id = []
        try:
            for key in users_json_data:
                if key["id"] == int(num):
                    if key["is_logged"] == False:
                        continue
                    else:
                        key["is_logged"] = False
                        print("Good Bye {} {}".format(key["name"], key["surname"]))
                        wrong_id.append(True)
                        x = False
                else:
                    wrong_id.append(False)
            if not any(wrong_id):
                print("Wrong ID, please choose correct Id number")
        except:
           print("Choosed id is not number, please choose correct id number") 
        save_user_to_json(users_json_data)




def save_user_to_json(userdata):
        """save to json data after changes"""
        with open("users_data.json", "w") as f:
            userdata_to_save = json.dumps(userdata, indent=2)
            f.write(userdata_to_save)


def create_json(userdata):
    """create json file """
    try:
        with open("users_data.json", "x") as f:
            userdata_to_save = json.dumps(userdata, indent=2)
            f.write(userdata_to_save)

    except:
        print("file exist")

# ---- END of function outside class ----
# ---------------------------------------



#creating instance of class user
users_db = User()

#add some users old method
users_db.add_user("Kamil","Wololo", "1234", True)
users_db.add_user("Max", "Oneal", "1234", False)
users_db.add_user("Klark", "Dyiop", "1234", False)
users_db.add_user("John", "Wick", "1392", False)
users_db.add_user("Fernando", "Leozzo", "1111", False)



create_json(users_db.user_list)

# print(users_db.user_list)
# show_users()