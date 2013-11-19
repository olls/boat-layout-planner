TEMPLATES = {
    'chair':
        {'XML': '<chair x="{x}" y="{y}" scale="{scale}" angle="{angle}" description="{description}" color="{color}" />', 
         'SVG': '<line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2="{x}" y2="{y}+({scale}*100)" />\
<line stroke="#000000" stroke-width="1" x1="{x}" y1="{y}" x2=" {x}+({scale}*100) " y2="{y}" />\
<line stroke="#000000" stroke-width="1" x1="{x}" y1=" {y}+({scale}*100) " x2=" {x}+({scale}*100) " y2=" {y}+({scale}*100) " />\
<line stroke="#000000" stroke-width="1" x1=" {x}+({scale}*100) " y1="{y}" x2=" {x}+({scale}*100) " y2=" {y}+({scale}*100) " />\
<line stroke="#000000" stroke-width="1" x1=" {x}" y1=" {y}+(({scale}*100))*.2 " x2=" {x}+({scale}*100) " y2=" {y}+(({scale}*100))*.2 " />'
        }
}