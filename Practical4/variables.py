a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
print("change 2004-2014:", d)
print("change 2014-2024:", e)
if d<e:
    print("Growth is acelerating")
elif d>e:
    print("Growth is decelerating")
else:
    print("Growth rate is constant")
# d=0.25, e=0.21999999999999975
# d is larger than e
# The population growth appears to be declarating because the increase from 2014 to 2024 is smaller than that from 2014 to2024
X = True
Y = False
W = X or Y
print("W =", W)
# Truth table for W =X or Y
# X       Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False