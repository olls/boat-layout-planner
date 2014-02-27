"""
    Scale is a meter at normal scale = 1.
"""

TEMPLATES = {
    'furniture': {
        'chair-north': {
            'XML': '<chair-north x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}"                y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}"                    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+({scale}*.4)"       x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({scale}*.4)"   y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(({scale}*.4))*.8"  x2="{x}+({scale}*.4)"   y2="{y}+(({scale}*.4))*.8 " />\n')
        },
        'chair-south': {
            'XML': '<chair-south x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}"                y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}"                    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+({scale}*.4)"       x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({scale}*.4)"   y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(({scale}*.4))*.2"  x2="{x}+({scale}*.4)"   y2="{y}+(({scale}*.4))*.2 " />\n')
        },
        'chair-east': {
            'XML': '<chair-east x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                    y1="{y}"                x2="{x}"                    y2="{y}+({scale}*.4)"   />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                    y1="{y}"                x2="{x}+({scale}*.4)"       y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                    y1="{y}+({scale}*.4)"   x2="{x}+({scale}*.4)"       y2="{y}+({scale}*.4)"   />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({scale}*.4)"       y1="{y}"                x2="{x}+({scale}*.4)"       y2="{y}+({scale}*.4)"   />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(({scale}*.4))*.2"  y1="{y}"                x2="{x}+(({scale}*.4))*.2"  y2="{y}+({scale}*.4)"   />\n')
        },
        'chair-west': {
            'XML': '<chair-west x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}"                y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}"                    />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+({scale}*.4)"       x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+({scale}*.4)"   y1="{y}"                    x2="{x}+({scale}*.4)"   y2="{y}+({scale}*.4)"       />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(({scale}*.4))*.8"                y1="{y}"  x2="{x}+(({scale}*.4))*.8"   y2="{y}+({scale}*.4)" />\n')
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

        'one-segment-sofa-south': {
            'XML': '<one-segment-sofa-south x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.4*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.4*{scale})"  y2="{y}+(0.5*{scale})"  />\n')
        },
        'two-segment-sofa-south': {
            'XML': '<two-segment-sofa-south x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+{scale}"        y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+{scale}"        y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}"                x2="{x}+{scale}"        y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+{scale}"        y2="{y}+(0.1*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.9*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Segments
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n')
        },
        'three-segment-sofa-south': {
            'XML': '<three-segment-sofa-south x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+(1.5*{scale})"  y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+(1.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(1.5*{scale})"  y1="{y}"                x2="{x}+(1.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+(1.5*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.1*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(1.4*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(1.4*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Segments
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}+(0.1*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}+(0.1*{scale})"  x2="{x}+{scale}"        y2="{y}+(0.5*{scale})"  />\n')
        },

        'one-segment-sofa-north': {
            'XML': '<one-segment-sofa-north x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.4*{scale})"  x2="{x}+(0.5*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                x2="{x}+(0.1*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.4*{scale})"  y1="{y}"                x2="{x}+(0.4*{scale})"  y2="{y}+(0.4*{scale})"  />\n')
        },
        'two-segment-sofa-north': {
            'XML': '<two-segment-sofa-north x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+{scale}"        y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+{scale}"        y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}"                x2="{x}+{scale}"        y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.4*{scale})"  x2="{x}+{scale}"        y2="{y}+(0.4*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                x2="{x}+(0.1*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.9*{scale})"  y1="{y}"                x2="{x}+(0.9*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    # Segments
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}+(0.4*{scale})"  />\n')
        },
        'three-segment-sofa-north': {
            'XML': '<three-segment-sofa-north x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+(1.5*{scale})"  y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.5*{scale})"  x2="{x}+(1.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.5*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(1.5*{scale})"  y1="{y}"                x2="{x}+(1.5*{scale})"  y2="{y}+(0.5*{scale})"  />\n'
                    # Back
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.4*{scale})"  x2="{x}+(1.5*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    # Sides
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.1*{scale})"  y1="{y}"                x2="{x}+(0.1*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(1.4*{scale})"  y1="{y}"                x2="{x}+(1.4*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    # Segments
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.5*{scale})"  y1="{y}"                x2="{x}+(0.5*{scale})"  y2="{y}+(0.4*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+{scale}"        y1="{y}"                x2="{x}+{scale}"        y2="{y}+(0.4*{scale})"  />\n')
        },

        'television-north': {
            'XML': '<television-north x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}+(0.6*{scale})"  y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.1*{scale})"  x2="{x}+(0.25*{scale})" y2="{y}+(0.13*{scale})" />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.35*{scale})" y1="{y}+(0.13*{scale})" x2="{x}+(0.6*{scale})"  y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.25*{scale})" y1="{y}+(0.13*{scale})" x2="{x}+(0.35*{scale})" y2="{y}+(0.13*{scale})" />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}"                x2="{x}"                y2="{y}+(0.1*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.6*{scale})"  y1="{y}"                x2="{x}+(0.6*{scale})"  y2="{y}+(0.1*{scale})"  />\n')
        },
        'television-south': {
            'XML': '<television-south x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />',
            'SVG': ('<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.13*{scale})" x2="{x}+(0.6*{scale})"  y2="{y}+(0.13*{scale})" />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.03*{scale})"  x2="{x}+(0.25*{scale})" y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.35*{scale})" y1="{y}"                x2="{x}+(0.6*{scale})"  y2="{y}+(0.03*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.25*{scale})" y1="{y}"                x2="{x}+(0.35*{scale})" y2="{y}"                />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}"                y1="{y}+(0.13*{scale})" x2="{x}"                y2="{y}+(0.03*{scale})"  />\n'
                    '<line  stroke="{color}"    stroke-width="1"    x1="{x}+(0.6*{scale})"  y1="{y}+(0.13*{scale})" x2="{x}+(0.6*{scale})"  y2="{y}+(0.03*{scale})"  />\n')
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
