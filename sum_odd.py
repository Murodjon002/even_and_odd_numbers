#A four-digit integer is given. Find the sum of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
var_int=1365
sum_even=0

x=var_int%10
var_int//=10
y=var_int%10
var_int//=10
a=var_int%10
var_int//=10
b=var_int%10

sum_even=x*(x%2)+y*(y%2)+a*(a%2)+b*(b%2)
print(sum_even)