# Partially based on https://stackoverflow.com/q/72597109/2378368
from flask import Flask, abort
from output_m3u import produce_m3u

app = Flask(__name__)

@app.route('/')
def index():
    m3u = produce_m3u()
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u

@app.route('/rai1')
def rai1():
    m3u = produce_m3u(channel='rai1')
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u

@app.route('/rai2')
def rai2():
    m3u = produce_m3u(channel='rai2')
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u

@app.route('/rai3')
def rai3():
    m3u = produce_m3u(channel='rai3')
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u

@app.route('/rai4')
def rai4():
    m3u = produce_m3u(channel='rai4')
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u

@app.route('/rai5')
def rai5():
    m3u = produce_m3u(channel='rai5')
    if m3u in [403, 404]:
        abort(m3u)
    else: 
        return m3u