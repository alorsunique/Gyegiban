from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    current_time = datetime.now().strftime('%H:%M')
    return render_template('index.html', current_time = current_time)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=2048, debug=True)