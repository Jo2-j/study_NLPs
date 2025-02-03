class Vehicle:
    def __init__(self, brand='Unknown', model='Unknown'):
        self.brand = brand
        self.model = model
    
    def get_info(self):
        return f'Brand: {self.brand}, Model: {self.model}'

class Car(Vehicle):
    def __init__(self, brand='Unknown', model='Unknown'):
        super().__init__(brand, model)  # 부모 클래스의 초기화 메서드 호출
    
    def get_info(self):  # 부모 클래스의 그대로 상속
        return super().get_info()
    
    def ride_info(self, wheels):
        return f'This car has {wheels} wheels'

class Truck(Vehicle):
    def __init__(self, brand='Unknown', model='Unknown'):
        super().__init__(brand, model)
    
    def get_info(self):  # 자체 구현
        return f'This is a truck - Brand: {self.brand}, Model: {self.model}'
    
    def more_info(self, wheels):
        return f'This truck runs on {wheels} wheels'

if __name__ == '__main__':
    # 테스트 코드
    car = Car('KIA', 'K7')
    truck = Truck('KIA', 'Bongo')
    
    # Car 테스트
    print(car.get_info())  # Brand: Toyota, Model: Camry
    print(car.ride_info(4))  # This car has 4 wheels
    
    # Truck 테스트
    print(truck.get_info())  # This is a truck - Brand: Volvo, Model: FH16
    print(truck.more_info(4))  # This truck runs on 6 wheels
