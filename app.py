from flask import Flask, render_template, request, jsonify
from os import environ
from data.read import read
#from data.vod import vod

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', vod=read())


@app.post('/update_vod')
def update_vod():
    vod_key = environ.get('vod_key', 'false')
    vod_request = request.get_json()['vod_key']

    if vod_key == vod_request:
        return jsonify({'return': 'success'})
    
    return jsonify({'return': 'fail'})


if __name__ == '__main__':
    run_state = environ.get('run_state', 'false')

    if run_state == 'production':
        app.run()

    else:
        app.run(debug=True)