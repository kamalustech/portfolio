from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')
    #print(url_for('static',filename = 'favicon.ico'))
    #return render_template('index.html',name = username,post_id = post_id )
    #return "<p>Hello, Niralya and Nithila</p>"

@app.route('/<string:page_number>')
def navigate(page_number):
    return render_template(page_number)

def write_to_file(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    with open('database.txt',mode = 'a') as database:
        database.write(f'\n{email}, {subject}, {message}')
    database.close()

def write_to_csv(data):
    with open('database.csv', mode= 'a', newline = '') as database2:
        email = data['email']
        subject= data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
    database2.close()

@app.route('/submit_form1', methods= ['POST', 'GET'])
def submit_form1():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_email = request.form["email"]
        data_message = request.form["message"]
        data_subject = request.form["subject"]
        write_to_csv(data)
        data1 = str(data)
        print(data1)
        with open('hello.txt', mode = 'a') as my_file:
            my_file.write('\n')
            text = my_file.write(data1)
        my_file.close()
        return  redirect('/thankyou.html')
    else:
        return "something was returned"
    return "Hi Form submitted"



"""
@app.route('/favicon.ico')
def favicon_ico():
    return ':)'


@app.route("/works.html")
def works_html():
    return render_template('works.html')

@app.route("/about.html")
def about_html():
    return render_template("about.html")


@app.route("/contact.html")
def contact_html():
    return render_template("contact.html")

"""


"""
@app.route("/blog")
def my_blog():
    return "<p>This is Kamal's blog</p>"

@app.route("/about")
def about():
    return render_template("about.html")

"""

