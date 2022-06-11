# File encoding: utf8

from flask import request


class Base:
    def __init__(self):
        pass

    def get_html(self):
        ip_guest = self.get_ip_guest()
        self.create_guest()

        with open('duest_all.txt', 'r') as r:
            ip = r.readlines()

        num_of_guest_all = 0
        num_of_guest_today = 0

        html = '''
        <!doctype html>
        <html>
            <head>
                <title>My tower</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>My tower</h1>
                <h2>20220102, naebakang</h2>
                <p>{}</p>
                <p>{}</p>
            </body>
        </html>
        '''.format(ip_guest, ip)

        return html

    def get_ip_guest(self):
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            if request.environ.get('HTTP_X_REAL_IP') is None:
                ip_guest = request.environ['REMOTE_ADDR']  # private ip
            else:
                ip_guest = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  # public ip
        else:
            ip_guest = request.environ['HTTP_X_FORWARDED_FOR']  # public ip

        # return ip_guest
        return 1

    def create_guest(self):
        ip_guest = self.get_ip_guest()
        with open('duest_all.txt', 'w') as w:
            w.write('\n'+str(ip_guest)+'\n')
