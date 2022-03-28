
age = 24
print("My and is {0} years".format(age))

# Examples of how to use '.format'

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# NOTE long code lines are not good so can split over 2 lines as above.

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31)) # output same as above.

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31)) # in .format(28=0, 30=1, 31=2) so outputs number of days in each month as typed.

print()
print("""Jan: {2} 
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))

