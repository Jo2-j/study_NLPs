# class class_name:
#     변수
#     def _init_(self):
#         pass
    
class Animal:
    
    def __init__(self, name='JuJu'):
        self.name = name
        pass
    
    def speak(self, species):
        # return f'{self.name}는 {species} 종입니다'
        return f'{species} 종입니다'
class Dog(Animal):
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self):
        pass

    def walking(self, legs):
        return f'{legs}로 걷는다'

    def speak(self, species):
        return f'{species} species! '

if __name__ == '__main__':
    # dog = Dog()
    cat = Cat()
    cat.speak('Cat')
    cat.walking('4')
    pass

# 원래 조상이 가지고 있는거 코 풀지 않고 사용 할 수도, 내가 customize(overide, super) 할 수도 있는거
