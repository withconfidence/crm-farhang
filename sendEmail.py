## credits: http://linuxcursor.com/python-programming/06-how-to-send-pdf-ppt-attachment-with-html-body-in-python-script
from socket import gethostname
# import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import dataModel


print(dataModel.data_model.total)

def send_email_pdf_figs(path_to_pdf, clintName,email):


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    if True:
        # config = json.load(f)
        server.login('360crm0@gmail.com', 'fimcagakyczitkoc')
        # Craft message (obj)
        msg = MIMEMultipart()

        with open("message.txt","r") as f:
            message=f.read().replace("[Name]",clintName)
        msg['Subject'] = f'{clintName} your Inovice'
        msg['From'] = '360crm0@gmail.com'
        msg['To'] = email
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        with open(path_to_pdf, "rb") as f:
            #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
            attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
        msg.attach(attach)
        # send msg
        server.send_message(msg)


def send_email_schedule(message, clintName,email):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    if True:
        # config = json.load(f)
        server.login('360crm0@gmail.com', 'fimcagakyczitkoc')
        # Craft message (obj)
        msg = MIMEMultipart()

        # with open("message.txt","r") as f:
        #     message=f.read().replace("[Name]",clintName)
        # message = f"""Dear {clintName}

        # """
        msg['Subject'] = f'{clintName} Meeting'
        msg['From'] = '360crm0@gmail.com'
        msg['To'] = email
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # # Attach the pdf to the msg going by e-mail
        # with open(path_to_pdf, "rb") as f:
        #     #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
        #     attach = MIMEApplication(f.read(),_subtype="pdf")
        # attach.add_header('Content-Disposition','attachment',filename=str(path_to_pdf))
        # msg.attach(attach)
        # send msg
        server.send_message(msg)