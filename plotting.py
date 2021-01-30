from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p = figure(x_axis_type="datetime",width=400, height=100,sizing_mode="scale_both",title="Motion Graph",toolbar_location="above")
p.title.text_color='navy'
p.title.text_font_size = "25px"

p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start ","@Start_string"),("End ","@End_string")])
p.add_tools(hover)

p.quad(top=1, bottom=0, left="Start",right="End", color="green",source=cds)#(#B3DE69)

output_file('motion_detection.html',title="Motion_detector Graph")
show(p)
