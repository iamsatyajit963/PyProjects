class Player:
    def play(self):
        return 'Playing'

class Cricketer(Player):
    def play(self):
        return super().play()

# rohit = Cricketer()
print(id(Cricketer()))
print(id(Player()))
print(Cricketer().play() == Player().play()) #True : As Reference point is same

print(Cricketer().play() is Player().play()) #True : As Reference point is same