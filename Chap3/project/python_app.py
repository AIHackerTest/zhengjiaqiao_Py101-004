import weather_api
from flask import Flask, request, render_template
app = Flask(__name__)
query_history = []

@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def weather():
    if request.form['button'] == 'query':
        try:
            location = request.form['location'].strip()
            city,temperature,weather,time = weather_api.fetchweather(location)
            record={'location':location, 'city':city, 'temperature':temperature, 'weather':weather,'time':time}
            query_history.append(record)
            return render_template('home.html',**record)
        except:
            return render_template('home.html', location = location, error = True)
    elif request.form['button'] == 'history':
        return render_template('home.html',history = query_history )
    else:
        return render_template('home.html',help = True)


if __name__ == '__main__':
    app.run()
