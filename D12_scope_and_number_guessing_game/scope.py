# in python, there is no block scope(unlike js if, while, for)
# if you want to access a global variable in a function and update it, you should use keyword: global
enemies=1
def my_game(enemy):
  # not suggest
  # global enemies
  # enemies+=1
  print(f"enemies:{enemies}")
  return  enemy+1

my_game(enemies)
# constant variable: use upper case with underscore
PI=3.14
GOOGLE_URL="https://google.com"
print(GOOGLE_URL)