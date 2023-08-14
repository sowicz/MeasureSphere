import json


class Model():
    def __init__(self):
        self.model_list = [] 
        self.model_dict = {}

    #function use late to show possible lines or machines form json
    def choose_from_data(self,file):
        # choose production line
        if file == "line":
            with open("./data/line_data.json", mode="r") as f:
                prod_data = json.load(f)

            global line_output
            correct = False
            while correct == False:
                print("Choose production line:")
                for index, lines in enumerate(prod_data, start=1):
                    print(f"{index}: {lines}")

                line_input = int(input())

                if line_input > len(prod_data):
                    print("wrong")
                elif line_input < 1:
                    print("wrong")
                else:
                    for index, lines in enumerate(prod_data, start=1):
                        if line_input == index:
                            line_output = lines
                            correct = True
            print(line_output)
            return line_output
        
        #choose production machine 
        if file == "machine": 
            with open("./data/machine_data.json", mode="r") as f:
                machine_data = json.load(f)

            global machine_output
            correct = False
            while correct == False:
                print("Choose production machine:")
                for index, mach in enumerate(machine_data , start=1):
                    print(f"{index}: {mach}")
                machine_input = int(input())
                if machine_input > len(machine_data):
                    print("wrong")
                elif machine_input < 1:
                    print("wrong")
                else:
                    for index, mach in enumerate(machine_data , start=1):
                        if machine_input == index:
                            machine_ouput = mach
                            correct = True
            print(machine_ouput)
            return machine_ouput



    # add model information - all inputs to get data from user about:
    # model measuring data 

    def add_model_info(self):
        # """choosing production line"""
        line = self.choose_from_data("line")
        # """choosing production machine"""
        machine = self.choose_from_data("machine")

    
        print("Add model Name or serial number:")
        model_name = input()
        print("How many measuring points/characteristics?")
        num = int(input())
        measuring_ponints_values = {}
        for i in range(1,num+1):
            print("Upper control line for P{}:".format(i))
            upper = float(input())
            print("nominal size (control line):")
            nominal = float(input())
            print("Lower control line:")
            lower = float(input())
            values = {"P{}".format(i): {
                    "Upper": upper,
                    "nominal": nominal,
                    "lower": lower
                    }}
            measuring_ponints_values.update(values)
        print(line)
        print(machine)
        print(model_name)
        print(measuring_ponints_values)
        


    def add_model_to_db(self,line, machine, name, num_measure, measuring_points):
        try:
            with open("./data/model_data.json", mode="r") as f:
                data = json.load(f)
                print(data)
            
   
            with open("./data/model_data.json", mode="w") as s:
                pass
        except:
            print("empty json")
            with open("./data/model_data.json", mode="r") as f:
                pass

model_1 = Model()

model_1.add_model_info()