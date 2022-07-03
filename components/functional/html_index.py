# File encoding: utf8

from flask import url_for

from components.functional import html_base


def get_html():
    path_file = r'components/static/input_txt.txt'
    with open(path_file, "r") as f:
        contents = f.read()
    body_extends = '''
        <h2>Input</h2>
        {}<br>
        <br>
        <br>
        <form action={} method="POST" enctype="multipart/form-data">
            <input type="text" name='input_txt'><br>
            <input type='submit' value='Get output'>
        </form>
        '''.format(
        contents,
        "output.html"
    )

    html = html_base.get_html(body_extends=body_extends)

    return html
