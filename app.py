from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100  # ubah cm ke meter
        bmi = weight / (height ** 2)

        # klasifikasi sederhana
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return render_template("result.html", bmi=round(bmi, 2), category=category)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
