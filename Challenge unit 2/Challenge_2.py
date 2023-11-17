class Player:
  def __init__(self, name):
      self.name = name

  def play(self):
      print(f"{self.name} is playing cricket.")

class Batsman(Player):
  def play(self):
      print(f"{self.name} is batting.")

class Bowler(Player):
  def play(self):
      print(f"{self.name} is bowling.")
player_name = input("Enter player's name: ")
player_type = input("Enter player type (Batsman/Bowler): ").lower()
if player_type == "batsman":
  player = Batsman(player_name)
elif player_type == "bowler":
  player = Bowler(player_name)
else:
  print("Invalid player type entered. Defaulting to Player.")
  player = Player(player_name)
player.play()
