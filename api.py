from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route('/')
def root():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=QEZobiZsyBGBhb1qBPQxdbfBWpdLHJeeZCgv2R1G')
    url = u.geturl()
    header = u.info()
    page = u.read()
    
    d = json.loads(page)

    return render_template('api.html', header = d['title'], description = d['explanation'], image = d['url'])

if __name__ == '__main__':
    app.debug = True
    app.run()
