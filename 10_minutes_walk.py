#http://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def isValidWalk(walk):
   v, g = 0, 0
   if len(walk) == 10:
       for d in walk:
           if d == 'n':
               g += 1
           elif d == 's':
               g -= 1
           elif d == 'w':
               v += 1
           else:
               v -= 1
       if v == 0 and g == 0:
           return True
   return False
