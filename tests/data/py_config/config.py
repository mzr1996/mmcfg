from mmcfg import read_base

with read_base():
    from .base1 import item1, item2, item3, item4
    from .base2 import *

with read_base():
    from .base3 import item8, item9, item10

item2['a'] = 1
item11 = item1.copy() + [3]
