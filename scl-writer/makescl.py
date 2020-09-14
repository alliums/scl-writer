# -*- coding: utf-8 -*-

from ratioDict import ratios
import math
from fractions import Fraction
import fileinput
import sys
import os
import string

print("\n*~Shruti / Interval to .SCL Translator~*")
print("PEACE! LAND! BREAD!\n")

print("One line should have one scale.")
print("Begin the line with the name of the scale to be used as the filename.")
print("You can optionally put a description after this.")
print("End the name with !, then the description(if you have one) with another !")
print("Then begin the scale. Every file needs exactly 1 or 2 exclamation points.")
print("Use interval notation in fractional form or decimal form(cents).")
print("1 octave = 2/1 = 1200.0000")
print("The program will calculate the number of steps for you.")
print("Do not include the tonic note (1).")
print("Carnatic swara are accepted. View ratioDict.py for more information.")

print("\nPerfectly valid lines look like this:")
print("jyoti-swarupini.scl ! 68th Melakarta Raga ! 10/9 5/4 27/20 3/2 128/81 9/5 2")
print("Jyoti-swarupini ! 68th Melakarta Raga ! S R₃ G₃ M₂ P D₁ N₂ Ṡ")



inFilename = input("enter full the filename of your input file: ")

inFile = open(inFilename, "r",encoding="utf-8")
inLines = inFile.readlines()
raw = []

for scale in inLines:
    occur = scale.count("!")
    if occur == 1:
        name = scale.split("!")[0]
        scale = scale.split("!")[1]
        splitScale = scale.split(" ")
        splitScale.append(name)
        splitScale.append(occur)
        raw.append(splitScale)
    if occur == 2:
        name = scale.split("!")[0]
        description = scale.split("!")[1]
        scale = scale.split("!")[2]
        splitScale = scale.split(" ")
        splitScale.append(description)
        splitScale.append(name)
        splitScale.append(occur)
        raw.append(splitScale)

    #print(i.split("\n"))

print(raw)


print("~~~~~")
currentScale  = []
scales = []

for i in raw:
    occur = i.pop()
    if occur == 1:
        outFilename = i.pop().strip()
    if occur == 2:
        outFilename = i.pop().strip()
        description = i.pop().strip()

    ##remove empty elements
    i = [q for q in i if q]
    ##counter
    c = 0

    print("\n")
    ##build current scale list
    for j in i:
        j = str(j)
        c += 1
        print(c, ": ", j)
        if j.strip() == "1" or j.strip() == "2" or j[0].isalpha():
            currentScale.append(ratios.get(j.strip()))
        else:
            currentScale.append(j.strip())


    scales.append(currentScale)
    ##making output files
    outFilename = outFilename + ".scl"
    if not os.path.exists("./files"):
        os.mkdir("./files")

    outFile = open("./files/" + outFilename,  "w+",encoding="utf-8")
    outFile.write("! " + outFilename + "\n!\n")

    #print info to the console for the human!
    print(currentScale)
    print(outFilename)
    print(c, "intervals")
    if occur == 2:
        print(description)
        outFile.write(str(description) + "\n")
    print("--------")

    ##count the number of steps in the scale and stick the fooker here
    outFile.write(" " + str(c) + "\n!\n")

    for i in currentScale:
        if i:
            outFile.write(" " + i + "\n")
    outFile.write("\n")
    currentScale = []
    outFile.close()
