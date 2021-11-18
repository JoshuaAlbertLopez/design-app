from flask import Flask
from flask import request
from flask import render_template


designapp = Flask(__name__)

# Route for handling the login page logic
@designapp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    designapp.run(host="0.0.0.0", port=8000)
