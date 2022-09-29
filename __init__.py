
class Stack:
  def __init__(self) -> None:
    self.items = []

  def is_empty(self) -> bool:
    return len(self.items) == 0

  def push(self, data: any) -> None:
    self.items.insert(0, data)

  def pop(self) -> any:
    return self.items.pop(0)

  def print(self):
    items =  self.items[:]

    end = " <== "
    while(items):
      if len(items) == 1:
        end = "\n"
      
      print(items.pop(0), end=end)


def main(*args, **kwargs) -> None:
  stack = Stack()

  stack.push(5)
  stack.push(4)
  stack.push(3)
  stack.push(2)
  stack.push(1)
  stack.print()

  stack.pop()
  stack.print()

  stack.push(0)
  stack.print()

if __name__ == "__main__":
  main()
