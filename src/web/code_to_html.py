code_filename = "test.py"
output_file = open("templates/index.html", "w")

output_html = """<!DOCTYPE html>
<html>
<head>
	<title>extraneous code</title>
</head>
<body>
<h3>Program:</h3>
<code>
{}
</code>

</body>
</html>"""

with open(code_filename) as f:
	lines = f.readlines()
	for i in range(1, len(lines)+1):
		test = "[" + str(i) + "] " + lines[i-1].strip("\n").replace("\t","&emsp;"*4) + "<br>"
		lines[i-1] = test


output_html = output_html.format("\n".join(lines))
output_file.write(output_html)