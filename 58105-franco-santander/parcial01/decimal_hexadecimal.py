"""ESTE MODULO SIRVE PARA CONVERTIR LOS NUMEROS DECIMALES A NUMEROS HEXADECIMALES 
Y ADEMAS TESTEAR QUE LOS NUMEROS INGRESADOS NO SEAN LETRAS"""

def hexad_to_decimal(number):
    diccionario = {10: "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    num_a = str(int(number)%16)

    num_b = str(int((int(number)/16)%(16)))

    num_c = str(int(int(number)/(16*16)))


    if int(num_a) > 9:
        num_a = diccionario[int(num_a)]

    if int(num_b) > 9:
        num_b = diccionario[int(num_b)]

    if int(num_c) > 9:
        num_c = diccionario[int(num_c)]
    
    if num_c != 0:
        hexad_number = num_c + num_b + num_a
    else:
        if num_b != 0:
            hexad_number = num_b + num_a
        else:
            hexad_number = num_a
    
    return hexad_number  
def no_letra (n):
    try:
        n = int(n)
        return n
    
    except :
        return 'Disculpe, solo acepto numeros'  
 
    


