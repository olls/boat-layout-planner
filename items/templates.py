"""
    Scale is in Meters.
"""

TEMPLATES = {
    'furniture': {
        'chair': {
            'XML': '<chair x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}"                y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}"                    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+({scale}*.4)"       x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({scale}*.4)"   y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(({scale}*.4))*.2"  x2="{x}+({scale}*.4)"   y2="{y}+(({scale}*.4))*.2 " />\n')
        },
        'table': {
            'XML': '<table x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+{scale}"        />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}"                x2="{x}+{scale}"        y2="{y}+{scale}"        />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+{scale}"        y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+{scale}"        x2="{x}+{scale}"        y2="{y}+{scale}"        />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                x2="{x}+(0.1*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}"                x2="{x}+(0.9*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}+(0.1*{scale})"  x2="{x}+(0.9*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}+{scale}"        x2="{x}+(0.1*{scale})"  y2="{y}+(0.9*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.9*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.9*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}+{scale}"        x2="{x}+(0.9*{scale})"  y2="{y}+(0.9*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}+(0.9*{scale})"  x2="{x}+(0.9*{scale})"  y2="{y}+(0.9*{scale})"  />\n')
        },
        'wall': {
            'XML': '<wall x="{x}" y="{y}" doorY="{doorY}" doorWidth="{doorWidth}" scale="{scale}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                        x2="{x}"                y2="{y}+{boatWidth}"            />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                        x2="{x}+(0.1*{scale})"  y2="{y}+{boatWidth}"            />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+{doorY}"                x2="{x}+(0.1*{scale})"  y2="{y}+{doorY}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+{doorY}+{doorWidth}"    x2="{x}+(0.1*{scale})"  y2="{y}+{doorY}+{doorWidth}"    />\n')
        }
    },
    'other': {
        'boat': {
            'XML': '<boat length="{length}" width="{width}" height="{height}" wallWidth="{wallWidth}" bow="{bow}" stern="{stern}" color="{color}" description="{description}" author="{author}">',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}"                        x2="{x}+{length}"                       y2="{y}"                        />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{wallWidth}"            x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{wallWidth}"            />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}+{width}"                x2="{x}+{length}"                       y2="{y}+{width}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{width}-{wallWidth}"    x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{width}-{wallWidth}"    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                                y1="{y}+(0.5*{width})"          x2="{x}+{bow}"                          y2="{y}"                        />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                                y1="{y}+(0.5*{width})"          x2="{x}+{bow}"                          y2="{y}+{width}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({length}-{stern})"             y1="{y}"                        x2="{x}+({length}-{stern})"             y2="{y}+{width}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{length}-{stern}-{wallWidth}"   y1="{y}+{wallWidth}"            x2="{x}+{length}-{stern}-{wallWidth}"   y2="{y}+{width}-{wallWidth}"    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}"                          y1="{y}"                        x2="{x}+{bow}"                          y2="{y}+{width}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{bow}+{wallWidth}"              y1="{y}+{wallWidth}"            x2="{x}+{bow}+{wallWidth}"              y2="{y}+{width}-{wallWidth}"    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{length}"                       y1="{y}"                        x2="{x}+{length}"                       y2="{y}+{width}"                />\n')
        }
    }
}
