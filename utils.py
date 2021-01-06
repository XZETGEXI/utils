import os

from pprint import pprint



def logger(verbose = True):
    """ Logger initiation """
    
    W, H = os.get_terminal_size()
    def log(*arg):
        if verbose:
            print("_" * W)
            msgs = [*arg]
            for msg in msgs:
                print(str(msg).upper().rjust(W, "|"))
            print("‾" * W)
    return log

class InputError(Exception):
    def __init__(self, msg, expression):
        self.msg = msg
        self.expression = expression

def sanitized_input(msg = "Input :"):
    user_input = input(msg)
    try:
        return str(user_input)
    except:
        raise InputError("Bad input", user_input)

class SelectionError(Exception):
    def __init__(self, msg, expression = ""):
        self.msg = msg
        self.expression = expression

def file_selector(dir_path = None):
    """
    Ask for input
    Return selected file as str
    """
    
    log("Entering file selector")
    
    if not dir_path:
        current_dir = os.getcwd()
    else:
        try:
            current_dir = os.chdir(dir_path)
        except FileNotFoundError:
            raise SelectionError("Invalid dir name")
            
    file_list = [file for file in os.listdir(current_dir) if os.path.isfile(file)]
    if not file_list:
        raise SelectionError("Empty directory")
        
    file_dict = {str(n): file for n, file in enumerate(file_list)}
    for n, file in file_dict.items():
        print(str(n).rjust(3), "->", file)
    
    user_input = sanitized_input("Which file do you want? ")
    
    try:
        user_input = str(user_input)
        return file_dict[user_input]
        
    except KeyError:
        raise SelectionError(user_input, "Selection not in range")
    except:
        raise SelectionError("Undefined error")
