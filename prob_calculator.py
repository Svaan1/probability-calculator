import random
import copy

class Hat:
    def __init__(self,**kwargs):
        self.contents = list()
        for index in kwargs:
            number = kwargs[f'{str(index)}']
            for num in range(number):
                self.contents.append(str(index).lower())
    
    def draw(self,amount):
        result = list()
        if amount >= len(self.contents):
            amount = len(self.contents)
        for c in range(amount):
            random_number = random.randint(0,len(self.contents)-1)
            result.append(self.contents[random_number])
            self.contents.pop(random_number)
        return result    

    
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):

    m_count = 0

    expected_balls_list = list()
    for index in expected_balls:
        for number in range(expected_balls[str(index)]):
            expected_balls_list.append(index)
    
    for c in range(num_experiments):
        count = 0
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        for index in expected_balls:
            if drawn_balls.count(index) >= expected_balls[str(index)]:
                count += 1
        if count == len(expected_balls):
            m_count += 1
    
    result = m_count/num_experiments

    return result