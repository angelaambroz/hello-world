#!/usr/bin/env python 

import turtle
import random
import math


def draw_stuff():
	window = turtle.Screen()
	window.bgcolor("white")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("black")
	brad.speed(20)

	for i in range(0,180):
		brad.right(i)

		#first box
		for i in range(0,4):
			brad.forward(100)
			brad.right(90)


	window.exitonclick()


draw_stuff()