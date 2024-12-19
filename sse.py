from flask import Flask, render_template
from flask import jsonify
from flask_sse import sse
import atexit
import requests
from apscheduler.schedulers.background import BackgroundScheduler

#set up flask with SSE
app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

#set up scheduler
def schedtest():
    print("sched test")
    with app.app_context():
        sse.publish({"message":"begin"},type='bread')

sched = BackgroundScheduler()
sched.add_job(func=schedtest,trigger="interval",minutes=100,misfire_grace_time=20)
sched.start()
#Flask routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='bread')
    return "Message sent!"

@app.route('/button')
def call_bot():
    print("Got call from site")
    r = requests.get('http://127.0.0.1:8080/button')
    resp = jsonify(success=True)
    resp.status_code=200
    return resp

atexit.register(lambda:sched.shutdown())