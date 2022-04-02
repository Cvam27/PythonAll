class Phone:

    def set_cost(self,cost):
        self.cost = cost

    def show_cost(self):
        return self.cost

p1=Phone()
p1.set_cost(300)
print(p1.show_cost())
