
import os, re

inputf_name = "/Users/mneary1/Desktop/IPT/src/code/input2.txt"

outf_name = "/Users/mneary1/Desktop/IPT/src/code/out.txt"
outf = open(outf_name)

code_file_name = "test4.py"
code_name = "/Users/mneary1/Desktop/IPT/src/code/testfiles/" + code_file_name

cmd = "python3 -m trace --trace {} < {} > {}".format(code_name, inputf_name, outf_name)
os.system(cmd)

#determine the line number of the line that was executed in this trace
for line in outf:
    if line.startswith(code_file_name):
        print(line[line.index('(')+1:line.index(')')])