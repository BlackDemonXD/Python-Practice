age = 16
height = 176.0
complex_number = '1+4j'

#Area of a Rectangle
print("Area of the triangle: ")
base = int(input('base: '))
height = int(input('height: '))

Area = base*height*0.5
print("Area of the triangle is", Area)

#Perimeter Of a Triangle
print("Perimeter of the Triangle: ")
side_a = int(input('a: '))
side_b = int(input('b: '))
side_c = int(input('c: '))

Perimeter = side_a+side_b+side_c
print("The Perimeter of the Triangle is", Perimeter)

#Area and Perimeter of a Rectangle
print("Area of the Rectangle: ")
rectangle_base = int(input('base: '))
rectangle_length = int(input('length: '))

Area_Rectangle = rectangle_base*rectangle_length
print("The Area of the Rectangle is", Area_Rectangle)

print("Perimeter of the Rectangle: ")
Perimeter_Rectangle = 2*rectangle_base*rectangle_length
print("Perimeter of the Rectangle is", Perimeter_Rectangle)

print("Radius of a circle: ")
r = int(input('radius: '))
Circumference = 2*3.1416*r
print("Circumference of the circle is", Circumference)

print((len('python') != (len('dragon'))))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'jargon')
print(len('python'))
string = '6'
print(string)
float = 6.0
print(float)

num = int(input('number: '))
print("The number is even:", num%2 == 0)
print("Float 7/3 is the same as Integer of 2.7:", 7//3 == int(2.7))
print("Type '10' is equal to 10", type('10') == type(10))
print("Int of 9.8 is equal to 10", int(9.8) == 10)

#Weekly earnings
print("Weekly earnings of a person: ")
Hours = int(input('Hour: '))
Rate = int(input('Rate of hour: '))
earnings = Hours*Rate
print('The weekly earning of the person is', earnings)

Years = int(input('Your age is: '))
seconds = Years*365*24*60*60
print("The seconds you have lived:", seconds)

for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
