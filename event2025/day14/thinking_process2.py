rounds = [183, 325, 1097, 1101, 1451, 1697, 2204]

"""
round active
(183, 580)
(325, 572)
(1097, 636)
(1101, 648)
(1451, 576)
(1697, 588)
(2204, 628)


(183+period, 580)
(325+period, 572)
(1097+period, 636)
(1101+period, 648)
(1451+period, 576)
(1697+period, 588)
(2204+period, 628)

"""

"""


125 -> 552
552, 588

you play y rounds

1, 2, 3, .... y

(x1,     x2,   x3
 552     588

 
How many numbers in this set {125 + 4095*x | s.t 125+4095*x <= y} ? (add up 552)
How many numbers in this set {1017 + 4095*x | s.t 1017+4095*x <= y} ? (add up 588)

period = 4278

S_i = {arr[i] + period * x | s.t arr[i] + period * x <= y, x >= 0}

x <= (y-arr[i]) / period

|S_i| = (y-arr[i]) / period + 1

4095*x <= y-125
x <= (y-125) // 4095, x is a whole number (including 0)

|S1| = int(y-125/4095) + 1
|S2| = int(y-1017/4095) + 1

|S1| * 552 + |S2| * 588

chips@chips-windows:/tmp/tmp$ python3 main.py
142 <- 183
772 <- 183 + 142
4 <- 183 + 142 + 772
350 <- 183 + 142 + 772 + 4
246 <- 183 + 142 + 772 + 4 + 350
507 <- 183 + 142 + 772 + 4 + 350 + 246
2074 <- 183 + 142 + 772 + 4 + 350 + 246 + 507

-------- <-- 142 + 772 + 4 + 350 + 246 + 507 + 2074

"""

n = len(rounds)
for i in range(1, n):
    print(rounds[i] - rounds[i-1])
