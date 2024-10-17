import turtle
from turtle import Screen
import random
import colorgram

# for this project, we will be using a package called colorgram.py
# it's a library of code written in python that allows us to extract colors from images
# we will end up with a pallet that looks similar to the image in the end
# it takes two inputs: image, and the number of colors to extract

# commented out - only extract colors once
# colors = colorgram.extract('hirst.jpeg', 30)
# rgb_list = []
# for rgb_tuple in colors:
#     unnamed_tuple = (rgb_tuple.rgb.r, rgb_tuple.rgb.g, rgb_tuple.rgb.b)
#     rgb_list.append(unnamed_tuple)
# print(rgb_list)

# list of colors
turtle.colormode(255)
color_pallet = [(35, 95, 186), (238, 164, 77), (245, 223, 88), (252, 48, 19), (215, 69, 106), (94, 197, 235), (204, 72, 19), (252, 136, 165), (188, 46, 91), (143, 233, 216), (245, 102, 139), (165, 175, 233), (67, 45, 12), (68, 207, 171), (84, 188, 101), (253, 220, 0), (252, 151, 1), (20, 157, 50), (166, 27, 7), (24, 37, 87), (105, 39, 45), (106, 213, 251), (22, 151, 230), (254, 12, 1), (37, 46, 98), (103, 91, 182)]
    #(217, 150, 117), (137, 162, 198), (244, 236, 239), (157, 58, 49), (35, 43, 60), (231, 213, 108), (189, 142, 153), (60, 93, 132), (145, 181, 163), (66, 111, 92), (57, 49, 46), (50, 42, 45), (201, 92, 81), (114, 87, 97), (41, 60, 55), (39, 60, 101), (225, 174, 166)]
    #[(217, 150, 117), (137, 162, 198), (244, 236, 239), (157, 58, 49), (35, 43, 60), (231, 213, 108), (189, 142, 153), (60, 93, 132), (145, 181, 163), (66, 111, 92), (57, 49, 46), (50, 42, 45), (201, 92, 81), (114, 87, 97), (41, 60, 55), (39, 60, 101), (225, 174, 166), (219, 173, 177), (168, 189, 221), (134, 42, 37), (86, 129, 176), (44, 76, 66), (159, 114, 125), (178, 198, 188), (64, 66, 58), (104, 138, 130), (86, 54, 60)]

# program requirements:
# 1. create a painting of 10x10 spots
# 2. each dot should be 20 in size, and space them apart by 50 paces

# print(turtle.screensize())
# print(turtle.pos())

turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()
turtle.setposition(-232, -221)
y = 0
for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(color_pallet))
        turtle.forward(50)
    if i < 9:
        y += 50
        turtle.setposition(-232, -221+y)
screen = Screen()
screen.exitonclick()