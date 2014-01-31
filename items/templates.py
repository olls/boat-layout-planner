"""
    Scale is in Meters.
"""

TEMPLATES = {
    'furniture': {
        'chair': {
            'XML': '<chair x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}"                y2="{y}+({scale}*.4)"       />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}"                    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+({scale}*.4)"       x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+({scale}*.4)"   y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+(({scale}*.4))*.2"  x2="{x}+({scale}*.4)"   y2="{y}+(({scale}*.4))*.2 " />')
        },
        'table': {
            'XML': '<table x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+{scale}"        />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}"                x2="{x}+{scale}"        y2="{y}+{scale}"        />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+{scale}"        y2="{y}"                />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+{scale}"        x2="{x}+{scale}"        y2="{y}+{scale}"        />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                x2="{x}+(0.1*{scale})"  y2="{y}+(0.1*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.1*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}"                x2="{x}+(0.9*{scale})"  y2="{y}+(0.1*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}+(0.1*{scale})"  x2="{x}+(0.9*{scale})"  y2="{y}+(0.1*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}+{scale}"        x2="{x}+(0.1*{scale})"  y2="{y}+(0.9*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+(0.9*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.9*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}+{scale}"        x2="{x}+(0.9*{scale})"  y2="{y}+(0.9*{scale})"  />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}+(0.9*{scale})"  x2="{x}+(0.9*{scale})"  y2="{y}+(0.9*{scale})"  />')
        },
        'wall': {
            'XML': '<wall x="{x}" doorY="{doorY}" color="{color}" description="{description}" />',
            'SVG': ('<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}"    x2="{x}"                y2="{y}+{boatWidth}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"    x2="{x}+(0.1*{scale})"  y2="{y}+{boatWidth}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+{doorY}"    x2="{x}+(0.1*{scale})"  y2="{y}+{doorY}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                y1="{y}+{doorY}+{doorWidth}"    x2="{x}+(0.1*{scale})"  y2="{y}+{doorY}+{doorWidth}"    />')
        }
    },
    'other': {
        'boat': {
            'XML': '<boat length="{length}" width="{width}" height="{height}" wallWidth="{wallWidth}" bow="{bow}" stern="{stern}" color="{color}" description="{description}" author="{author}">',
            'SVG': ('<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}"                        x2="{x}+{length}"                       y2="{y}"                        />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{wallWidth}"            x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{wallWidth}"            />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}+{width}"                x2="{x}+{length}"                       y2="{y}+{width}"                />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{width}-{wallWidth}"    x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{width}-{wallWidth}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                                y1="{y}+(0.5*{width})"            x2="{x}+{bow}"                          y2="{y}"                      />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}"                                y1="{y}+(0.5*{width})"            x2="{x}+{bow}"                          y2="{y}+{width}"              />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+({length}-{stern})"             y1="{y}"                        x2="{x}+({length}-{stern})"             y2="{y}+{width}"                />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{length}-{stern}-{wallWidth}"   y1="{y}+{wallWidth}"            x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{width}-{wallWidth}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}"                        x2="{x}+{bow}"                          y2="{y}+{width}"                />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{wallWidth}"            x2="{x}+{bow}+{wallWidth}"              y2="{y}+{width}-{wallWidth}"    />'
                    '<line  stroke="#000000"    stroke-width="1"    x1="{x}+{length}"                       y1="{y}"                        x2="{x}+{length}"                       y2="{y}+{width}"                />')
        }
    }
}