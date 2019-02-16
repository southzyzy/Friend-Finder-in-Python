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
name_list = []
main_class = {}

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

            m_class = main.MAIN(df) # Create the main class method
            main_class['m_class'] = m_class # store it in memory so can be accessible throughout

            data_list = f3.LIKES_DISLIKES(df).temp_list

            female_list = [val['Name'].replace(' ', '') for val in data_list if val['Gender'] == 'F']
            male_list = [val['Name'].replace(' ', '') for val in data_list if val['Gender'] == 'M']

            for val in data_list:
                if val not in name_list:
                    name_list.append(val['Name'])

            templateData = {
                'data': data_list,  # return and pass the data to index.html
                'female_list': female_list,
                'male_list': male_list
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


@app.route('/functions')
def functions():
    if not session.get('profiles'):
        return render_template('welcome.html')
    else:
        if name_list == []:
            session['profiles'] = False
            flash('Session Expire')
            return redirect('/')
        else:
            templateData = {
                'name_list': name_list
            }
            return render_template('functions.html', **templateData)


@app.route('/result', methods=["GET", "POST"])
def handle_functions():
    if not session.get('profiles'):
        return render_template('welcome.html')

    else:
        if request.method == 'POST':
            option = request.form['option']
            sb_name = request.form['name']

            # get the m_class Class
            m_class = main_class.get('m_class')

            """ This part get student B info """
            sb_df = m_class.student_B(sb_name)

            f2_df = m_class.function2(sb_df, sb_name)
            if option == '2':
                print "Run function 2"
                """ This part serves function 2 """
                f2_list = f3.LIKES_DISLIKES(f2_df).temp_list

                templateData = {
                    'name' : sb_name,
                    'data' : f2_list
                }

                return render_template("results.html", **templateData)

            """ This part serves function 3 """
            f3_class = f3.LIKES_DISLIKES(f2_df)  # calling the class LIKES_DISLIKES
            f3_temp_profiles_list = f3_class.temp_list  # converting dataframe to list

            f3_df = m_class.function3(f3_class, f3_temp_profiles_list, sb_df)

            if option == '3':
                print "Run function 3"
                f3_list = f3.LIKES_DISLIKES(f3_df).temp_list
                templateData = {
                    'name' : sb_name,
                    'data' : f3_list
                }

                return render_template("results.html", **templateData)


@app.route('/home', methods=["GET", "POST"])
def api_key():
    if not session.get('profiles'):
        return render_template('welcome.html')

    if request.method == 'POST':
        file_path = request.form['file_path']


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