from flask import Flask,render_template,abort
import json
import os
import re
app = Flask(__name__)
app.config['TEMPLATES-AUTO-RELOAD']=True
@app.route('/')
def index():
    filesname = os.listdir('/home/shiyanlou/files/')
#    filesname = re.findall('.*.json$',filesname)
    titles = []
    for filename in filesname:
        if filename[-5:] != '.json':
            continue
        with open('/home/shiyanlou/files/{}'.format(filename)) as file:
            data = json.load(file)
            title = data['title']
            titles.append(title)
    return render_template('index.html',titles = titles)

@app.route('/files/<filename>')
def file(filename):
    filesname = os.listdir('/home/shiyanlou/files/')
    filename += ".json"
#    if filename  not in filesname:
#        abort(404)
    with open('/home/shiyanlou/files/{}'.format(filename)) as file:
        data = json.load(file)
        content = data['content']
    return render_template('file.html',content = content)

@app.errorhandler(FileNotFoundError)
#@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
