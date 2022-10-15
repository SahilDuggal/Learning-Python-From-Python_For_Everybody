# the major differenc between a list and a tuple is that
# Tuples are immutable. and on the place of [], () are used.
#   Things can't be done is tuples:-
#       sort(), append(), reverse(), etc.
#   Things can be done is tuples:-
#       t = tuple()
#       print(dir(t))

#  Sorting lists of tuples by key:-
d = {'a':10,'c':1,'b':22}
print(d.items())
print(sorted(d.items()))

#  Sorting lists of tuples by values:-
d = {'a':10,'c':1,'b':22}
temp = list()
for k,v in d.items():
    temp.append((v,k))
print(temp)

temp = sorted(temp, reverse=False)
print(temp)
