def number(string):
    if('%' not in string):
        return float(string)*100
    number = string.strip('%')  
    try:
        number = float(number)  
        return number
    except ValueError:
        return None  
print(number('78'))