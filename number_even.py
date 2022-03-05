#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=1234
x=var_int%10
var_int//=10
y=var_int%10
var_int//=10
a=var_int%10
var_int//=10
b=var_int%10

s=(a+1)%2+(b+1)%2+(x+1)%2+(y+1)%2
print(s)
