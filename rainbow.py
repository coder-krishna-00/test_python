#!/usr/bin/env python3

def rainbow(colour):
    rainbow_colours = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
    for rainbow_colour in rainbow_colours:
        if (colour == rainbow_colour):
            print ("You entered a valid Rainbow Colour: "+ colour)
        elif (colour != rainbow_colour and rainbow_colours.index(rainbow_colour) == (len(rainbow_colours) - 1)):
            print (colour + " is not a valid Rainbow Colour.")

colour = input("Enter a Rainbow Colour:" )
rainbow(colour)



