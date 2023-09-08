from flask import Flask, render_template, url_for, request

app = Flask(__name__)

import pyshorteners
import pyperclip

def shortenit(longurl):
    s = pyshorteners.Shortener()
    url = longurl;
    shorturl= s.tinyurl.short(url)
    return shorturl

def convert(longurl):
    if ' ' in longurl:
        return "Remove spaces from URL 🥲"
    if len(longurl)==0:
        return "URL Box is blank 😒"
    x = shortenit(longurl)
    pyperclip.copy(x)
    spam = pyperclip.paste()
    return x


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():

    longurl = request.form.to_dict()
    
    name = longurl["name"]
    shorturl = convert(name)

    return render_template('index.html', name = shorturl)


if __name__ == "__main__":
    app.run(debug=True)