#
# 
# Exec: `streamlit run example/play-streamlit.py`

import streamlit as st
import streamlit.components.v1 as components

import hacka as hka

pablo= hka.Artist( hka.SupportSVG() )

st.write("Map:")

test= """<svg width="800" height="600">
<polygon points="0,0 0,600 800,600 800,0" style="fill:#ffbb55;stroke:#996633;stroke-width:10" />
<line x1="-40" y1="8" x2="240" y2="80" style="stroke:#770011;stroke-width:3"/>
<line x1="-40" y1="8" x2="240" y2="80" style="stroke:#770011;stroke-width:3"/>
<circle r="32" cx="50" cy="50" fill="none" stroke="#770011" stroke-width="3" />
<circle r="32" cx="100" cy="50" fill="#aa0011" />
<circle r="44" cx="150" cy="50" fill="#aa0011" stroke="#770011" stroke-width="8" />
<polygon points="30,130 140,130 70,200" fill="#aa0011" />
<polygon points="70,130 190,130 130,200" style="fill:#aa0011;stroke:#110000;stroke-width:4" />
<polygon points="10,10 10,590 790,590 790,10" style="fill:none;stroke:#770011;stroke-width:6" />
</svg>"""

components.html( test, 1000, 800 )