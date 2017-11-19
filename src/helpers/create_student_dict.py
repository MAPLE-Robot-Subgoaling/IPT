import os, pickle

students = []

for dir in os.listdir("."):
    if not os.path.isdir(dir): continue
    subdirs = os.listdir("./"+dir)
    for name in subdirs:
        if name not in students:
            students.append(name)

pickle.dump(students, open("students.txt", "wb"))
