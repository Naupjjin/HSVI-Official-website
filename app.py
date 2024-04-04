from flask import Flask, render_template
from news.newssystem import app_route as newssystem
from __init__ import alert_now,index_shownews_n 
from main.db import db


app = Flask(__name__)
app.register_blueprint(newssystem)



@app.route('/')
def index():
    _announce = db.load_news(index_shownews_n)
    return render_template('index.html' ,announcements = _announce) #alert_now = alert_now

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/work_with_us')
def rounded():
    return render_template('wantyou.html')

@app.route('/explainVtuber')
def explainVtuber():
    return render_template('whatv.html')

@app.errorhandler(404)
def erro404(e):
    return render_template('404.html'),404



if __name__=="__main__":
    app.run(host='0.0.0.0', port=80,debug=True) #