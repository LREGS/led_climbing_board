"""Manual mapping of the led numbers to the hold numbers within pyside - this is vital for telling neopixel which leds it needs to illuminate"""

def routeToLeds(route):
    conversion =  {
    1:1, 
    2:4,
    11:7,
    10:10,
    13:13,
    12:16,
    24:21,
    27:25,
    25:29,
    37:31,
    26:34,
    36:36,
    38:39,
    52:41,
    39:44,
    40:46,
    51:48,
    53:50,
    50:54,
    54:56,
    48:60,
    49:63,
    41:67,
    42:69,
    43:71,
    44:73,
    33:75,
    34:78,
    29:80,
    21:81,
    20:84,
    56:87,
    19:88,
    15:91,
    14:94,
    22:97
        }
    led_to_light = []
    for hold in route:
        print(hold)
        if hold in conversion.keys():
            led = conversion[hold]
            led_to_light.append(led)
    data = {"leds": led_to_light}
    return data