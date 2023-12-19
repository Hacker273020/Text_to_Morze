import os

MORSE = {'A': '.-', 'B': '-...',
         'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....',
         'I': '..', 'J': '.---', 'K': '-.-',
         'L': '.-..', 'M': '--', 'N': '-.',
         'O': '---', 'P': '.--.', 'Q': '--.-',
         'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--',
         'X': '-..-', 'Y': '-.--', 'Z': '--..',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.',
         '0': '-----', ', ': '--..--', '.': '.-.-.-',
         '?': '..--..', '/': '-..-.', '-': '-....-',
         '(': '-.--.', ')': '-.--.-', ' ': '/'}

def texto_a_morse(texto):
    texto = texto.upper()
    morse_code = ' '.join([MORSE[letra] for letra in texto])
    return morse_code

def morse_a_texto(morse_code):
    morse_code = morse_code.split(' ')
    texto = ''.join([key for value, key in MORSE.items() if value in morse_code])
    return texto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpiar_pantalla()
        print("1. Texto a Morse")
        print("2. Morse a Texto")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '0':
            break
        elif opcion == '1':
            texto = input("Ingresa el Texto: ")
            morse_code = texto_a_morse(texto)
            limpiar_pantalla()
            print("Texto en Morse:", morse_code)
            input("Presiona Enter para continuar...")
        elif opcion == '2':
            morse_code = input("Ingresa el código Morse: ")
            texto = morse_a_texto(morse_code)
            limpiar_pantalla()
            print("Texto descifrado:", texto)
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
