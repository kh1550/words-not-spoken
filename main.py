# Kristin Ho
# CSCI-UA.380 Python for Applications
#
# Visual Novel Final Project
#
from flask import Flask, render_template, request, redirect, jsonify
from novel import *
import csv
app = Flask(__name__)
app.debug = True

# SETUP STUFF
# Needs to be independent for each user
act = 1
scene = 1
line_count = 0
chars = []
init = False
p = Play()

def initialize():
    def characters(file_name):
        try:
            f = open(file_name, 'r')
            f.readline()
            cf = csv.reader(f, delimiter=",", quotechar='"')
            for line in cf:
                c = Character()
                c.load(line)
                chars.append(c)
        except IOError as e:
                print('{}: {}'.format(e.__class__.__name__, "Invalid file name"))
    def load(file_name):
        try:
            f = open(file_name, 'r')
            f.readline()
            cf = csv.reader(f, delimiter=",", quotechar='"')
            for line in cf:
                s = Scene()
                s.load(line,chars)
                p.append(s)
        except IOError as e:
                print('{}: {}'.format(e.__class__.__name__, "Invalid file name"))
    characters("chars.csv")
    load("text.csv")

# FLASK STUFF
@app.route('/')
def index():
    global init
    if not init:
        initialize()
        init = True
    p.pointer = 0
    return render_template("index.html")

@app.route('/play', methods=['GET', 'POST'])
def projects():
    if request.method == 'GET':
        chara = ''
        path = ''
        line = ''
        spkr = ''
        color = "false"
        if (len(p.scenes) > 0):
            s = next(p)
            chara = s.speakerImg()
            path = s.bg
            line = s.line
            spkr = s.spkrobj.label()
            color = s.isColor()
            return render_template("novel.html", color=color, chara=chara, path=path, line=line, spkr=spkr)
        else:
            return redirect('/')
    elif request.method == 'POST':
        return redirect('/play')

@app.route('/progress', methods=['POST'])
def progress():
    result = [c.full() for c in chars if int(c.friend) > 0]
    if (len(result) == 0):
        result = ["None"]
    return jsonify(list=result)

app.run()