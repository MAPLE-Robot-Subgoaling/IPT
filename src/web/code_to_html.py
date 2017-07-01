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

extraneous_lines = [1,3,5]

with open(code_filename) as f:
	lines = f.readlines()
	for i in range(1, len(lines)+1):
		lines[i-1] = "[" + str(i) + "] " + lines[i-1].strip("\n").replace("\t","&emsp;"*4) + "<br>"
		if i in extraneous_lines:
			lines[i-1] = "<mark>{}</mark>".format(lines[i-1])


output_html = output_html.format("\n".join(lines))
output_file.write(output_html)