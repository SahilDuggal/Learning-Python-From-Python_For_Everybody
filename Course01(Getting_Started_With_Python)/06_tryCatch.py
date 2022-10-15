# The function will ask for a sentence and convort it to int which is not possible,
# So at the place of error/trace back 0 will be outputted.
from tokenize import Double


x = input("Enter the sentence : ")
try:
    # Try Function will try thr code mentioned 
    # If the code runnes then ok otherwise it will run except code.
    con_01 = int(x)
    print("Converted to int output is : ",con_01)
except:
    con_01 = 0
    print(con_01)

# At this step as the input is number and it can be conerterd to int so it will run and convert to int
# If we enter sentance or word or even float value over here it will output 0.
y = input("Enter the number : ")
try:
    con_02 = int(y)
    print("Converted to int output is :",con_02)
except:
    con_02 = 0
    print(con_02)

# At this step as the input is number and it can be conerterd to float so it will run and convert to float/double
# If we enter sentance or word value over here it will output 0.
z = input("Enter the number : ")
try:
    con_03 = float(z)
    print("Converted to float output is :",con_03)
except:
    con_03 = 0
    print(con_03)
