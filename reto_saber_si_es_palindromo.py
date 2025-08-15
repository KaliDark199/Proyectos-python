number = input("ingrese un palidromo: ")

def es_palindromo(number):
    for i in number:
        if number == number[::-1]:
            return True
            print ("es palindromo")
        else:
            return False 
            print ("no es palindromo")
        
print (es_palindromo(number))