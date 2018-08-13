
import os
folder = "/Users/mneary1/Desktop/hw3_analysis"

cstr = "The confusion matrix for"

outstr = """\\begin{{table}}
\\begin{{minipage}}{{.6\\textwidth}}
\\centering
\\begin{{tabular}}{{l|ll}}
\\backslashbox{{Results}}{{Actual}} & Positive & Negative \\\\ \\hline
Positive & {} & {} \\\\
Negative & {} & {} \\\\
\\end{{tabular}}
\\caption{{{}}}
\\end{{minipage}}
\\begin{{minipage}}{{.6\\textwidth}}
\\centering
\\begin{{tabular}}{{l|ll}}
Accuracy & {} \\\\ \\hline
Sensitivity & {} \\\\ \\hline
Specificity & {} \\\\ \\hline
Precision & {} \\\\
\\end{{tabular}}
\\caption{{{}}}
\\end{{minipage}}
\\end{{table}}
"""
TP = 999
FP = 888
TN = 777
FN = 666
run_type = "student X run Y"
cap1 = "Confusion matrix for " + run_type
cap2 = "Statistics for " + run_type
accu = 2345
sens = 5432
spec = 9894
prec = 1930

print(outstr.format(TP, FP, FN, TN, cap1, accu, sens, spec, prec, cap2))