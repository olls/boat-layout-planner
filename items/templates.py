"""
    Scale is in Meters.
"""

TEMPLATES = {
    'furniture': {
        'chair': {
            'XML': '<chair x="{x}" y="{y}" scale="{scale}*.3" angle="{angle}" description="{description}" color="{color}" />', 
            'SVG': '<line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2="{x}" y2="{y}+({scale}*.3)" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2=" {x}+({scale}*.3) " y2="{y}" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}" y1=" {y}+({scale}*.3) " x2=" {x}+({scale}*.3) " y2=" {y}+({scale}*.3) " />\
                    <line stroke="#000000" stroke-width="1" x1=" {x}+({scale}*.3) " y1="{y}" x2=" {x}+({scale}*.3) " y2=" {y}+({scale}*.3) " />\
                    <line stroke="#000000" stroke-width="1" x1=" {x}" y1=" {y}+(({scale}*.3))*.2 " x2=" {x}+({scale}*.3) " y2=" {y}+(({scale}*.3))*.2 " />'
        }
    },
    'other': {
        'boat': {
            'XML': '<boat length="{length}" width="{width}" bow="{bow}" stern="{stern}" color="{color}" description="{description}" author="{author}" />',
            'SVG': '<line stroke="#000000" stroke-width="1" x1="{x}+{bow}" y1="{y}" x2="{x}+{length}" y2="{y}"/>\
                    <line stroke="#000000" stroke-width="1" x1="{x}+{bow}" y1="{y}+{width}" x2="{x}+{length}" y2="{y}+{width}" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}+({width}/2)" x2="{x}+{bow}" y2="{y}" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}+({width}/2)" x2="{x}+{bow}" y2="{y}+{width}" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}+({length}-{stern})" y1="{y}" x2="{x}+({length}-{stern})" y2="{y}+{width}" />\
                    <line stroke="#000000" stroke-width="1" x1="{x}+{length}" y1="{y}" x2="{x}+{length}" y2="{y}+{width}" />'
        },
        'wall': {
            'XML': '',
            'SVG': ''
        }
    }
}