from character import market_collector
from buildings import Granary

m = market_collector()
g = Granary()

g.update_granary_status("working")
g.granary_addition({"Meat":400})
g.granary_addition({"Wheat":100})
g.granary_addition({"Wheat":100})
print(g.retrieve_contents())
print(m.decide_on_food_good())
print(m.bag_contents())
print(g.retrieve_contents())
m.pickup_granary_goods(g)
print(g.retrieve_contents())
print(m.bag_contents())

