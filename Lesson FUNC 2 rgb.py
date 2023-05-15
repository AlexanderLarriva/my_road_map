def rgb(red=0, green=0, blue=0):
  return f'rgb({red}, {green}, {blue})'
  

def get_colors():
  colors = {'red': rgb(red = 255),
            'green': rgb(green = 255),
            'blue': rgb(blue = 255)}
  return colors

colors = get_colors()

print(colors["green"])
