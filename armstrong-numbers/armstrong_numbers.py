
def is_armstrong_number(number):
    aux = str(number)
    operation = sum(int(i) ** len(aux) for i in aux)
    return number == operation
