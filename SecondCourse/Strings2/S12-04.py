# Una frase es palíndromo si se lee igual de derecha a izquierda que de izquierda a derecha,
#  pero obviando los espacios en blanco y os de puntuación. Por ejemplo, las cadenas ’sé verla al revés’,
#  ’anita lava la tina’, ’luz azul’ y ’la ruta natural’ contienen frases palíndromas. 
# Diseña un programa que diga si una frase es o no es palíndroma


s = input("Ingresa un texto: ").strip().replace(" ", "")
j = -1
for i in range(int(len(s)/2)):
    if s[i] == s[j]:
        palindrome = True
    else: 
        palindrome = False
    j -= 1
if palindrome:
    print("Es un palindromo")
else:
    print("No es un palindromo")

