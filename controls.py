global control_reference
control_reference = {}

def add_control_reference(key, value):
    global control_reference    
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

def return_control_refrence():
    global control_reference
    return control_reference