        #  01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:-27:-1] # OR we can write it like this [25::-1] & this [::-1] see previous for why this works.
print(backwards)


# Challenge (could not figure out how to reverse only select numbers 'qpo'
#SOLUTIONS:

# Create a slice that produces the characters 'qpo' (make sure starting value greater than ending going in reverse)
print(letters[16:13:-1])

# slice the string to produce 'edcba'
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
# OR can also use ([:-9:-1]) instead of [25:17:-1]

# list of idioms in P code that are useful for slicing
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])