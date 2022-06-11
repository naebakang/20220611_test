# File encoding: utf8

from component.html_factory import Base

ins_base = Base()
with open("index.html", "w") as f:
    f.write(ins_base.get_html())
