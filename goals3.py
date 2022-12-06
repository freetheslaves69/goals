colorlist = ['red', 'blue' , 'yellow', 'green']
print( "you can print one color  . index numbers go from 0 to " , len(colorlist) )
i = int(input("Which color do you want to print"))
while i >= len(colorlist):
    i = int(input("Enter correct number: "))
print(colorlist[i])