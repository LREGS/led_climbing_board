

import os

root_dir = '/home/william/Desktop/led_climbing_board'
sources = 'SOURCES ='

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.py'):
            sources += f'\n\t{os.path.join(dirpath, filename)} \\'

print(sources)