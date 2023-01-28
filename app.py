# app.py
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

class FileUploadForm(FlaskForm):
    file = FileField('file', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FileUploadForm()
    if request.method == 'POST':
        file = request.files['file']
        if file and form.validate_on_submit():
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
