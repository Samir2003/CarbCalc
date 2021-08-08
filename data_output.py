import matplotlib.pyplot as plot
from tabulate import tabulate

def construct_graphb(x_data,y_data,graph_title,x_label,y_label,colours):
  """Constructs a bar graph based on the emissions of the user's items.

  Keyword arguments
  x_data -- The name of each user-selected item
  y_data -- The carbon emission value for each item
  graph_title -- The title of the bar graph
  x_label -- The x-axis title
  y_label -- The y-axis title
  colours -- The colours of the bars
  """
  #The clear function is ran first of every graphing function to ensure that there is no overlap of the previous graph when saving a png.
  plot.clf()
  plot.title(graph_title)
  plot.xlabel(x_label)
  plot.ylabel(y_label)
  plot.bar(range(len(x_data)),y_data, color = colours)
  #The labels for the x-axis have to be set seperately to avoid overlap when many items have to be graphed
  plot.xticks(range(len(x_data)),x_data, rotation = "vertical")

  #The data for the y-axis has to be enumerated and plotted as a textbox on the graph to display the user the true value of the bar for conveniance purposes
  for pos,values in enumerate(y_data):
    plot.text(x=pos, y = values+7, s = f"{values}", fontdict = dict(fontsize=7))
  
  plot.tick_params(axis = 'x', labelsize = 8)
  #When saving the figure, the graph is set to be saved as tight, to prevent extra white space when displaying the graph.
  plot.savefig('Emissions_Graphb.png',bbox_inches = "tight")

def construct_graphp(y_values,graph_labels,graph_title,colours):
  """Constructs a pie graph based on the emissions % of the user's items.

  Keyword arguments
  y_values -- The carbon emission value for each user-selected item
  graph_labels -- The name of each item
  graph_title -- The title of the pie graph
  colours -- The colours of the pie slices
  """
  plot.clf()
  plot.title(graph_title)
  plot.pie(y_values, labels = graph_labels, colors = colours, autopct = "%.2f")

  
  plot.savefig('Emissions_Graphp.png', bbox_inches = "tight")

def construct_table(data):
  """Constructs a table with fancy grid format of a 2D list.

  Keyword arguments
  data -- The 2D list of data to be formatted into a table
  """
  with open("Emission_results.txt",'w') as out_file:
    out_file.write(tabulate(data,headers = "firstrow", tablefmt = 'fancy_grid'))

