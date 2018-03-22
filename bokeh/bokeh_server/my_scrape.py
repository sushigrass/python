from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#create figure
f=figure()

#create webscraping function
def extract_value():
    r=requests.get("https://www.quadrigacx.com/",headers={'User-Agent':'Mozilla/5.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    value_raw=soup.find_all("li")
    return value_raw[1].strong.text.split("X",1)[0]


#create ColumnDataSource
source=ColumnDataSource(dict(x=[1],y=[extract_value()]))

#create glyphs
f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y',source=source)



#create periodic function
def update():
    new_data=dict(x=[source.data['x'][-1]+1],y=[extract_value()])
    source.stream(new_data,rollover=200)
    print(source.data)

#add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update,10000)
