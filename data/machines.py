import json

class Machine():
    def __init__(self):
        self.machine_list = []

    def add_machine(self):
        try:
            with open("./data/machine_data.json", mode="r") as f:
                data = json.load(f)
                print(data)
            print("Machine name (min. 3 characters):")
            machine_name = input()
            while len(machine_name) < 3:
                print("Wrong line name, please type correct line name:")
                machine_name = input()
            data.append(machine_name)
            print("List of existing machines:")
            print(data)
            with open("./data/machine_data.json", mode="w") as s:
                self.machine_list = data
                machine_json_to_save = json.dumps(self.machine_list, indent=2)
                s.write(machine_json_to_save)
        except:
            print("empty json")
            with open("./data/machine_data.json", mode="w") as f:
                print("Machine name (min. 3 characters):")
                machine_name = input()
                while len(machine_name) < 3:
                    print("Wrong line name, please type correct line name:")
                    machine_name = input()
                self.machine_list.append(machine_name)
                machine_json_to_save = json.dumps(self.machine_list, indent=2)
                f.write(machine_json_to_save)



machine_1 = Machine()

