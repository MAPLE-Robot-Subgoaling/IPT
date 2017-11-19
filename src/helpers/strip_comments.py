import os, re

r = re.compile("[\s]*#[.]*")

for dir in os.listdir("."):
    if not os.path.isdir(dir): continue
    if dir == ".git": continue
    
    for file in os.listdir(dir):
        name = "./" + dir + "/" + file
        with open(name) as f:
            lines = f.readlines()
            lines = list(filter(lambda x: not r.match(x), lines))
        
        with open(name, "w") as f:
            for line in lines:
                f.write(line)

    
