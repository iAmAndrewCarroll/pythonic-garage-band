class Band:
  def __init__(self, name, members):
    self.name = name
    self.members = members

class Musician:
  def __init__(self, name, instrument):
    self.name = name
    self.instrument = instrument
  def __str__(self):
    return f"My name is {self.name} and I play {self.instrument}"
  def __repr__(self):
    return f"{self.__class__.__name__} instance. Name = {self.name}"

class Guitarist(Musician):
  def __init__(self, name):
    # super(). pulls from the parent class (musician), __init__ intializes the attributes, name is unique, "guitar" because every guitartist plays guitar.
    super().__init__(name, "guitar")
  def get_instrument(self): 
    return self.instrument

class Bassist(Musician):
  def __init__(self, name):
    super().__init__(name, "bass")
  def get_instrument(self): 
    return self.instrument
  
class Drummer(Musician):
  def __init__(self, name):
    super().__init__(name, "drums")
  def get_instrument(self): 
    return self.instrument

# if __name__ == '__main__':
