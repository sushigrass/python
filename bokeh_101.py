from bokeh.plotting import figure
from bokeh.io import output_file, show, save
import pandas

def main():
    df=pandas.read_csv("data.csv")
    x=df["x"]
    y=df["y"]
    print df
    output_file("Line_from_bachelors.html")

    f=figure()

    f.line(x,y)

    save(f)

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
