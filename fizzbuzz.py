#Created on Mon May 22 12:30:36 2023

#author: jjf3


print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,51)),sep='\n')
