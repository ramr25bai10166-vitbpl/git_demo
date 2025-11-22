#Exchange using 3rd variable
x=input("Enter value of x:")
y=input("Enter value of y:")
temp=x
x=y
y=temp
print('Swapped using third variable')
print('x=',x)
print('y=',y)
print('')

#Exchange using multiple assignment
x=input("Enter value of x:")
y=input("Enter value of y:")
x,y=y,x
print('Swapped using multiple assignment')
print('x=',x)
print('y=',y)
print('')

#Exchange using addition & subtraction
x=float(input("Enter value of x:"))
y=float(input("Enter value of y:"))
x=x+y
y=x-y
x=x-y
print('Swapped using addition & subtraction')
print('x=',x)
print('y=',y)
print('')

#Exchange using Multiplication & Division
x=float(input("Enter value of x:"))
y=float(input("Enter value of y:"))
x=x*y
y=x/y
x=x/y
print('Swapped using multiplication & division')
print('x=',x)
print('y=',y)
