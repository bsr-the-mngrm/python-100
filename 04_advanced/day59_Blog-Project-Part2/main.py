from flask import Flask, render_template, request
from dotenv import load_dotenv
from os import getenv
import requests
import smtplib


all_posts = requests.get('https://api.npoint.io/9e168a049320703f5f31').json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        send_message(request.form)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<post_id>')
def post_page(post_id):
    return render_template('post.html', post=all_posts[int(post_id)-1])


def send_message(form: dict):
    load_dotenv()
    host_email_addr = getenv('EMAIL_ADDRESS')
    host_email_addr_pass = getenv('EMAIL_APP_PASS')
    smtp_addr = getenv('SMTP_ADDRESS')
    smtp_port = getenv('SMTP_PORT')

    with smtplib.SMTP_SSL(host=smtp_addr, port=smtp_port) as smtp_connection:
        smtp_connection.login(user=host_email_addr, password=host_email_addr_pass)
        # SEND MESSAGE TO HOST
        smtp_connection.sendmail(
            from_addr=host_email_addr,
            to_addrs=host_email_addr,
            msg=f"Subject:Message from {form['name']}\n\n"
                f"Contact info:\n"
                f"{form['name']} | {form['email']} | {form['phone']}\n"
                f"Message:\n"
                f"{form['message']}"
        )

        # SEND VERIFICATION TO SENDER
        smtp_connection.sendmail(
            from_addr=host_email_addr,
            to_addrs=form['email'],
            msg="Subject: Successfully sent message\n\n"
                "We received your message. Thank you!"
        )


if __name__ == "__main__":
    app.run(debug=True)
