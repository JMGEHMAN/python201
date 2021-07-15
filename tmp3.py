class Food:
    name_list = []
    def __init__(self,name):
        self.name = name
        if self.name in Food.name_list:
            print(self.name, ' is in list')
        else:
            Food.name_list.append(self.name)

    def __del__(self):
        print(f'{self.name} will be removed from the list: {Food.name_list}')
        Food.name_list.remove(self.name)

a = Food('cheese')
b = Food('bread')
c = Food('meat')
d = Food('salt')

print(Food.name_list)