#Una palabra es ((alfabética)) si todas sus letras están ordenadas alfabéticamente. 
# Por ejemplo, ((amor)), ((chino)) e ((himno)) son palabras ((alfabéticas)). 
#Diseña un programa que lea una palabra y nos diga si es alfabética o no.

x = input("Ingresa un texto: ")
words = [];  
for i in x:
    w = format(ord(i),'08b')
    words.append(w) 

for i in range(len(words)):
    if words[i-1] >= words[i]:
        order = False
    else:
        order = True

if order:
    print("La palabra es alfabética")
else:
    print("La palabra no es alfabética")