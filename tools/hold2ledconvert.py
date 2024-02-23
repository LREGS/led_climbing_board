"""Manual mapping of the led numbers to the hold numbers within pyside - this is vital for telling neopixel which leds it needs to illuminate"""

def routeToLeds(route):
    conversion =  {
    1:1, 
    2:4,
    11:10,
    10:7,
    13:12,
    12:15,
    24:19,
    23:21,
    27:23,
    25:27,
    37:29,
    26:32,
    36:34,
    38:37,
    52:39,
    39:41,
    40:43,
    51:45,
    53:47,
    50:53,
    54:55,
    48:60,
    49:57,
    41:51,
    42:150,
    43:148,
    44:146,
    33:144,
    34:141,
    29:136,
    21:126,
    20:134,
    56:133,
    19:130,
    15:118,
    14:121,
    22:124,
    48:58,
    47:62,
    55:66,
    46:69,
    45:72,
    31:75,
    32:77,
    18:80,
    30:82,
    17:87,
    16:90,
    8:92,
    7:96,
    6:100,
    5:103,
    9:106,
    4:109,
    3:112,
    28:138,
    35:139 
        }
    led_to_light = []
    for hold in route:
        print(hold)
        if hold in conversion.keys():
            led = conversion[hold]
            led_to_light.append(led)
    data = {"leds": led_to_light}
    return data