# This file was *autogenerated* from the file 44.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_10000 = Integer(10000)
P = set()
for i in (ellipsis_range(_sage_const_1  ,Ellipsis, _sage_const_10000 )) :
    P.add(i * (_sage_const_3  * i - _sage_const_1 ) / _sage_const_2 )

x = sorted(list(P))
# print x
for i in x :
    for j in x :
        if i < j :
            break
        if (i + j) in P and (i - j) in P :
            print i, j, i - j