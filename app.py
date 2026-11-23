from flask import Flask, render_template, request, jsonify
from os import environ
from data.read import read

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', vod=read())


@app.post('/update_vod')
def update_vod():
    return jsonify({'return': 'success'})


if __name__ == '__main__':
    run_state = environ.get('run_state', 'false')

    if run_state == 'production':
        app.run()

    else:
        app.run(debug=True)