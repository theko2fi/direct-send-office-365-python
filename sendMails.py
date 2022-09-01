import smtplib, ssl


msg = """\
Subject: Hi there

This message is sent from Python."""


def mail_me_only(message):
    port = 25  # For starttls
    smtp_server = "example-com.mail.protection.outlook.com"
    sender_email = "sender@example.com"
    receiver_email = "receiver@example.com"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.sendmail(sender_email, receiver_email, message)


mail_me_only(msg)
