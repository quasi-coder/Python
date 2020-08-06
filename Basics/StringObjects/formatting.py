x = 42
y =73
z = 42 * 747 * 1000
print('the number is {} {}'.format(x, y))
print('the number is {xx} {bb}'.format(xx=x,bb=y))
print('the number is {1} {0}'.format(x, y))
print('the number is {1} {0} {1}'.format(x, y))
print('the number is {0:<5} {1:>5}'.format(x, y))
#Number of spaces or zeroes including the value
print('the number is {0:<05} {1:>05}'.format(x, y))
print('the number is {0:<05} {1:+05}'.format(x, y))
print('the number is {:,}'.format(z))
print('the number is {:,}'.format(z).replace(',','.'))
print('the number is {:x}'.format(z))
print('the number is {:b}'.format(z))
print('the number is {:o}'.format(z))
print(f'the number is {x:.3f}')
print('the number is {:3f}'.format(z).replace(',', '.'))
