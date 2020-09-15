# scl-writer
create batches of .scl files with .txt inputs.

simply open up command line, clone the repo, run makescl.py, follow the instructions.

the program takes a text file, each line containing one scale, composed of its intervals, its name, and its description.
then it creates a directory (./file/) and outputs a .scl file for every scale.

You may be asking - what is the point of an .scl formatter if you my end up having to type out every file?
The point is to support translations of libraries, not individual files, where it is much easier to put a batch of files into the convertable format than to type them out individually. 
Unless it is in carnatic notation, there is currently no advantage to using this program if you only need to translate one file.
It may also be helpful since the parameters of the separation algorithm use exclamation points, you can easily write a script to scrape a site and process all of the data into 
name ! description ! scale format.

Things that will probably be added:
1. support for implicit intervals - a mode where the user first designates a tonic and then provides subsequent explicit notes whose intervals are calculated and generalized into a mode.
2. Eventually, someday, a gui

on formatting:

Carnatic notes work. check ratioDict.py for a full list of Carnatic notes and their ratios.
More conversions be added as time goes on.

ratios are acceptable as numbers in decimal or fraction format. 
fractions like (a/b)

check example-input.txt.

requires Python 3

