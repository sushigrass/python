from bokeh.models.glyphs import Circle
from bokeh.models import Plot, ColumnDataSource, Range1d, Grid, DataRange1d
from bokeh.io import output_file, show

def main():
    output_file("Line_from_models.html")

    x=[1,2,3,4,5]
    y=[6,7,8,9,10]

    data=ColumnDataSource(dict(x=x,y=y))

    p=Plot(x_range=DataRange1d(start=0,end=6),y_range=DataRange1d(start=0,end=11))
    #p=Plot(x_range=DataRange1d(start=0,end=15),y_range=DataRange1d(start=0,end=15))

    circle=Circle(x="x",y="y")


    p.add_glyph(data,circle)

    show(p)

if __name__ == "__main__":
    main()
