from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variables for the game
cookies = 0
cookies_per_click = 1

# Building data (name, cookies per second, cost)
buildings = [
    {"name": "Granny", "cps": 2, "cost": 5},
    {"name": "Pig Workers", "cps": 10, "cost": 10},
    {"name": "Factory", "cps": 50, "cost": 500},
    {"name": "Portal", "cps": 100, "cost": 1000},
    {"name": "SuperPortal", "cps": 1000, "cost": 5000}
]

@app.route('/')
def index():
    return render_template('index.html', cookies=cookies, cookies_per_click=cookies_per_click, buildings=buildings)

@app.route('/click')
def click():
    global cookies
    cookies += cookies_per_click
    return jsonify({"cookies": cookies})

@app.route('/buy/<int:index>')
def buy(index):
    global cookies
    global cookies_per_click
    building = buildings[index]
    if cookies >= building['cost']:
        cookies -= building['cost']
        cookies_per_click += building['cps']
        building['cost'] *= 2  # Increase the cost for the next purchase
        return jsonify({"message": f"Bought {building['name']}!", "cookies": cookies})
    else:
        return jsonify({"error": "Not enough cookies to buy this building"})

if __name__ == '__main__':
    app.run(debug=True)
