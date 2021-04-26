#"convert roman numbers to arabic ones
# how it works ? ben je sais pas n va chercher :-)
# Roman	Arabic
# i 1
# v 5
# X 10
# l	50
# c	100
# d	500
# m	1000
# if a letter except i as is predecessor then you can the letter value - its predecessor value except for X which is I,
#  C which is X


def numerous(romanfigure):
    retour=0
    for (p,roman) in enumerate(romanfigure): #by using "enumerate" we got the index directly !!!!
        if roman=='I':
            retour+=1
            continue
        if roman=='V':
            if romanfigure[p-1]=='I':
                retour+=5-2 #+5-2=+3
            else: retour+=5
            continue
        if roman=='X':
            if romanfigure[p-1]=='I':
                retour+=10-2
            else: retour+=10
            continue
        if roman=='L':
            if romanfigure[p-1]=='X':
                retour+=50-20
            else: retour+=50
            continue        
        if roman=='C':
            if romanfigure[p-1]=='X':
                retour+=100-20
            else: retour+=100
            continue        
        if roman=='M':
            if romanfigure[p-1]=='C':
                retour+=1000-200
            else: retour+=1000    
            continue    

    return retour




test=input("enter the roman number:")

print(numerous(test.upper()))