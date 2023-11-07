from GridWorld import GridWorld
from QLearning import QLearning

gw = GridWorld("map/largeMap.txt", 0.01)
ql = QLearning(gw)
ql.run()
ql.get_result()