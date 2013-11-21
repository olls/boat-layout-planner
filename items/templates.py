TEMPLATES = {
    'furniture': {
        'chair': {
            'XML': '<chair x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />', 
            'SVG': '<line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2="{x}" y2="{y}+({scale}*100)" /><line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2=" {x}+({scale}*100) " y2="{y}" /><line stroke="#000000" stroke-width="1" x1="{x}" y1=" {y}+({scale}*100) " x2=" {x}+({scale}*100) " y2=" {y}+({scale}*100) " /><line stroke="#000000" stroke-width="1" x1=" {x}+({scale}*100) " y1="{y}" x2=" {x}+({scale}*100) " y2=" {y}+({scale}*100) " /><line stroke="#000000" stroke-width="1" x1=" {x}" y1=" {y}+(({scale}*100))*.2 " x2=" {x}+({scale}*100) " y2=" {y}+(({scale}*100))*.2 " />'
        }
    },
    'other': {
        'boat': {
            'XML': '<boat length="{length}" color="{color}" description="{description}" author="{author}" />',
            'SVG': '<line stroke="#000000" stroke-width="1" x1="{x}+{bow}" y1="{y}" x2="{x}+{length}" y2="{y}" id="svg_1"/><line stroke="#000000" stroke-width="1" x1="{x}+{bow}" y1="{y}+{width}" x2="{x}+{length}" y2="{y}+{width}" /><line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}+({width}/2)" x2="{x}+{bow}" y2="{y}" /><line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}+({width}/2)" x2="{x}+{bow}" y2="{y}+{width}" /><line stroke="#000000" stroke-width="1" x1="{x}+{length}" y1="{y}" x2="{x}+{length}" y2="{y}+{width}" />'
        },
        'wall': {
            'XML': '',
            'SVG': ''
        }
    }
}