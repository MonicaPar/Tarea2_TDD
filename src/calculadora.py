def string_calculator(cadena):
    if cadena == "":
        return 0
    if len(cadena) == 1:
        if cadena.isdigit():
            return int(cadena)
        else:
            return cadena
