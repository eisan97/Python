# standard input/output

# Output
a=10
b=15
print('Hello World {}'.format(a)) 
print('Hello World {} {}'.format(a,b)) 
print('Hello World {1} {0}'.format(a,b))
print('Hello World %s' % a)
print('Hello World %f' % a)
print('Hello World %.2f' % a)

# Input
# name = 'Thin Ei San'
name = input('Enter your name : ')
print(f'Hello {name}')