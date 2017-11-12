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

@app.route('/weather')
def weather():
    u = urllib2.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22chicago%2C%20il%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    url = u.geturl
    header = u.info()
    page = u.read()

    d = json.loads(page)
    wind_dict = d['query']['results']['channel']['wind']
    
    return render_template('weather.html', header = 'Wind\n', description = 'Chill: ' + wind_dict['chill'] + '\nDirection: ' + wind_dict['direction'] + '\nSpeed: ' + wind_dict['speed'] + '\n')

if __name__ == '__main__':
    app.debug = True
    app.run()
