print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + "world")
greeting = "Hello"
name = "Nadine"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print(type(greeting))
print(type(age))

#___________________________________________________________________________________________
# Here we are using code from the old file "strings" and put an 'f' in front of "is and {age} in curly brackets.
# This fixed the old code that was giving an error:
age_in_words = "2 years"
# old error code  was: print(name + " is " + age + " years old")
print(name + f" is {age} years old ")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

