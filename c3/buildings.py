class Granary:
    def __init__(self,
                name = "Granary",
                status = "not_working",
                coords = tuple(),
                contents = {"Wheat": 0,
                            "Fruit": 0,
                            "Vegetables": 0,
                            "Meat": 0},
                contents_status = {"Wheat":"Accepting",
                                   "Fruit":"Accepting",
                                   "Vegetables":"Accepting",
                                   "Meat":"Accepting"},
                market_collector_threshold = 600,
                granary_threshold = 2400):
        self.market_collector_threshold = market_collector_threshold
        self.name = name
        self.contents = contents
        self.contents_status = contents_status
        self.status = status
        self.coords = coords
    
    def retrieve_contents(self):
        return self.contents
    
    def retrieve_contents_status(self):
        return self.contents_status
    
    def retrieve_working_status(self):
        return self.status

    def update_granary_status(self, x):
        _options = ["working","partial_working","idle"]
        if x not in _options:
            return print(f"{x} is not a valid working status")
        else:
            self.status = x

    def granary_addition(self,cart_dict):
        _cart_good = list(cart_dict.keys())[0]
        _current_amount = self.contents[_cart_good]
        _cart_amount = cart_dict[_cart_good]

        if _cart_amount == 100 and _current_amount < self.granary_threshold:
            self.contents[_cart_good]+=cart_dict[_cart_good]
        elif _cart_amount == 400 and _current_amount < self.granary_threshold - 400:
            self.contents[_cart_good]+=cart_dict[_cart_good]
        elif _current_amount == self.granary_threshold:
            return "cart_blocked, at capacity"


    def retrieve_granary_contents(self, good_dict):
        _good = list(good_dict.keys())[0]
        if self.contents[_good]>0:
            current_amount = self.contents[_good]
            if current_amount<= self.market_collector_threshold:
                self.contents[_good]-=current_amount
                return current_amount
            else:
                self.contents[_good]-=self.market_collector_threshold
                return self.market_collector_threshold
        else:
            return print(f"There is not sufficient {_good} to retrieve")

g = Granary()
g.update_granary_status("working")
print(g.retrieve_granary_contents({"Wheat":"collecting"}))
print(g.retrieve_working_status())