import jinja2
import pdfkit
from datetime import datetime

import sendEmail
import dataModel
import os
import json

def generate(id):
    import sqlite3
    conc = sqlite3.connect(os.getcwd()+'/crm.db')
    connection = conc.cursor()
    sql = "SELECT order_.id, customer.first_name, order_.date, order_.item_id, order_.quantity, order_.price,order_.discount,customer.email from ORDER_ INNER JOIN customer on order_.customer_id = customer.id where order_.customer_id=?"

    connection.execute(sql,(id,))
    output = connection.fetchall()
    print(output)

    client_name = "Frank Andrade"
    itemList = []
    total = 0

    data = dataModel


    for i in output:
        print(i)

        data.data_model.client_name = i[1].capitalize()
        data.data_model.item_name = i[3]
        data.data_model.subtotal = i[5]
        email = i[7]
        item_dic = {
            'name': data.data_model.item_name,
            'subtotal':data.data_model.subtotal
        }
        itemList.append(item_dic)
        data.data_model.total += data.data_model.subtotal
    today_date = datetime.today().strftime("%d %b, %Y")
    month = datetime.today().strftime("%B")

    # pdf invoice content mapping
    context = {'client_name':  data.data_model.client_name, 'today_date': today_date, 'total': f'${data.data_model.total:.2f}', 'month': month,

               'items': itemList,
               }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'invoice.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf/bin/wkhtmltopdf.exe')
    output_pdf = 'invoice.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='invoice.css')


    # send email function call
    sendEmaill = sendEmail.send_email_pdf_figs("invoice.pdf",data.data_model.client_name,email)
def generate2(id):
    import sqlite3
    conc = sqlite3.connect(os.getcwd()+'/crm.db')
    connection = conc.cursor()
    sql = "SELECT order_.id, customer.first_name, order_.date, order_.item_id, order_.quantity, order_.price,order_.discount,customer.email from ORDER_ INNER JOIN customer on order_.customer_id = customer.id where order_.id=?"

    connection.execute(sql,(id,))
    output = connection.fetchall()
    print(output)

    client_name = "Frank Andrade"
    itemList = []
    total = 0

    data = dataModel


    for i in output:
        print(i)

        data.data_model.client_name = i[1].capitalize()
        data.data_model.item_name = i[3]
        data.data_model.subtotal = i[5]
        email = i[7]
        item_dic = {
            'name': data.data_model.item_name,
            'subtotal':data.data_model.subtotal
        }
        itemList.append(item_dic)
        data.data_model.total += data.data_model.subtotal
    today_date = datetime.today().strftime("%d %b, %Y")
    month = datetime.today().strftime("%B")

    # pdf invoice content mapping
    context = {'client_name':  data.data_model.client_name, 'today_date': today_date, 'total': f'${data.data_model.total:.2f}', 'month': month,

               'items': itemList,
               }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'invoice.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf/bin/wkhtmltopdf.exe')
    output_pdf = 'invoice.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config, css='invoice.css')


    # send email function call
    sendEmaill = sendEmail.send_email_pdf_figs("invoice.pdf",data.data_model.client_name,email)

# generate(1)