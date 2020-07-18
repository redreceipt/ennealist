import os

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/', methods=['GET', "POST"])
def index():
    # TODO if email is in session, go to types page
    if "email" in session.keys():
        return render_template("types.html")
    return render_template("login.html")


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    # TODO verify code
    # NOTE temp always true for debug
    verified = "code" in request.form.keys()
    if verified:
        session['email'] = email
        return redirect(url_for("index"))
    # TODO flash message that code is invalid
    return render_template("verify.html", email=request.form["email"])


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))
