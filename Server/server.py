from flask import Flask, request
import board 
import neopixel

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p> hi </p>"



@app.route('/processRoute', methods=['POST'])
def processroute():
    request_data = request.json
    illuminate_route(request_data['middle holds'])
    return "<p> s </p>" 

def printData(data):
    print(data['middle holds'])

def illuminate_route(route):
    pixels = neopixel.NeoPixel(board.D18, 150, brightness = 1)
    route_to_led_conversion = []
    for hold in route:
        route_to_led_conversion.append(pixels[route])
    for pixel in route_to_led_conversion:
        pixel = (0,225,0)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8090)
