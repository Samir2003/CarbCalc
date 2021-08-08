#Samir, A
#4/12/2021
#CarbCalc

from energy_items import EnergyItem
from data_output import*
import datetime
import numpy as np
import time

year = datetime.datetime.now()
year = year.strftime("%Y")
user_items = []
item_name = []
item_emiss = []
data_table = []
graph_colours = []

def main():
  """Main entry point.
  
  """
  set_userinp()
  items_emiss(user_items)
  data_userinp()
  time.sleep(3)
  #This escape sequence is used to clear the console of any irrelevant or repeated text for user conveniance and readability
  print("\033c")
  print("\nThanks for using our calculator! Please view your results and begin with decreasing the emissions of the item that releases the most so far. Global Warming is a real and very important problem! If we want to minimize its effects, we need your help! One way to begin is to understand that everything electronic is emitting carbon directly or indirectly, even your computer! Therefore, a small place to start would be shutting your computer off for some time!")

def set_userinp():
  """Capture of the initial user input, like items to calculate emissions for.

  """
  print("\033c")
  print("Welcome to CarbCalc!")

  #The following print statement is repeated to enhance user readability and conveniance when entering input
  print("These are the following items that can be evaluated:\n[0] Vehicles\n[1] Housing\n[2] Flying/Travelling\n[3] Food")

  print("\nEach item can be selected more than once in the instance that one owns multiple vehicles/homes or lives with other people.")

  amt_items = int(input("\nHow many items would you like to report usage for (including duplicates): "))

  if amt_items == 0:
    print("Hopefully we can help you next time!")
    exit(0)

  for i in range(amt_items):
    typ_item = int(input("\nPlease enter the associated number with the item to enter: "))

    if typ_item == 0:
      fuel_type = input("\nPlease specify if your car is Gasoline, Hybrid, or Electric: ")
      usage_item = int(input("\nPlease enter the amount of km you travel per year in this vehicle: "))
      user_items.append(EnergyItem(f"Vehicle/{fuel_type}", usage_item))

    if typ_item == 1:
      usage_item = int(input("\nPlease enter the amount of kWh used per month: "))
      user_items.append(EnergyItem("Electricity/Housing",usage_item))
    
    if typ_item == 2:
      usage_item = int(input("\nPlease enter the amount of km that you travelled in a plane per year: "))
      user_items.append(EnergyItem("Travel/Flying",usage_item))

    
    if typ_item == 3:
      #Three seperate food variables were used instead of one list to avoid repetitive value calculations when user selects food consumption more than once
      usage_meat = (int(input("\nPlease input the calories of meat consumed per day on average: ")))
      usage_veg = (int(input("Please input the calories of vegetables consumed per day on average: ")))
      usage_fruit = (int(input("Please input the calories of fruits consumed per day on average: ")))
      user_items.append(EnergyItem("Food Consumption",[usage_meat,usage_veg,usage_fruit]))

    print("\033c")
    print("These are the following items that can be evaluated:\n[0] Vehicles\n[1] Housing\n[2] Flying/Travelling\n[3] Food")

def items_emiss(items):
  """Emissions for each user-selected item is calculated.
  
  Keyword arguments
  items -- The activities/items selected by the user
  """
  for i in range(len(items)):
    items[i].calc_emiss()
    item_name.append(items[i].get_name())
    item_emiss.append(items[i].get_emissions())

    #Numpy is used to produce a tuple of 3 random numbers as each number represents either red, green, or blue intensity and is used to ensure every bar/slice in the graphs have a different colour
    graph_colours.append(np.random.rand(3,))

  print("\nAll calculations have been made. Please select one of the following options by using the proper number associated with such option.\n[0] Save Raw Results\n[1] Save Emissions Bar Graph\n[2] Save Emissions Percentage Pie Graph")

def data_userinp():
  """Capture of the final user input, like how to display the results data.
  
  """
  num_rep = int(input("How many data representations would you like: "))

  if num_rep == 0:
    print("Please save your data next time!")
    exit(0)

  for i in range(num_rep):
    typ_rep = int(input("\nPlease enter the number of the data representation: "))

    if typ_rep == 0:
      data_table.append(["Items",f"Carbon (CO2e/yr)({year})"])

      for i in range(len(item_name)):
        data_table.append([item_name[i],item_emiss[i]])
      construct_table(data_table)
      print("\nCheck Emissions_results.txt for your results")
    
    if typ_rep == 1:
      construct_graphb(item_name,item_emiss,f"Comparison of Annual Emissions for Numerous Activities/Items in {year}", "Activities/Items", "Emissions Released Per Year (CO2e/yr)",graph_colours)
      print("\nCheck Emissions_Graphb.png for your graph.")
    
    if typ_rep == 2:
      construct_graphp(item_emiss,item_name,f"Comparison of Annual Emissions for Numerous Activities/Items by % in {year}",graph_colours)
      print("\nCheck Emissions_Graphp.png for your graph.")


if __name__ == '__main__':
  main()

