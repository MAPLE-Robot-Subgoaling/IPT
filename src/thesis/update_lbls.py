unlabeled = "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite.txt"
labeled = "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_labeled.txt"

un = open(unlabeled)
lb = open(labeled)

un_lines = un.readlines()
lb_lines = lb.readlines()

lb.close()
un.close()

lb_dict = {}
for line in lb_lines:
    items = line.strip().split("],")
    fname = items[0].split(":")[0].strip('*')
    lb_dict[fname] = items[1].split(',')

un_dict = {}
w = open("/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_with_labels.txt", 'w')
for line in un_lines:
    items = line.strip().split(":")
    fname = items[0]

    if items[1] == 'XXXXX':
        w.write(line)
        #print(line, end="")
    else:
        w.write(line.strip().strip(',') + ':' + ",".join(lb_dict[fname])+'\n')
        #print()
w.close()

