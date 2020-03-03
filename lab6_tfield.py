#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:55:35 2020

@author: tfield
"""
import sys
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

# Error check based on the number of inputs
numInputs = len(sys.argv)
if numInputs == 3: #Input and Output file names provided
    #Input and output file names defined
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
elif numInputs == 2: #Only input file name provided
    #If no output filename is defined, use the input filename with .pdf extension
    inputFileName = sys.argv[1]
    outputParts = inputFileName.split('.')
    outputFileName = outputParts[0]
    for i in range(1, len(outputParts)-1):
        outputFileName = outputFileName + '.' + outputParts[i]
    outputFileName = outputFileName + '.pdf'
elif numInputs == 1: #No input file provided
    print("You need to define at least an input filename!")
else: #More than the input and output file names provided
    print("Too many inputs!")

if ((numInputs ==2) or (numInputs == 3)):
    # Reads in the data from the file, using the first line as the name for each column of data
    data = np.genfromtxt(inputFileName, names=True, unpack=True)
    
    outFig = plt.figure()
    plt.suptitle('Lab 6 Output - Field')
    
    #The first plot
    plt.subplot(311)
    plt.plot(data['Year'], data['Mean'], 'k')
    plt.plot(data['Year'], data['Max'], 'r')
    plt.plot(data['Year'], data['Min'], 'b')
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('Streamflow (cfs)')
    plt.legend(['Mean', 'Maximum', 'Minimum'], loc='best')
    
    #The second plot
    plt.subplot(312)
    plt.plot(data['Year'], data['Tqmean']*100, '*g')
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('Tqmean $\mu_{Tq}$ (%)')
    plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter())
    
    #The third plot
    plt.subplot(313)
    plt.bar(data['Year'], data['RBindex'])
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('R-B Index (ratio)')
    plt.show()
    
    #Format everything nicely and save the three plots to a single PDF file
    outFig.tight_layout(rect=[0, 0, 1, .9])
    outFig.savefig(outputFileName, bbox_inches='tight')
    
    
    
    
    
    
    
    
    
    
    
