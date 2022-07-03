# File encoding: utf8

from components.functional import html_index
from components.functional import html_output

with open("index.html", "w") as f:
    f.write(html_index.get_html())
#
# with open("output.html", "w") as f:
#     f.write(html_output.get_html())
