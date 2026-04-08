from flask_mail import Mail, Message


def configure_mail(app):

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'thamaraiselvan112005@gmail.com'
    app.config['MAIL_PASSWORD'] = 'hkvf apxi ltpa lcpb'

    mail = Mail(app)

    return mail


def send_alert_email(mail, sender_email, receiver_email,
                     original_username, new_username):

    try:

        msg = Message(
            subject="Security Alert: Similar Username Detected",
            sender=sender_email,
            recipients=[receiver_email]
        )

        msg.body = f"""
Hello {original_username},

A new account with username '{new_username}'
similar to your username has been detected.

If this was not you, please take action immediately.

Fake Profile Detection System
"""

        mail.send(msg)

        print("Alert email sent successfully")

    except Exception as e:

        print("Email sending failed:", e)