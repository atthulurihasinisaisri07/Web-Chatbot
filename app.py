from flask import Flask, render_template, request

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello"]:
        return "Hello 👋 Welcome to the Student Helpdesk!"

    elif "courses" in user_input:
        return "We offer Python, SQL, Data Science, Web Development, and Excel."

    elif "subjects" in user_input:
        return "Core subjects include Python, DBMS, Statistics, and Machine Learning."

    elif "exams" in user_input:
        return "Prepare using notes, previous question papers, and mock tests."

    elif "timetable" in user_input:
        return "Classes run from 9 AM to 4 PM, Monday to Friday."

    elif "attendance" in user_input:
        return "Students must maintain at least 75% attendance."

    elif "study" in user_input:
        return "Study daily, practice coding, revise weekly, and work on projects."

    elif "placements" in user_input:
        return (
            "Placement preparation includes:\n"
            "1. Strong basics\n"
            "2. Projects\n"
            "3. Resume building\n"
            "4. Mock interviews"
        )

    elif "contact" in user_input:
        return "Please contact the training department through email or notice board."

    elif user_input in ["bye", "exit"]:
        return "Thank you! All the best for your studies and placements 🌟"

    else:
        return "Please ask about courses, exams, placements, or study tips 😊"


@app.route("/", methods=["GET", "POST"])
def index():
    chat_history = []  # ✅ fresh chat every load

    if request.method == "POST":
        user_input = request.form["message"]
        bot_reply = get_response(user_input)

        chat_history.append(("user", user_input))
        chat_history.append(("bot", bot_reply))

    return render_template("index.html", chat_history=chat_history)


if __name__ == "__main__":
    app.run(debug=True)
