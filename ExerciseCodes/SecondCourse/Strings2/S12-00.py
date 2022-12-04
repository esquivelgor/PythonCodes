# Metodos de cadenas

# count()

s = "Olá mundo, Olá"
print("Count = " + str(s.count("Olá"))) 

# find() e index()

print("Find = " + str(s.find("O")))
print("Index = " + str(s.index("O")))

# rfind() 

print("RFind = " + str(s.rfind("O")))

# startswith() e endswith()

print("Startswith = " + str(s.startswith(("Olá"))))
print("Endswith = " + str(s.endswith(("mundo"))))

# isnumeric(), isdecimal(), isdigit()
n1 = "121"; n2 = "13 12"; n3 = "fef212"
print("Isnumeric = " + str(n1.isnumeric()))
print("Isdecimal = " + str(n2.isdecimal()))
print("Isdigit = " + str(n3.isdigit()))


