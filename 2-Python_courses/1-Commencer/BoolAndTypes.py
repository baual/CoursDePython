print(type('Hello world')) #string
print(type(7))  #int

print(type(True))   #bool
print(type(False))   #bool

print(type('True')) #string
print(type('False'))#string
#imprime le type de class pour le type() il faut regarder le type retourné pour les 'true' true 'false' false 
print('')                       #un espace entre chaque sortie écran

print(bool('True'))             #resultat = True
print(bool('False'))            #resultat = True
print(bool(''))                 #resultat = False
print(bool(' '))                #resultat = True
print(bool('Hello world!'))     #resultat = True
#pourquoi seul print(bool('')) est False ? parceque c'est le seul qui ai reçu une chaine de caractères vide
print('')                       #un espace entre chaque sortie écran

print(bool(7))                  #resultat = True
print(bool(1))                  #resultat = True
print(bool(0))                  #resultat = False
print(bool(-1))                 #resultat = True
#pourquoi seul print(bool(0)) est False ? parceque toute valeur non nulle est True et 0 est coniverti en False
print('')                       #un espace entre chaque sortie écran

print(1 + 1 == 3)               #resultat = False et oui 1+1 n'est pas égal à 3!!!
print(1 + 1 == 2)               #resultat = True ben oui 1+2 =2
print('')  


#Operator	Description
# ==	Equality operator
# !=	Inequality operator
# >	Greater than operator
# # <	Less than operator
# >=	Greater than or equal to operator
# <=	Less than or equal to operator


print(3 == 4)                   #resultat = False
print(3 != 4)                   #resultat = True
print(3 > 4)                    #resultat = False
print(3 < 4)                    #resultat = True
print(3 >= 4)                   #resultat = False
print(3 <= 4)                   #resultat = True

print('')



first_number = 5
second_number = 0
true_value = True
false_value = False

if first_number > 1 and first_number < 10:
    print('The value is between 1 and 10.')

if first_number > 1 or second_number < 1:
    print('At least one value is greater than 1')

print(not true_value)       #resultat = False : not operateur boolean d' "invertion"
print(not false_value)      #resultat = True

if not first_number > 1 and second_number < 10:
    print('Both values pass the test')
else:
    print('Both values do NOT pass the test')