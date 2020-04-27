import os
import psycopg2
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from tempfile import mkdtemp
import sqlite3
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from random import randint
from smtplib import SMTP_SSL as SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from helpers import apology, login_required
# Configure application
app = Flask(__name__)
app.secret_key = "secret_key"
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
@app.route('/home', methods=['GET','POST'])
@app.route("/")
@login_required
def home():
    return render_template("index.html", name = session["name"])

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method=="POST":
        if not request.form.get("f_name"):
            return apology("What's your first name? A shortened form, such as Nick instead of Nicholas, is acceptable.")
        f_name = request.form.get("f_name")
        if not request.form.get("l_name"):
            return apology("What's your last name?")
        l_name = request.form.get("l_name")
        if not request.form.get("email"):
            return apology("What's your email? You need it to be able to register into this event.")
        elif (request.form.get("email")).find("@abschools.org", 0, len(request.form.get("email"))) == -1 or (request.form.get("email")).find("20", 0, len(request.form.get("email"))) == -1:
            return apology("Please use your abschools.org email if you're a senior or sign up with another email as an attendee")
        email = request.form.get("email")
        session["email"] = request.form.get("email")
        session["name"] = f_name
        return redirect("/")
    return render_template("register.html")
if __name__ == "__main__":
    app.run(debug=True)
