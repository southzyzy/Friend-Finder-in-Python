from flask import Flask, render_template, request, redirect, flash, session
from flask_wtf.csrf import CSRFProtect

import os
import function1 as f1
import function3 as f3
import main
import ui_v2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

csrf = CSRFProtect(app)
csrf.init_app(app)

profiles_dir = []

@app.route('/')
def index():
    if not session.get('profiles'):
        return render_template('welcome.html')

    else:
        try:
            profiles = [file for file in os.listdir(profiles_dir[0]) if
                        file.endswith(".txt")]  # list out all the profiles in profiles folder

            f1_list = f1.FUNCTION_1(profiles_dir=profiles_dir[0], files=profiles)
            df = f1_list.profilesDF(f1_list.HEADERS, f1_list.DATA)
            data_list = f3.LIKES_DISLIKES(df).temp_list

            templateData = {
                'data': data_list,  # return and pass the data to index.html
            }
            return render_template('index.html', **templateData)

        except:
            session['profiles'] = False
            flash('Session Expire')
            return redirect('/')


@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        file_path = request.form['file_path']

        if not os.path.exists(file_path):
            flash('Directory does not exist')
            return redirect('/')

        elif ui_v2.checkFile(file_path) == "False":
            flash('Profiles Directory specified is empty. Are you sure you point to the right directory?')
            return redirect('/')

        else:
            session['profiles'] = True
            profiles_dir.append(file_path)

            return redirect('/')


@app.route("/logout")
def logout():
    session['profiles'] = False
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 404 status explicitly
    return render_template('500.html'), 500