import json

class Prod_Line():
    def __init__(self):
        self.line_dict = {}
        self.line_list = []
        
        
    def add_prod_line(self):
        try:
            with open("./data/line_data.json", mode="r") as f:
                data = json.load(f)
                print(data)
            print("Production line name (min. 3 characters):")
            line_name = input()
            while len(line_name) < 3:
                print("Wrong line name, please type correct line name:")
                line_name = input()
            line_name_new = line_name.replace(" ", "_")
            data.append(line_name_new)
            print("List of existing machines:")
            print(data)
            with open("./data/line_data.json", mode="w") as s:
                self.line_list = data
                line_json_to_save = json.dumps(self.line_list, indent=2)
                s.write(line_json_to_save)
        except:
            print("empty json")
            with open("./data/line_data.json", mode="w") as f:
                print("Production line name (min. 3 characters):")
                line_name = input()
                while len(line_name) < 3:
                    print("Wrong line name, please type correct line name:")
                    line_name = input()
                line_name_new = line_name.replace(" ", "_")
                self.line_list.append(line_name_new)
                line_json_to_save = json.dumps(self.line_list, indent=2)
                f.write(line_json_to_save)



prod_1 = Prod_Line()


