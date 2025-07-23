def string_calculator(cadena):
    if cadena == "":
        return 0
    if len(cadena) == 1:
        if "," in cadena:
            return sum(int(x) for x in cadena.split(",") if x.isdigit())
        return int(cadena)

