from bokeh.plotting import figure
from bokeh.io import output_file, show, save
from bokeh.models.tools import Range1d, PanTool, ResetTool, HoverTool
import pandas

def main():
    df=pandas.read_csv("data.csv")
    x=df["x"]
    y=df["y"]
    print df
    output_file("Line_from_bachelors.html")

    f=figure()

    f.line(x,y)

    #plot area
    f.plot_width = 1100
    f.plot_height = 650
    f.background_fill_color = "olive"
    f.background_fill_alpha = 0.3

    #plot title
    f.title.text = "this is a title"
    f.title.text_color = "olive"
    f.title.text_font = "times"
    f.title.text_font_size = "25px"
    f.title.align = "center"

    #axies
    f.xaxis.minor_tick_line_color ="blue"
    f.yaxis.major_label_orientation = "vertical"
    #f.xaxis.visible = False
    #f.xaxis.minor_tick_line_color = None #this overrides the previous one
    '''
    f.xaxis.minor_tick_in = -6
    f.xaxis.minor_tick_out = 4
    '''
    f.xaxis.major_label_text_color = "orange"

    #Axes geometry
    f.x_range = Range1d(start=0,end=10)
    f.y_range = Range1d(start=3,end=12)

    #f.xaxis.bounds = (2,5) #only ticks in a certain range
    f.yaxis[0].ticker.desired_num_ticks = 20

    #grid style
    f.xgrid.grid_line_color = None #no lines or color
    f.ygrid.grid_line_alpha = 0.3



    show(f)

    '''x = [1,2,3,4,5]
    y = [6,7,8,9,10]

    output_file("Line.html")

    f = figure()
    f.line(x,y)
    #f.triangle(x,y)
    #f.circle(x,y)
    show(f)'''

if __name__ == "__main__":
    main()
