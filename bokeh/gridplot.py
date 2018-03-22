from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import gridplot

def main():
    output_file('layout.html')

    x1,y1 = range(0,10),range(10,20)
    x2,y2 = range(20,30),range(30,40)
    x3,y3 = range(40,50),range(50,60)

    f1 = figure(width=250,plot_height=250,title='Circles')
    f1.circle(x1,y1,size=10,color="navy",alpha=0.5)

    f2 = figure(width=250,plot_height=250,title='Triangles')
    f2.triangle(x2,y2,size=10,color="navy",alpha=0.5)

    f3 = figure(width=250,plot_height=250,title='Squares')
    f3.square(x3,y3,size=10,color="navy",alpha=0.5)

    f = gridplot([f1,f2],[None,f3])
    show(f)

if __name__ == "__main__":
    main()
