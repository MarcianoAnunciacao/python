""" f = open(r"C:\\Users\\marci\\x.txt")
for linha in f.readlines():
    print(linha.strip())
f.close()
 

with open(r"C:\\Users\\marci\\x.txt") as f:
    print(f.read())
 """
    
cripto = open(r"C:\Users\marci\y.txt", "x")    
texto = open(r"C:\Users\marci\x.txt")   
for linha in texto.readlines():
    for letra in linha:
        if letra in  'aeiouõã':
            cripto.write('*')
        else:
            cripto.write(letra)
        
texto.close()
cripto.close()       