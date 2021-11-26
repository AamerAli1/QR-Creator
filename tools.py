import pdfkit
from jinja2 import Environment, FileSystemLoader
import tempfile
import win32print
import locale
import ghostscript
import ntplib
import datetime, time


def HTMLToPDF(input, output):
    options = {
        'encoding': 'ANSI',
        'margin-left': '5mm',
        'margin-right': '5mm',
        'margin-bottom': '3mm',
        'margin-top': '3mm',

    }
    pdfkit.from_string(input,output,options=options)
    return pdfkit.from_string(input, False)


def populate_HTML(html,dict):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(html)

    html_out = template.render(dict)

    return html_out


def toPrinter(pdf, printerName):
    # temp1 = tempfile.mktemp('.pdf')
    # f1 = open(temp1, 'ab')
    # f1.write(pdf)
    # f1.close()

    args = [
        "-dPrinted", "-dBATCH", "-dNOSAFER", "-dNOPAUSE", "-dNOPROMPT"
        "-dFIXEDMEDIA"                                             "-q",
        "-dNumCopies#1",
        "-sDEVICE#mswinpr2",
        f'-sOutputFile#"%printer%{printerName}"',
        f'"{pdf}"'
    ]

    encoding = locale.getpreferredencoding()
    args = [a.encode(encoding) for a in args]
    ghostscript.Ghostscript(*args)


def check_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        Internet_date_and_time = datetime.datetime.fromtimestamp(response.tx_time)
        print('\n')
        if Internet_date_and_time < datetime.datetime(2022,1,1):
            return True


    except OSError:
        print('\n')
        print('Internet date and time could not be reported by server.')
        print('There is no internet connection.')
        input("Press Enter to Exit")