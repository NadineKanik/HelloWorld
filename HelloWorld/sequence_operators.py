
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "

print(string1 + string2 + string3 + string4 + string5) # but the '+' is not necessary when concatenating strings so can
# write as below too.
print("he's " "probably " "pining " "for the " "fjords") # NOTE: add space after last " to output a space in text.

# strings can also be multiplied- which is weird for other programing languages.
print("Hello " * 5) # multiplication just REPEATS what preceeds it that number of times.
# So output is Hello Hello Hello Hello Hello

# Operator precedence also applies here too. See below.
print("Hello " * (5+4))
print("Hello " * 5 + "4")

today = "friday" # This uses the 'in' operator
print("day" in today)  # True
print("fri" in today)  # True
print("thur" in today) # False
print("parrot" in "fjord") # False
