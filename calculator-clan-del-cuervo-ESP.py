# Códigos de escape ANSI para colores
rojo = '\033[91m'
verde = '\033[92m'
amarillo = '\033[93m'
azul = '\033[94m'
magenta = '\033[95m'
cian = '\033[96m'
reset = '\033[0m'  

# Ejemplo de uso de colores
# print(rojo + "Este texto es rojo" + reset)
# print(verde + "Este texto es verde" + reset)
# print(amarillo + "Este texto es amarillo" + reset)
# print(azul + "Este texto es azul" + reset)
# print(magenta + "Este texto es magenta" + reset)
# print(cian + "Este texto es cian" + reset)

# suma
def suma(a, b):
    return a + b

# resta
def resta(a, b):
    return a - b

#  multiplicación
def multiplicacion(a, b):
    return a * b

#  división
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "[-]Error: División por cero"

while True:

    print(azul +"""
                .__                  .__               .___                       
  ____  _____   |  |    ____   __ __ |  |  _____     __| _/ ____ _______ _____    
_/ ___\ \__  \  |  |  _/ ___\ |  |  \|  |  \__  \   / __ | /  _ \\_  __ \\__  \   
\  \___  / __ \_|  |__\  \___ |  |  /|  |__ / __ \_/ /_/ |(  <_> )|  | \/ / __ \_ 
 \___  >(____  /|____/ \___  >|____/ |____/(____  /\____ | \____/ |__|   (____  / 
     \/      \/            \/                   \/      \/                    \/  


""" + reset)
    
    print("""
 __________________________
|    _________________     |
|   |clan_del_cuervo  |    |
|   |_________________|    |
|  ___ ___ ____       ___  |
| | 1 |suma    |     | + | |
| |___|___|____|     |___| |
| | 2 |resta   |     | - | |
| |___|___|____|_____|___| |
| | 3 |multiplicacion| x | |
| |___|___|____|_____|___| |
| | 4 |division|     | / | |
| |___|___|____|     |___| |
| | 5 |exit    |           |
| |___|___|____|           |
|                          |
|__________________________|
""")

    opcion = input("\nCALCULADORA-D.C.D: ")

    if opcion == "5":
        print("¡Adiós!")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input( verde + f"[+]" "Ingresa el primer número: " + reset))
        
        num2 = float(input( amarillo +"[+]Ingresa el segundo número: " + reset))

        if opcion == "1":
            resultado = suma(num1, num2)
            print(rojo + f"[+]Resultado: {resultado}" + reset)

        elif opcion == "2":
            resultado = resta(num1, num2)
            print(rojo + f"[+]Resultado: {resultado}" + reset)

        elif opcion == "3":
            resultado = multiplicacion(num1, num2)
            print(rojo + f"[+]Resultado: {resultado}" + reset)

        elif opcion == "4":
            resultado = division(num1, num2)
            print( rojo + f"[+]Resultado: {resultado}" + reset)
            
    else:
        print( rojo+"[-]Opción inválida. Por favor, selecciona una opción válida (1/2/3/4/5)."+reset)
