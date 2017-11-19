paths = ["/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_onlystruc.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_onlyexec.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_onlydata.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_nostruc.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_noexec.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_nodata.txt",
         "/Users/mneary1/Desktop/IPT/data/results_hw3_norewrite_all.txt"]

for file in paths:
    with open(file) as f:
        l = file.split("/")
        s = l[-1]
        l[-1] = s.replace("results_hw3_norewrite_", "")
        l.insert(-1, "results_hw3")

        new_file = "/".join(l)

        with open(new_file, "w") as w:

            for line in f:
                # skip files where nothing was found
                if 'XXXXX' in line:
                    continue

                #print(line, end="")
                line = line.strip(",\n")
                line = line.replace('[', '').replace(']', '').replace(' ', '').replace(':', ',')
                #print(line)
                w.write(str(line))
                w.write("\n")
                #print()


