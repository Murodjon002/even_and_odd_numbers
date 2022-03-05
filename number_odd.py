#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=5679
x=var_int%10
var_int//=10
y=var_int%10
var_int//=10
a=var_int%10
var_int//=10
b=var_int%10

s=x%2+y%2+a%2+b%2
print(s)