import random

class market_collector:
    def __init__(self, name = "market_collector", bag = [], target_good = {}, status = "idle", travelling = False, home_coords = tuple(), target_coords = tuple()):
        self.name = name
        self.bag = bag
        self.status = status 
        self.travelling = travelling
        self.target_good = target_good
        self.home_coords = home_coords
        self.target_coords = target_coords

    def bag_contents(self):
        return self.bag
    def decide_on_food_good(self):

        #currently initiated to random, but would be decided upon by a different logic

        candidate_target_good = {"Wheat": "collecting",
                        "Fruit": "collecting",
                        "Meat": "collecting",
                        "Vegetables": "collecting"}
        
        random_key = random.choice(list(candidate_target_good.keys()))

        selection = {str(random_key):str(candidate_target_good[random_key])}

        self.target_good = selection

        return f"{self.name} is collecting {selection}"
    
    def init_travel(self, home_coords = tuple(), target_coords = tuple()):


        return f"{self.name} is travelling from {home_coords} to {target_coords}"
    
    def pickup_granary_goods(self, granary):
        _dict_target = self.target_good
        #e.g. Wheat
        #_target = list(_dict_target.keys()[0])
        _dict_carrying = granary.collect_from_granary(_dict_target)
        self.bag.append(_dict_carrying)





# x = market_collector()

# print(x.decide_on_target_good())

# print(x.travel(home_coords=(1,1), target_coords=(13,17)))

# goes 




