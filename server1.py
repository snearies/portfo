from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__, template_folder='template')

#print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar= '"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
          data = request.form.to_dict()
       # data = request.args.to_dict()
       # print(data)                         ------------remove this while writing to file and add below
       # write_to_file(data)                 ----------------------for database.txt
          write_to_csv(data)                  #-----------------for csv
          return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'try again'



# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/work.html")
# def work():
#     return render_template('work.html')
#
# @app.route("/works.html")
# def works():
    #return render_template('works.html')


# @app.route("/favicon.ico")
# def blog():
#     return "<p>welcome to my blog!</p>"

# @app.route("/blog/2021/dogs")
# def blog2():
#     return "<p>this is my dog</p>"


if __name__=='__main__':
    app.run(debug=True)

#print(dir(Flask))


#----------------------------------STEPS VENV
# ------------to
# a venv
# command in terminal (first change directory)
# python -m venv venv

#---------------go one step back cd ..
# to make the current directory as venv ( adds include,lib,scripts)
#python -m venv web-server/
#now delete the venv

#-----------------to activate
#web-server\Scripts\activate


#-------------------------------------------------------execution stpes--------------
# set FLASK_APP=server.py

#this works  ----------------------make sure to pip install flask

#python -m flask run

# to set debug mode
# set FLASK_ENV=development


#---------------------------------for render template,add template_folder='template'


