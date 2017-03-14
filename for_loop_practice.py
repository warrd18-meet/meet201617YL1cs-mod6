import turtle

def print_triangle(n_lines):
    for i in range(n_lines +1 ):
        print ("*" * i )

print_triangle(2)
print_triangle(4)
print_triangle(10)

my_drawing=[ (0,0), (50,0), (50,50), (0,50), (100,100) ]
for my_pos in (my_drawing):
    turtle.goto(my_pos)
    
x=3
x=x+3
x-=3
print (x-3)
print (x)

    
