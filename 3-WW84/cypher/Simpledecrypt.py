# Convert a letter to lowercase, for consistency.
# Convert a letter to its corresponding ASCII character code by using the ord() function.
def lassoLetter(letter, shiftAmount):
    letterCode = ord(letter.lower())
    decodedLetterCode = letterCode + shiftAmount
    decodedLetter = chr(decodedLetterCode)
    return decodedLetter

lettreacoder='w'
mouvement=2
resultlettrecodee = lassoLetter(lettreacoder, mouvement)

#"codage"
print(f"lettre {lettreacoder} codée {mouvement} : {resultlettrecodee}")

#"decodage"
print(f"lettre {resultlettrecodee} decodée - {mouvement} : "+lassoLetter(resultlettrecodee, -mouvement))
