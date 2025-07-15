def est_palindrome(mot):
    return mot == mot[::-1]

mot = input("Entrez un mot : ")
if est_palindrome(mot):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
