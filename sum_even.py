#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int=1264
sum_even=0

x=var_int%10
var_int//=10
y=var_int%10
var_int//=10
a=var_int%10
var_int//=10
b=var_int%10

sum_even=x*((x+1)%2)+y*((y+1)%2)+a*((a+1)%2)+b*((b+1)%2)
print(sum_even)