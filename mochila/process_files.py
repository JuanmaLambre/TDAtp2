import glob, os
from parser import parse

for file in os.listdir("../../smallcoeff_pisinger"):
    if file.endswith(".csv"):
        parse("../../smallcoeff_pisinger/" + file)