#  List / Dictionaries / Tuples

ls = ["It's", "not","a string"]
n_ls = ["it's a",ls,'in a list']
print(n_ls)
print(n_ls[1])

# for strings value assignment does not work in a list
# for eg:-
# ls[1]='new' ---> This will not work 
# But for numbers it does 

ls = [20,50,30,40,60]
ls[4]= 10                       # replacing a particular element
print(ls)

n_ls = [60,80,100,70,90]

ad_ls = ls+n_ls                 # Concatinating 2 lists

ad_ls.sort()                    # sort the list assendingly
print(ad_ls)
ad_ls.sort(reverse=False)       # sort the list assendingly
print(ad_ls)
ad_ls.sort(reverse=True)        # sort the list decendingly
print(ad_ls)

print(ad_ls[1:5])               # slicing a list's part

print(sum(ad_ls))               # To get sum of all elements of list

print(60 in ls)                 # chech i element in list
print(60 not in ls)             # chech i element not in list


print(10 in ls)                 # chech i element in list
print(10 not in ls)             # chech i element not in list


# Sorting with a particulat key or sorting criteria.
def myKey(a):
    return a['year']            # defining the criteria.

nameAnd_YOB = [{'name':'Sahil','year':'2002'},{'name':'Saloni','year':'2005'},
{'name':'Pranav','year':'1999'},{'name':'Aanchal','year':'1995'},
{'name':'Vikesh','year':'1999'}]

nameAnd_YOB.sort(reverse=True,key=myKey)
print(nameAnd_YOB)

nameAnd_YOB.sort(reverse=False,key=myKey)
print(nameAnd_YOB)

print(dir(ls)) # To print all the functions can be performed on list
