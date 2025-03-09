import random

class market_collector:
    def __init__(self, name = "market_collector", bag = [], target_good = {}, status = "idle", travelling = False):
        self.name = name
        self.bag = bag
        self.status = status 
        self.travelling = travelling
        self.target_good = target_good

    def decide_on_target_good(self):

        #currently initiated to random, but would be decided upon by a different logic

        candidate_target_good = {"wheat": "collecting",
                        "fruit": "collecting",
                        "meat": "collecting",
                        "vegetables": "collecting",
                        "pottery":" collecting",
                        "furniture": "collecting",
                        "oil": "collecting",
                        "wine": "collecting"}
        
        random_key = random.choice(list(candidate_target_good.keys()))

        selection = {str(random_key):str(candidate_target_good[random_key])}

        self.target_good = selection

        return f"{self.name} is collecting {selection}"
    
    def travel(self, home_coords = tuple(), target_coords = tuple()):

        return f"{self.name} is travelling from {home_coords} to {target_coords}"
    
    def pickup_goods(self, amount = 0):
        

x = market_collector()

print(x.decide_on_target_good())

print(x.travel(home_coords=(1,1), target_coords=(13,17)))        




