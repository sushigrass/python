from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup

#create figure
f=figure(x_range=(0,11),y_range=(0,11))

#create ColumnDataSource
source=ColumnDataSource(dict(x=[],y=[]))

#create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)

def extract_value():
    r=requests.get("https://www.quadrigacx.com/",headers={'User-Agent':'Mozilla/5.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    value_raw=soup.find_all("li")
    price = value_raw[0].strong.text
    return price

def update():
    new_data=dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data,rollover=15)
    print(source.data)
