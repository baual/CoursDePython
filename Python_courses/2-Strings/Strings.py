first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string)
#resultat = True on dirait que c'est pariel mais le comportement change en fonction de ce qu'il y a dans la chaine de acractère
print('') #on passe ue ligne




third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)
#comme ici on a mis un ' entre une chaine de " et vice versa l'interet du " est qu'il 'auto implemente du deuxieme entre autres
print("")





fifth_string = 'A single quoted literal string with an \' escaped single quote' #\ permer d'intégrer le ' ou " dans une chaine qui commence par le même signe ' ou "
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'    # ici on ajoute une fin de ligne
eighth_string = 'A literal string with a \t tab character'          # ici une tabulation

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

print()



nineth_string = r"A literal string with a \n new line character printed raw"

print(nineth_string) #la ligne de sortie est la m^mem que ci-dessus donc sequence \ marchent avec ' et pas "


print()


#va etre rigolo celui là
tenth_string = '''A literal string
    on more than one line
sometimes known as a verbatim string'''

eleventh_string = """Another literal string
     on more than one line
using double quotes"""

print(tenth_string)
print(eleventh_string)

#comportement

#A literal string
#   on more than one line
#sometimes known as a verbatim string
#Another literal string
#     on more than one line
#using double quotes

print()

#use print() with other parameters
first = 'Conrad'
second = 'Grant'
third = 'Bob'
print(first,second)                             #imprime les 2 variables avec un espace entre chaque
print(first, second, third)                     #imprime les 3 variables avec un espace entre chaque
print(first, second, third, sep='-')            #imprime les 3 variables avec - en tant que séparateur entre chaque
print(first, second, third, sep='-', end='.')   #imprime les 3 variables avec un espace entre chaque et un . à la fin
print()
print("autres fonctions de print")

message = str.capitalize('first message')
print(message)
message = 'second message'.capitalize()
print(message)
message = 'third message'
print(message.capitalize())
#le resultat est le même on met en majuscule la premiere lettre de la chaine

print()
message = 'hello world'
print(message.lower())  #tout en minuscules
print(message.upper())  #tout en majuscules

message = message.title()   #majuscule sur la premiere lettre de chque mot
print(message)
print(message.swapcase())   #on inverse minuscule et majuscule

print()

#compte le nombre de s
location = 'Mississippi'
print(location.count('s'))
print()

#retourner longueur de la chaine de caractere
print(len('how many letters in this string?'))
print()

#tests boolean
message = 'racecar'
print(message.startswith('r'))      #resultat=True
print(message.startswith('a'))      #resultat=False
print(message.startswith('ra'))     #resultat=True
print()
print(message.endswith('r'))        #resultat=True
print(message.endswith('a'))        #resultat=False
print(message.endswith('ar'))       #resultat=True

print()

#trouve un caractère dans la chaine : retourne sa position. Le premier caractère de la chaine est à la position 0
message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))    #resultat=4
print(message.find('t'))    #resultat=31
print(message.find('T'))    #resultat=0
#si il trouve pas il renvoie -1
#cherchez pas cette phrase est un pangramme : elle utilise toutes les lettres de l'alphabet 1 fois
#par contre ca marche avec les majuscules sauf si vous 'lowerisez' la chaine d'abord.
print(message.find('H'))    #resultat=-1
print(message.lower().find('T'))    #resultat=-1
#on peut "enchainer" les fonctions : normal message.lower() est aussi un str() donc ca marche !!!!!!
print()



#le milieu !
message = '    middle    '
print('.' + message.lstrip() + '.')     #.middle     .  : enlève les espaces vides à gauche
print('.' + message.rstrip() + '.')     #.    middle.   : enlève les espacesvides  à droite
print('.' + message.strip() + '.')      #.middle.       : enlève les espaces vides à droite et à gauche

print()

#maintenant on rajoute à droite ou à gauche
message = 'howdy'
print(message.rjust(20))        #ici du vide à droite
print(message.rjust(20, '-'))   #ici 20 - à droite
print(message.ljust(20))        #ici du vide à gauche
print(message.ljust(20, '-'))   #ici 20 - à gauche

print()

#remplace des chaines de carctères par une autre:
message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

print()

print()


#Index Slicing [:], [::2]
#[:] returns the entire string
#[::2] returns the first char and then steps to every other char in the string
#[1::3] returns the second char and then steps to every third char in the string
#the number 2, in the print statement below, represents the step
#use [::-1] to reverse a string

student_name = "Colette"
# return all
print(student_name[:])
#output: Colette

# return every other
print(student_name[::2])
#output:Clte

# return every third, starting at 2nd character
print(student_name[1::2])
#output:oet

long_word = "consequences"
# starting at 2nd char (index 1) to 9th character, return every other character
print(long_word[1:9:2]) #OnSeQuEn
#output:osqe

long_word = "characteristics"
# make the step increment -1 to step backwards
print(long_word[::-1])
#output: scitsiretcarahc

# start at the 7th letter backwards to start
print(long_word[6::-1])
#output: tcarahc

print()

student_name = "Skye"
for letter in student_name[:3]:
    print(letter)
# output
# s
# k
# y
print()
for letter in student_name[::-1]:
    print(letter)
# output
# e
# y
# k
# s
print()
# start at "y" (student_name[2]), iterate backwards
for letter in student_name[2::-1]:
    print(letter)
# output
# y
# k
# s