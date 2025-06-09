import csv
import json

def read_file(directory, create_new = False):
    """:return: A list with a str value for each line in the file"""
    output = []
    try:
        with open(directory,"r") as file:
            for line in file:
                line = line.replace("\n","")
                output.append(line)
        return output
    except:
        if create_new:
            create_file(directory)
            return output
        else:
            raise FileNotFoundError()

def read_template(directory, create_new = False) -> str:
    output = ""
    try:
        with open(directory, "r") as file:
            output = file.read()
        return output
    except:
        if create_new:
            create_file(directory)
            return output

def read_flat(directory, create_new=False):
    contents = read_file(directory, create_new)
    for line in contents:
       contents[contents.index(line)] = line.split(",")
    return contents

def read_csv(directory, create_new=False):
    """
    :param directory: The csv file you want to read
    :param create_new:  When the file does not exist, creates a new file if True, else raises an error
    """
    output = []
    try:
        with open(directory, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                output.append(row)
        return output
    except:
        if create_new:
            create_file(directory)
            return output
        else:
            raise FileNotFoundError()
            
def read_dict(directory, base_key,  create_new=False) -> dict:
    output = {}
    try:
        with open(directory, "r") as file:
            starting_line = True
            for line in file:
                line = line.replace("\n", "").split(",")
                if starting_line:
                    key_dict = {"base_key": line.index(base_key)}
                    for key in line:
                        if key != base_key:
                            key_dict[line.index(key)] = key
                    starting_line = False
                else:
                    output[current_key := line[key_dict.get("base_key")]] = {}
                    for value in line:
                        if line.index(value) in key_dict:
                            output.get(current_key)[key_dict[line.index(value)]] = value
        return output
    except FileNotFoundError:
        if create_new:
            create_file(directory)
            return output
        else:
            raise FileNotFoundError()


def create_file(directory, default_value = ""):
    try:
        open(directory,"x")
        with open(directory,"w") as file:
            file.write(default_value)
        return True
    except:
        return False

def write_file(directory, values):
    with open(directory,"w") as file:
        for value in values:
            file.write(f"{value}\n")

def write_flat(directory, values):
    for line in values:
        newline = ""
        for value in line:
            if newline != "":
                newline+=","
            newline+=str(value)
        values[values.index(line)] = newline
    write_file(directory, values)

def write_csv(directory,values):
    with open(directory,"w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(values)

def read_json(directory, create_new = False) -> list:
    output = []
    try:
        with open(directory, "r", encoding="utf8") as file:
            output = json.loads(file.read())
        return output
    except FileNotFoundError:
        if create_new:
            create_file(directory)
            return output
        else:
            raise FileNotFoundError()