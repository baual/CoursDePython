# Concept
# .join() build a string from a list
# .join() is a method applied to a separator string and iterates through its argument


# tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 
# " ".join(tip_words)
# a space (" ") is the separator that gets injected between the objects in the argument (the list "tip_words")
# Result = "Notebooks can be exported as .pdf"

# Examples

tip_words = ['Notebooks', 'can', 'be', 'exported', 'as', '.pdf'] 
# join tip_words objects with spaces
print(" ".join(tip_words))
# output
# Notebooks can be exported as .pdf
no_space = ""
letters = ["P", "y", "t", "h", "o", "n"]
print(no_space.join(letters))
# output
# Python

print()

# [ ] review and run example - .join() iterates through sequences
dash = "-"
space = " "
word = "Iteration"
ellipises = "..."

dash_join = dash.join(word)
print(dash_join)
# output
# I-t-e-r-a-t-i-o-n
print(space.join(word))
# output
# I t e r a t i o n
print(ellipises.join(word))
# output
# I...t...e...r...a...t...i...o...n

#word has been cast as a list !!!!
#see next file :-)