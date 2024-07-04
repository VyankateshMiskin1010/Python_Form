from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    image_data = request.form['image_data']
    location = request.form['location']

    # Decode the base64 image data and save it as a file
    image_data = image_data.split(',')[1]
    image_data = base64.b64decode(image_data)
    image_path = os.path.join(UPLOAD_FOLDER, 'image.png')
    with open(image_path, 'wb') as fh:
        fh.write(image_data)

    return f'''
        <h1>Data Received</h1>
        <p>Name: {name}</p>
        <p>Location: {location}</p>
        <img src="/static/uploads/image.png" alt="User Image">
    '''

if __name__ == '__main__':
    app.run(debug=True)
