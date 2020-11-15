import random


class Stakeholder():

    #let's initialize all attributes as False to assign all clases this
    has_child = False
    is_vegan = False
    like_starbucks = False
    need_travel = False
    like_tech = False
    like_design = False
    like_basket = False
    like_party = False
    need_groomer = False


class Employee(Stakeholder):
    def __init__(self):
        super().__init__()

    like_party = True


class Ceo(Employee):

    is_vegan = True
    score = 100

    def __init__(self):
        super().__init__()




class Executive(Employee):

    like_starbucks = True
    score = 50

    def __init__(self):
        super().__init__()




class Account(Employee):
    score = 25
    need_travel = True

    def __init__(self):
        super().__init__()


class Whitecollar(Employee):
    score = 15

    def __init__(self):
        super().__init__()

class Developer(Whitecollar):

    like_tech = True

    def __init__(self):
        super().__init__()



class Engineer(Whitecollar):
    def __init__(self):
        super().__init__()



class Designer(Whitecollar):

    like_design = True

    def __init__(self):
        super().__init__()


class Bluecollar(Employee):
    score = 10
    like_basket = True

    def __init__(self):
        super().__init__()

class Dog(Stakeholder):
    score = 5
    need_groomer = True

    def __init__(self):
        super().__init__()


    
def assign_child(stakeholders, num):

    parents = 0
    random.seed(20)

    while parents < num:
        pick = random.choice(stakeholders)

        cond1 = issubclass(pick.__class__,Employee)
 
        cond2 = pick.has_child
        
        if  cond1 and (not cond2):
            pick.has_child = True
            parents += 1
        else:
            pass

    return stakeholders



def get_score(stakeholders, param):
    score = 0
    for stakeholder in stakeholders:
        
        if param == 'design':
            cond = stakeholder.like_design
        elif param == 'school':
            cond = stakeholder.has_child
        elif param == 'tech':
            cond = stakeholder.like_tech
        elif param == 'starbucks':
            cond = stakeholder.like_starbucks
        elif param == 'airport':
            cond = stakeholder.need_travel
        elif param == 'club':
            cond = stakeholder.like_party
        elif param == 'vegan':
            cond = stakeholder.is_vegan
        elif param == 'basket':
            cond = stakeholder.like_basket
        elif param == 'dog':
            cond = stakeholder.need_groomer
            
        else:
            pass

        if cond:
            score += stakeholder.score
        else:
            pass
        
    return score


def create_stakeholders():
    '''


    '''

    stakeholders = []
    number_stakeholders ={'Ceo': 1, 'Executive': 10, 'Account': 20, 'Developer': 15, 'Engineer': 20, 'Designer': 20, 'Bluecollar': 1, 'Dog': 1}

    for key, value in number_stakeholders.items():
        for _ in range(value):
            
            if key == 'Ceo':
                tmp = Ceo()
            elif key == 'Executive':
                tmp = Executive()
            elif key == 'Account':
                tmp = Account()
            elif key == 'Developer':
                tmp = Developer()
            elif key == 'Engineer':
                tmp = Engineer()
            elif key == 'Designer':
                tmp = Designer()
            elif key == 'Bluecollar':
                tmp = Bluecollar()
            elif key == 'Dog':
                tmp = Dog()
    
            stakeholders.append(tmp)

    return stakeholders






















CEO_NUM = 1
CEO_SCORE = 100
EXECUTIVES_NUM = 10
EXECUTIVES_SCORE = 50
ACCOUNT_MAN_NUM = 20
ACCOUNT_MAN_SCORE = 25