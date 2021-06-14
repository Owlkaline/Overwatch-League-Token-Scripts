#!/usr/bin/python3

COLOR1 = '${color0}'
COLOR2 = '${color1}'
COLOR_GREEN = '${color2}' #green
COLOR_RED = '${color3}' #red

with open("/home/akuma/Contenders", "r") as o:
  lines = o.readlines();
  if len(lines) == 0:
    print('%s%s' % (COLOR_RED, "No Scheduled Streams"));
  else:
    for line in lines:
      print('%s%s' % (COLOR_GREEN, line));
  
