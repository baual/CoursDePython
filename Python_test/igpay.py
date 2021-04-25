# "pass a word
# if start with a vowel then writes "ay" at the end
# else writes first letter of the world and "ay" at the end"

def igpay(word):
    if word[0] in "aeiouAEIOU":
        return word + "ay"
    else: 
        return word[1:] + word[0] + "ay"

test=input("enter a word:")
print(igpay(test))