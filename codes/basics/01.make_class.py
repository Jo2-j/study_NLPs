# class class_name:
#     변수
#     def _init_(self):
#         pass
    
class Animal:
    
    def __init__(self):
        self.name = 'JuJu'
        pass
    
    def speak(self, species):
        return f'{self.name}는 {species} 종입니다'


if __name__ == '__main__':
    animal = Animal()
    animal.speak('Cat')
    pass
