x = 0x0a # hex decimal literal numbers 0a
y = 0x02  # hex decimal literal numbers 02
z = x & y 
#{02x} , 0 says its a  leading zero, 2 says that field is two character wide and x is for hexa decimal display of integer value
print(f"(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}") 
print(f"(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}")

x1 = 0x0a  
y1 = 0x05  
z1 = x | y
print(f"(hex) x1 is {x1:02x}, y1 is {y1:02x}, z1 is {z1:02x}")
print(f"(bin) x1 is {x1:08b}, y1 is {y1:08b}, z1 is {z1:08b}")

#XOR
x2 = 0x0a
y2 = 0x0f
z2 = x ^ y
print(f"(hex) x2 is {x2:02x}, y2 is {y2:02x}, z2 is {z2:02x}")
print(f"(bin) x2 is {x2:08b}, y2 is {y2:08b}, z2 is {z2:08b}")

#Left Shift
x3 = 0x0a
y3 = 0x01
z3 = x << y
print(f"(hex) x3 is {x3:02x}, y3 is {y3:02x}, z3 is {z3:02x}")
print(f"(bin) x3 is {x3:08b}, y3 is {y3:08b}, z3 is {z3:08b}")


#Right Shift
x4 = 0x0a
y4 = 0x01
z4 = x >> y
print(f"(hex) x4 is {x4:02x}, y4 is {y4:02x}, z4 is {z4:02x}")
print(f"(bin) x4 is {x4:08b}, y4 is {y4:08b}, z4 is {z4:08b}")

