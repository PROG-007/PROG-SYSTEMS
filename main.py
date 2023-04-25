import msvcrt
import os

class Selector:
    def __init__(self, options):
        self.options = options
        self.index = 0
        self.list = ["Item"]*options

    def run(self):
        while True:
            os.system("cls")
            if self.index > self.options-1:
                self.index = 0
            if self.index < 0:
                self.index = self.options-1
            for i in range(self.options):
                temp = ["*", " "][i != self.index]
                print(temp, self.list[i], temp)
            char = msvcrt.getch()
            if char == b'\xe0':
                char = msvcrt.getch()
                if char == b'H':
                    self.index -= 1
                elif char == b'P':
                    self.index += 1
            if char == b'\r':
                print("AYEEEE YOU SELECTED!!")
                break
            if char == b'\b':
                print("AYEEEE YOU NOT SELECTED!!")
                break

s = Selector(5)
s.run()