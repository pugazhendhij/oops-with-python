class Ride:

    def __init__(self,vehicle,distance):
        self.vehicle = vehicle
        self.distance = distance
        self.driver = None
        self.payment = 0

    def book_ride(self):
        print("User booked the ride")
        self.driver = self.__find_user()
        self.payment = self.__payment_calculation()

    def start_ride(self):
        print("User has started Ride")

    def end_ride(self):
        print(f"Ride is completed please make paymant {self.payment}.00")

    def __find_user(self):
        return "Pugazhendhi"

    def __payment_calculation(self):
        base_price = 5
        return self.distance * base_price
    
ride = Ride("Bike",10)
ride.book_ride()
ride.start_ride()
ride.end_ride()