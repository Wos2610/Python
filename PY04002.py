class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color[0].upper() + color[1:].lower()
        self.perimeter = 2 * (width + height)
        self.area = width * height
        

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print('INVALID')
else:
    print('{} {} {}'.format(r.perimeter, r.area, r.color))