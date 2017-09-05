"""Using the 'shapes' module to create shapes and control their attributes"""
from shapes import Triangle, Rectangle, Oval


# create a rectangle:
rect_1 = Rectangle(color=None)
# set the attributes:

#rect_1.set_width(200)
#rect_1.set_height(100)
#rect_1.set_color('blue')
# draw the rectangle:
rect_1.draw()


# create an oval:
oval_1 = Oval()

oval_1.set_width(100)
oval_1.set_height(50)
oval_1.set_color('yellow')
oval_1.set_x(100)
oval_1.set_y(200)

oval_1.draw()


rect_2 = Rectangle()

#rect_2.set_width(100)
#rect_2.set_height(150)
#rect_2.set_color('yellow')
#rect_2.set_x(100)
#rect_2.set_y(75)

#rect_2.draw()


oval_2 = Oval()

oval_2.set_width(100)
oval_2.set_height(50)
oval_2.set_color('red')
oval_2.set_x(100)
oval_2.set_y(50)

oval_2.draw()

