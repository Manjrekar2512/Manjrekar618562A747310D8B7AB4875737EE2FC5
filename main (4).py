class player:

  def play(self):
    print("The player is playing cricket")


class Batsman:

  def play(self):
    print("The batsman is batting")


class Bowler:

  def play(self):
    print("The Bowler is bowling")


playerobj = player()
Batsmanobj = Batsman()
Bowlerobj = Bowler()
playerobj.play()
Batsmanobj.play()
Bowlerobj.play()