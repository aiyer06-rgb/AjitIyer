from flask import Flask, render_template, request, flash, redirect, url_for
#from flask_mail import Mail, Message
#from dotenv import load_dotenv
#import os

# Load environment variables from .env file
#load_dotenv()

app = Flask(__name__)
#app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Configuring Flask-Mail
#app.config['MAIL_SERVER'] = 'smtp.gmail.com'
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
#app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
#app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

#mail = Mail(app)

@app.route('/')
def index():
    return render_template("home.html")

#@app.route('/send_email', methods=['POST'])
#ef send_email():
    #if request.method == "POST":
     #   name = request.form["name"]
      #  email = request.form["email"]
       # message = request.form["message"]

        #if not name or not email or not message:
         #   flash('All fields are required.')
          #  return redirect(url_for('contact'))

       # msg = Message(
        #    subject=f"New Contact Form Submission from {name}",
         #   recipients=[os.getenv('MAIL_USERNAME')],
          #  body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        #)

        #try:
         #   mail.send(msg)
          #  flash('Thank you for your message. It has been sent.')
        #except Exception as e:
         #   flash(f'There was a problem sending your message. Please try again later. Error: {str(e)}')
          #  return redirect(url_for('contact'))

        #return redirect(url_for('contact'))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

# @app.route('/blog')
# def blog():
#     return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
