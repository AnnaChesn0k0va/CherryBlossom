class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):               
        self.amount_of_fuel -= count           
        self.total_weight -= count             
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                      
        return f'Топливо: {self.amount_of_fuel}'
    def get_total_weight(self):                                     
        return f'Масса: {self.total_weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine_status}'

def main():
    Taburetka = Rocket(95000, 4500, True)
    while Taburetka.amount_of_fuel > 0:
        Taburetka.spend_fuel(100)
        print(Taburetka.get_fuel_level(), end='; ')
        print(Taburetka.get_total_weight(), end='; ')
        print(Taburetka.get_is_engine_running())
main()
