from flask import Flask, render_template, request, redirect, url_for
import random
import os

port = int(os.environ.get('PORT', 5000))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)


app = Flask(__name__)

# Санасан тоо хадгалах
secret_number = random.randint(1, 10)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess_number", methods=["GET", "POST"])
def guess_number():
    global secret_number
    message = ""
    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == secret_number:
            message = "🎉 Зөв таалаа! Дахин эхлэх үү?"
            secret_number = random.randint(1, 10)
        elif guess < secret_number:
            message = "🔼 Их тоо оруул!"
        else:
            message = "🔽 Бага тоо оруул!"
    return render_template("guess_number.html", message=message)

@app.route("/rps", methods=["GET", "POST"])
def rps():
    result = ""
    choices = ["чулуу", "даавуу", "хайч"]
    if request.method == "POST":
        user = request.form["choice"]
        computer = random.choice(choices)
        if user == computer:
            result = "⚖️ Тэнцлээ!"
        elif (user == "чулуу" and computer == "хайч") or (user == "даавуу" and computer == "чулуу") or (user == "хайч" and computer == "даавуу"):
            result = f"🎉 Та яллаа! Компьютер: {computer}"
        else:
            result = f"😢 Та хожигдлоо! Компьютер: {computer}"
    return render_template("rps.html", result=result)

@app.route("/image_guess", methods=["GET", "POST"])
def image_guess():
    answer = "нартай"
    message = ""
    if request.method == "POST":
        guess = request.form["guess"].lower()
        if guess == answer:
            message = "✅ Браво! Зөв!"
        else:
            message = "❌ Буруу! Дахиад оролдоорой."
    return render_template("image_guess.html", message=message)

@app.route("/fibonacci", methods=["GET", "POST"])
def fibonacci():
    correct = False
    message = ""
    a, b = 5, 8  # 5, 8 => дараагийн тоо нь 13
    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == a + b:
            message = "✅ Зөв!"
        else:
            message = f"❌ Буруу! Зөв хариулт нь {a + b} байсан."
    return render_template("fibonacci.html", message=message, a=a, b=b)

@app.route("/maze")
def maze():
    return render_template("maze.html")

if __name__ == "__main__":
    app.run(debug=True)
