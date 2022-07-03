# File encoding: utf8

from flask import url_for


def get_html(body_extends):
    html = '''
        <!doctype html>
        <html>
            <head>
                <title>test_by_smile</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>Just test</h1>
                <br>
                <br>
                <br>
                {body_extends}<br>
                <br>
                <br>
                <br>
                <h2>Thank you for your attention.</h2>
            </body>
        </html>
        '''.format(
        body_extends=body_extends
    )

    return html
