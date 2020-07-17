from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == 'POST':
        email = request.form["email"]
        # TODO verify code
        verified = True
        if verified:
            session['email'] = email
        else:
            # TODO do something if code is wrong
            pass
    # TODO if email is in session, go to types page
    # return render_template("types.html")
    return render_template("login.html")


@app.route('/verify', methods=["POST"])
def verify():
    return render_template("verify.html", email=request.form["email"])


@app.route('/logout')
def logout():
    # remove the email from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
