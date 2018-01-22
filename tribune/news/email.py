from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,reciever):
    # creating message subject and sender
    subject = 'Welcome to the MoringaTribune NewsLetter'
    sender = 'sethkrm@gmailcom'

    # passing in thee context variables
    text_context = render_to_string('email/newsemail.txt',{"name":name})
    html_context = render_to_string('email/newsemail.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_context,sender,[reciever])
    msg.attach_alternative(html_content,'text/html')
    msg.send()