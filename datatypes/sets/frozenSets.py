# Frozen Sets

# Frozen Set doesn't allow to Update and remove operations.


s = {1,2,3,4,5} # This is a set.

f= frozenset(s) # This is a expression which is supposed not to work. Let's see PVM throws what sort of error message ? 
f.update([20])

Only Navigate and access the values of frozen set are allowed.

