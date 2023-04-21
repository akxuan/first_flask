from flask import Flask, render_template, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    df = pd.read_csv(file)
    total = df.iloc[:,0].sum()
    with open('result.txt', 'w') as f:
        f.write(str(total))
    return render_template('result.html', total=total)

@app.route('/download')
def download():
    return send_file('result.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!!'

#def index():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # debug=True is for development only
'''