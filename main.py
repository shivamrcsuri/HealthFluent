from flask import Flask, render_template, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired




app = Flask(__name__)

app.config["SECRET_KEY"] = "fsediwq3e78fwshdore"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 405
app.config['MAIL_USERNAME'] = 'healthfluent123@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

s = URLSafeTimedSerializer('secret_key')


@app.route("/", methods=['GET', 'POST'])
def home():
  return render_template("index.html")
def index():
    if request.method == "GET":
        return '<input type="email" class="form-control" name="email" id="email" placeholder="Your Email" required><button class="btn btn-primary" type="submit">Make an Appointment</button>'

    
    email = request.form['email']
    token = s.dumps(email, salt='email-confirm')
    msg = Message('Confirm Appointment', sender="healthfluent123@gmail.com", recipients=[email])

    link = url_for("confirm_email", token=token, _external=True)
    msg.body = "You have booked an appointment with Health Fluent for (date) (location) (cause)!"
    mail.send(msg)
    
@app.route('/confirm_email/<token>')
def confirm_email(token):
    email = s.loads(token, salt='email-confirm', max_age=360)
        
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)