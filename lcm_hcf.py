''' In this program the dividers from 2 to 9 are first checked whether they are factors of given numbers in line 13 
if they are not the factors of numbers then incremented in line 19
the factors are stored to hcf in line 14
also the numbers after removal of factors are obtained by dividing  with the divider as lines 15,16,17 
and the lcm is obtained by multiplying common factors i.e. hcf with the remaining numbers '''


numbers = list(map(int , input("Enter any three numbers seperated by , : ").split(',')))
#here map is used to iterate and convert each element to integer and then all are stored to numbers as list
divider = 2
hcf = 1
lcm = 1
print(numbers)
while divider <= 9 :
    if numbers[0] % divider == 0 == numbers[1] % divider and numbers[2] % divider == 0:
        hcf *= divider 
        numbers[0] /= divider
        numbers[1] /= divider
        numbers[2] /= divider
    else :
        divider += 1
print('\nHCF of given three numbers is {}.'.format( hcf))
print('\nLCF of given three numbers is {}.'.format(int(numbers[0])* int(numbers[1])*int(numbers[2])* hcf))
