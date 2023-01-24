import re 
import sys
import os

if len(sys.argv)>1:
        print(f"Reading {sys.argv[1]}")
else:
    raise RuntimeError("No input file provided")

input_file = str(sys.argv[1])
with open(input_file, mode="r") as f:
    o_input = f.read()

four_zeroes = r"(\s+)(0000)(\s+)"                    #Capture spaces (group 1 and 3) and 0000
m_input = re.sub(four_zeroes, r"\g<1>0\3", o_input) #Put back spaces, substitute 0

zero_before_mat = r"(\s+)(0)([1-9]\d\d)(\s+)"              #Capture spaces (group 1 and 4) and mat number
m_input = re.sub(zero_before_mat, r"\1\3\4", m_input) #Put back spaces, substitute 0

default_libraries = r"\n(M0000)|\n(\s+(NLIB|PNLIB|PLIB|ELIB|HLIB))" #Capture default libraries strings
m_input = re.sub(default_libraries, r"\nC \1\2", m_input)           #comment all of them

material_card = r"\n(M|MT|MX)(0)([1-9]\d\d)"               #Find M, MT and MX
m_input = re.sub(material_card, r"\n\1\3", m_input)     #Remove 0

print(f"Modified input file saved in {os.getcwd()}/inp_gxs")

with open("inp_gxs", mode="w") as f:
    f.write(m_input)