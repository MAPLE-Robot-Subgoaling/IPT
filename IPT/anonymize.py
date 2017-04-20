import os, pickle

students = pickle.load(open("students.txt", "rb"))

for dir in os.listdir("."):
    if not os.path.isdir(dir): continue
    if dir == ".git": continue
    
    for subdir in os.listdir("./"+dir):
        try:
            i = students.index(subdir)
            os.rename("./"+dir+"/"+subdir, "./"+dir+"/"+dir.lower()+"_"+str(i)+".py")
        except:
            print("Failed for:", dir, subdir)
