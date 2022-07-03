# File encoding: utf8

# from flask import Blueprint, flash, redirect, request, url_for
from components.functional import html_base

# output = Blueprint('output', __name__, url_prefix='/output/')
#
#
# @output.route('/', methods=['GET', 'POST'])
def get_html():
    if request.method == 'POST':
        data = request.form

        # check if the post request has the file part
        # if "input_txt" not in data:
        #     flash('No file part')
        #     return redirect(url_for('index'))

        contents = data["input_txt"]
        path_file = r'components/static/input_txt.txt'
        with open(path_file, "w") as f:
            f.write(contents)

        # image = request.files['image']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        # if image.filename == '':
        #     flash('No selected file')
        #     return redirect(url_for('index'))
        #
        # _, extension = os.path.splitext(image.filename)
        # path_file = r'components/static/' + 'input_user' + str(extension)
        # image.save(path_file)
        # if image and allowed_file(image.filename):
        #     filename = secure_filename(image.filename)
        #     ins_env_directory = Directory()
        #     shutil.copy2(src=path_file, dst=ins_env_directory.upload + filename)
        #
        #     ins_yolov4 = YOLOv4()
        #     ins_yolov4.create_image_of_object_detection(file_name=filename)

            # 이건 필요 없는 2줄인데?
            # path_file = r'component/static/' + 'output.jpeg'
            # image.save(path_file)

            # file_list = os.listdir('component/static/')
            # for i in file_list:
            #     if 'output' in i:
            #         aa = i
            #         break
            #
            # path_txt_file = 'component/static/output.txt'
            # with open(path_txt_file, 'r') as rb:
            #     txt = rb.readlines()
            #     content = ''
            #     for i in txt:
            #         content = content + i + '<br>'

            body_extends = '''
                        <h2>Success</h2>
                        <br>
                        <br>
                        '''.format(
                )

            html = html_base.get_html(body_extends=body_extends)

            return html

    else:
        return redirect(url_for('index'))
