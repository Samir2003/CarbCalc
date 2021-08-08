class EnergyItem():
  def __init__(self, item_type, usage_amount):
    """Initializes the EnergyItem class.

    Keyword arguments
    item_type -- The name of the item
    usage_amount -- The amount used of the item in its proper units
    """
    self.name = item_type
    self.usage = usage_amount
    self.emission = []
  
  def calc_emiss(self):
    """Calculates the emission of each user-inputted item.
    
    """
    if "Vehicle" in self.name:
      if "gas" in self.name.lower():
        self.emission.append(self.usage * 0.22)
      
      elif "hybrid" in self.name.lower():
        self.emission.append(self.usage * 0.13)

      elif  "elec" in self.name.lower():
        self.emission.append(self.usage * 0.07)
    
    elif self.name == "Electricity/Housing":
      self.emission.append(self.usage * 12 * 0.19)
    
    elif self.name == "Travel/Flying":
      self.emission.append(self.usage * 2.10)
    
    elif self.name == "Food Consumption":
      for i in range(len(self.usage)):
        if i == 0:
          self.emission.append(self.usage[i] *365* (5.9/200))
        if i == 1:
          self.emission.append(self.usage[i]*365*(1.3/200))
        if i == 2:
          self.emission.append(self.usage[i]*365*(1.5/200))

  def get_emissions(self):
    """Returns the emissions of each item to a rounded value of 2 decimal places.

    """
    #The emissions value is rounded because certain usage numbers will yield very long decimals when calculating emissions
    return round((sum(self.emission)),2)
  
  def get_name(self):
    """Returns the name of each item.

    """
    return self.name