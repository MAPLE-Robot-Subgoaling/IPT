import os
data = os.listdir("/Users/mneary1/Desktop/IPT/data/HW3")
fs = list(filter(lambda x: ".py" in x, data))

fname = "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_with_labels.txt"
results = open(fname)
fname2 = '/Users/mneary1/Desktop/IPT/data/hw3_labels.txt'
labels = open(fname2)

known_labels = {'0': "'else:' immediately followed by 'if'",
         '1': "unreached decision",
         '2': "unused variable",
         '3': "reassignment",
         '4': "miscast data",
         '5': "unnecessary function",
         'X': "nothing extraneous"
         }

label_count = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, 'X':0}
label_dict = {}

for line in labels:
    items = line.strip().split("y,")
    fname = items[0]+"y"
    lbls = items[1].split(",")
    label_dict[fname] = lbls
    for lbl in lbls:
        label_count[lbl] += 1

print("{:>36}:{:>5}".format("number of programs", len(data)))
for key in known_labels:
    pct = label_count[key] / len(data) * 100
    print("{:>36}:{:>5} ({}%)".format(known_labels[key], label_count[key], round(pct, 2)))

print()

result_known = {'0': "'else:' immediately followed by 'if'",
         '1': "unreached decision",
         '2': "unused variable",
         '3': "reassignment",
         '4': "miscast data",
         '5': "unnecessary function",
         '6': "misidentified as extraneous",
         '7': "other/unidentified as first",
         'X': "nothing extraneous"
         }

result_count = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, 'X':0}
result_dict = {}

for line in results:
    result_items = line.strip().split(":")
    fname = result_items[0]
    if result_items[1] == 'XXXXX':
        result_dict[fname] = ['X']
        result_count['X'] += 1
    else:
        items = result_items[-1].split(",")
        result_dict[fname] = items
        for item in items:
            result_count[item] += 1


correct_count = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, 'X':0}

for key in result_dict:
    result = result_dict[key]
    truth = label_dict[key]
    for r in result:
        if r in truth: #correct
            correct_count[r] += 1

print("By error:")
for key in result_count:

    if key in label_count:
        pct = correct_count[key] / label_count[key] * 100
        print("{:>36}:{:>5} ({}%)".format(known_labels[key], correct_count[key], round(pct, 2)))
    else:
        print("{:>36}:{:>5}".format(result_known[key], result_count[key]))

results.close()
labels.close()
