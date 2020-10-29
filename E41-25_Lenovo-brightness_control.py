import os
print("Monitor: eDP")
print("xrandr --output eDP --brightness x.x")
value  = str(input("Enter Brightness Value 0.2 - 0.8: "))
cmd = "xrandr --output eDP --brightness " + value
os.system(cmd)
