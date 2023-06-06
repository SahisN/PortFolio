from flask import Flask, render_template, request
from writer import write_to_csv
from mailbot import MailBot


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/robots.txt")
def robot_page():
    return "No Scrapping allowed"


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            send_mail(data)
            return render_template("submitted.html")
        except:
            return render_template("unsubmitted.html")
    else:
        return render_template("unsubmitted.html")


def send_mail(data):
    try:
        mailbot = MailBot(
            "apcsa2020@gmail.com",
            "You have a message from " + data["name"],
            data["message"] + "\n \n" + "contact: " + data["email"],
        )
        mailbot.send_email()
    except:
        return
