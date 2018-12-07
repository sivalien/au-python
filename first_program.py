#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import modules for mathematics
import math 
import numpy 
import matplotlib.pyplot as mpp #import module for drawing plots


if __name__=='__main__': 
    arguments = numpy.r_[0:200:0.1] #create an array of function arguments
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
        #create an array of function's values
    ) #draw the plot
    mpp.show() #show the plot on the screen
