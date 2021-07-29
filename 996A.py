n = int(input())

hundred = n//100
n = n%100

twenty = n//20
n = n%20

ten = n//10
n = n%10

five = n//5
n = n%5

one = n

total = hundred+twenty+ten+five+one
print(total)