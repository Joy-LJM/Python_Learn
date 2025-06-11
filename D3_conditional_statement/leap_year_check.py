# leap year(闰年)
year = input("Which year do you want to check?")
year_int = int(year)
if (year_int % 4 == 0):
  if (year_int % 100 == 0):  # modulo 取模
    if (year_int % 400 == 0):
      print("Leap year.")
    else:
      print("Not a Leap year.")
  else:
    print("Leap year.")
else:
  print("Not a Leap year.")