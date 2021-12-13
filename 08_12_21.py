class animals():
    def __init__(self, type, gender, age, height, basic_food):
        self.type = type 
        self.gender = gender
        self.age = age
        self.height = height
        self.basic_food = basic_food

class mammals(animals):
    def __init__(self, type, gender, age, height, basic_food, tem, kol_cubs):
        super().__init__(type, gender, age, height, basic_food)
        self.tem = tem
        self.kol_cubs = kol_cubs

class human(mammals):
    def __init__(self, type, gender, age, height, basic_food, tem, kol_cubs, name, social_status):
        super().__init__(type, gender, age, height, basic_food, tem, kol_cubs)
        self.name = name
        self.social_status = social_status

class cat(mammals):
    def __init__(self, type, gender, age, height, basic_food, tem, kol_cubs, name, thoroughbred):
        super().__init__(type, gender, age, height, basic_food, tem, kol_cubs)
        self.name = name
        self.thoroughbred = thoroughbred

class dog(mammals):
    def __init__(self, type, gender, age, height, basic_food, tem, kol_cubs, name, presence_of_a_tattoo):
        super().__init__(type, gender, age, height, basic_food, tem, kol_cubs)
        self.name = name
        self.presence_of_a_tattoo = presence_of_a_tattoo 

class Student(human):
    def __init__(self, type, gender, age, height, basic_food, tem, kol_cubs, name, social_status, kol_dz_deliver):
        super().__init__(type, gender, age, height, basic_food, tem, kol_cubs, name, social_status)
        self.kol_dz_deliver = kol_dz_deliver
    def __eq__(self, Student):
        return self.kol_dz_deliver == Student.kol_dz_deliver
    def __ne__(self, Student):
        return self.kol_dz_deliver != Student.kol_dz_deliver    
    def __lt__(self, Student):
        return self.kol_dz_deliver < Student.kol_dz_deliver
    def __gt__(self, Student):
        return self.kol_dz_deliver > Student.kol_dz_deliver
    def __le__(self, Student):
        return self.kol_dz_deliver <= Student.kol_dz_deliver
    def __ge__(self, Student):
        return self.kol_dz_deliver >= Student.kol_dz_deliver

Planaria = animals('Flatworms', 'hermaphrodite', '2  months', 14, 'crustaceans, worms, snails')
Little_panda=mammals('Little_panda', 'female', '5  years', 55, 'vegetation', 39, 1)
Tom = human('A reasonable person', 'male', '23 years', 172, 'omnivorous', 36.6, 0, 'Tom', 'worker')
Kosmos = cat ('cat', 'male', ' 5 years', 57, 'omnivorous', 38.6, 0, 'Kosmos', False)
Dana = dog ('dog', 'female', ' 8 years', 45, 'omnivorous', 38.2, 0, 'Dana', True)
Bob = Student('A reasonable person', 'male', '21 years', 167, 'omnivorous', 36.6, 0, 'Bob', 'student', 13)
Elena = Student('A reasonable person', 'male', '21 years', 161, 'omnivorous', 36.6, 0, 'Elena', 'student', 23)
print(Bob == Elena)
print(Bob != Elena)
print(Bob < Elena)
print(Bob > Elena)
print(Bob <= Elena)
print(Bob >= Elena)