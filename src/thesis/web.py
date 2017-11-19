from flask import Flask, render_template, request, redirect, flash
import os
import new_new_thesis
from new_new_thesis import INCLUDE_EXECUTE, INCLUDE_STRUCTURE, INCLUDE_SEMANTIC

app = Flask(__name__)
UPLOAD_PATH = "/Users/mneary1/Desktop/IPT/src/thesis/uploads"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if 'file' not in request.files:
        print("no file found idk")
        return redirect(request.url)

    try:
        files = request.files.getlist("file")
        target = ''
        inputs = []
        goals = []

        for file in files:

            full_path = os.path.join(UPLOAD_PATH, file.filename)
            file.save(full_path)
            filetype = file.filename.rsplit('.', 1)[1].lower()
            if filetype == 'py':
                target = full_path
            elif filetype == 'txt' and 'input' in file.filename:
                inputs.append(full_path)
            elif filetype == 'txt' and 'goal' in file.filename:
                with open(full_path) as f:
                    for line in f:
                        goals.append(line.strip())

            else:
                print("UNKNOWN FILE TYPE:", filetype)

        extraneous_lines, src = new_new_thesis.run_thesis(target, inputs, goals)
        for i in range(1, len(src) + 1):
            src[i - 1] = "[" + str(i) + "] " + src[i - 1].strip("\n").replace("\t", "&emsp;" * 4).replace(" ", "&nbsp;") + "<br>"
            if i in extraneous_lines:
                src[i - 1] = "<mark>{}</mark>".format(src[i - 1])

        results = "\n".join(src)

        return render_template("result.html", results=results, prev=src, name=os.path.split(target)[1], execute=INCLUDE_EXECUTE, semantic=INCLUDE_SEMANTIC, structural=INCLUDE_STRUCTURE)

    except Exception as e:
        print(e)
        return render_template('index.html')

def safe_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ["py"]

if __name__ == "__main__":
    app.run(debug=True)
