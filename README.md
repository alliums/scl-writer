# scl-writer
create batches of .scl files with .txt inputs.

simply open up command line, clone the repo, run makescl.py, follow the instructions.

the program takes a text file, each line containing one scale, composed of its intervals, its name, and its description.
then it creates a directory (./file/) and outputs a .scl file for every scale.


on formatting:

Carnatic notes work. check ratioDict.py for a full list of Carnatic notes and their ratios.
More conversions be added as time goes on.

ratios are acceptable as numbers in decimal or fraction format. 
fractions like (a/b)

check example-input.txt.



requires Python 3

i'll rewrite it to work with node later on. for now, all of the dependencies should be included with the latest Python.
