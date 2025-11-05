from flask import Flask, request, render_template_string
import smtplib
import os

app = Flask(__name__)

@app.route("/")
def form():
    return render_template_string('''
        <form action="/send" method="post">
          <input name="name" placeholder="Your name" required><br>
          <input name="email" placeholder="Your email" required><br>
          <textarea name="message" placeholder="Your message" required></textarea><br>
          <button type="submit">Send</button>
        </form>
    ''')

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # send the email
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
    server.sendmail(
        os.environ["EMAIL_USER"],
        os.environ["EMAIL_USER"],
        f"Subject: New message from {name}\n\nFrom: {email}\n\n{message}"
    )
    server.quit()
    return "Message sent! Thanks for reaching out."

if __name__ == "__main__":
    app.run(debug=True)
