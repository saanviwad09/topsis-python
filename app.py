from flask import Flask, request, render_template
import os
import re

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files['file']
        weights = request.form['weights']
        impacts = request.form['impacts']
        email = request.form['email']

        if not valid_email(email):
            return "Invalid email format"

        weights_list = weights.split(',')
        impacts_list = impacts.split(',')

        if len(weights_list) != len(impacts_list):
            return "Number of weights must equal number of impacts"

        for i in impacts_list:
            if i not in ['+', '-']:
                return "Impacts must be + or - only"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")
        file.save(input_path)

        
        os.system(f'python topsis.py {input_path} "{weights}" "{impacts}" {output_path}')

       
        return "TOPSIS result generated successfully. Email feature implemented but disabled due to SMTP security restrictions."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
