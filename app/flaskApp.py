import flask
from body import Body
from enums import Starclass, PlanetType, AtmossphericComposition, VolcanismType, BioType
from input import Input
from main import get_possible_biologicals, get_most_valuable_biologicals, get_least_valuable_biologicals, get_total_value

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    jsonBody = []
    leastValue = []
    mostValue = []
    sortedAllPossible = []
    totalLeast = -1
    totalMost = -1
    error = ''
    if flask.request.method == 'POST':
        try:
            bioCount = int(flask.request.form.get('bioCount'))
            starclass = Starclass[(flask.request.form.get('starclass'))]
            planetType = PlanetType[(flask.request.form.get('planetType'))]
            atmossphericComposition = AtmossphericComposition[(flask.request.form.get('atmossphericComposition'))]
            volcanismType = VolcanismType[(flask.request.form.get('volcanismType'))]
            atmossphericPressure = float(flask.request.form.get('atmossphericPressure'))
            gravity = float(flask.request.form.get('gravity'))
            minTemp = int(flask.request.form.get('minTemp'))
            maxTemp = int(flask.request.form.get('maxTemp'))

            
            body = Body('', 0, '', 0, bioCount, starclass, planetType, atmossphericComposition, volcanismType, atmossphericPressure, gravity, minTemp, maxTemp)

            all_bio = Input.read_biologicals("app\\biologicals")


            jsonBody = body.to_json()
            leastValue = get_least_valuable_biologicals(body, all_bio)
            mostValue = get_most_valuable_biologicals(body, all_bio)
            allPossible = get_possible_biologicals(body, all_bio)

            totalLeast = f"{get_total_value(body, leastValue):,}".replace(",",".")
            totalMost = f"{get_total_value(body, mostValue):,}".replace(",",".")

            sortedAllPossible = sorted(allPossible, key= lambda x: x.value)
            sortedAllPossible.reverse()
        except ValueError as e:
            error = 'You entered a wrong value, please try again'
    return flask.render_template('index.html', 
                                    error = error,
                                    totalLeast = totalLeast, totalMost=totalMost, 
                                    jsonBody = jsonBody, 
                                    leastValue = leastValue, mostValue = mostValue, 
                                    allPossible = sortedAllPossible)


if __name__ == '__main__':
    app.run(debug=True)
