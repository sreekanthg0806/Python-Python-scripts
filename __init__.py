print("Hello,World!")
# first comment
print("Hello")  # comment no-2
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
print(word)
print(sentence)
print(paragraph)
counter=100
name="Alex"
seconds=10.5
a=b=c=10
p,q,r=1,2.5,"john"
print(counter,name,seconds)
print(a,b,c,p,q,r)
val1=1
val2=10
print(val1,val2)
del val1,val2
print("values got deleted")
value=10  #integer
pi=3.14   #float
com= -654+12j #complex
print(value,pi,com)
#str="Welcome!"

#print(str)
#print(str[0])
#print(str[len(str)-1])
#print(str[3:7])
#print(str * 3)
#print(str+"to python")

list1=['john',10,2.5,'alex',1]
list2=[123,'smith']

print(list1) #prints complete list1
print(list2) #prints complete list2
print(list1[2:4]) #prints elements from 3rd till 4th
print(list2 * 2) #prints list2 two times
print(list1 + list2)
print(list1[0]) #prints 1st element of list1 concatenated with 1st element of list2
print(list1 + list2) #prints concatenated list of list1 and list2

tuple1=('john','123','25.68','456')
tuple2=('alex','789')

print(tuple1)
print(tuple2)
print(tuple1[1:3])
print(tuple2 * 2)
print(tuple1[0:1])
print(tuple1 + tuple2)

dict1 = {}
dict1['one'] = "This is one"
dict1[2]     = "This is two"

dict2 = {'name': 'john','val':6734, 'dept': 'sales'}


print (dict1['one'])   # Prints value for 'one' key
print (dict1[2])       # Prints value for 2 key
print (dict2)          # Prints complete dictionary
print (dict2.keys())   # Prints all the keys
print (dict2.values()) # Prints all the values

# if-statements
var = 10
var1 = 0
if var == 10 :
    print("Value of var is " + str(var))
if var1 > 0 :
    print("Value of var1 is " + str(var1))

# if-else statements
if var1 != 0 :
    print("Value of var1 is not equal to zero")
else:
    print("Value of var1 is equal to zero")

# Nested-if
if var < 50:
    print("Value of var is less than 50")
    if var == 30:
        print("Which is 30")
    elif var == 10:
        print("Which is 10")
    else:
        print("Which is not either 10 or 20")
elif var > 50:
    print("Value of var is more than 50")
else:
    print("Couldn't find value of var")


# Prints out 0,1,2,3,4 using while loop

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Prints out only even numbers - 2,4,6,8,10 using for loop

for x in range(10):
    # Check if x is even
    if not x % 2 == 0:
        continue
    print(x)
#nested loop----printing prime numbers less than 100

i=2
while(i<100):
    j=2
    while(j<=(i/j)):
        if not (i%j): break
        j=j+1
    if(j> (i/j)): print(str(i)+" is prime")
    i=i+1

#difference between continue and pass--printing elements of list

a=[0,1,2,3]
for ele in a:
    if not ele:
        pass
    print(ele)
print("------")
for ele in a:
    if not ele:
        continue
    print(ele)

x = 4
y = 12
if y%x:
    print(" y mod x = 0 as fn evaluation")
else :
    print("y mod x is equal to 0")
