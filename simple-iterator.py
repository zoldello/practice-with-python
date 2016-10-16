__author__ = "Phil"

class SimpleIterator:
  def __init__(self):
    self.items = []

  def add(self, name):
    self.items.append(name)

  def __iter__(self):
    return self.items.__iter__()

if __name__ == "__main__":
  carts = SimpleIterator()

  carts.add('Billie Jean')
  carts.add("Dirty Diana")

  for cart in carts:
    print(cart)
