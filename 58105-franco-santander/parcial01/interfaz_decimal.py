'''ESTE MODULO SIRVE PARA QUE EL USUARIO INGRESE UN NUMERO DECIMAL 
Y EL PROGRAMA LE DEVUELVA EL NUMERO EQUIVALENTE EN HEXADECIMAL'''

def main():
    from decimal_hexadecimal import hexad_to_decimal, no_letra
    print('Ingrese un numero decimal')
    n = input()
    numero = no_letra(n)
    hexad_number = hexad_to_decimal(numero)
    print('El numero ingresado en hexadecimal es: ',hexad_number)

main()
