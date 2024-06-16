#Factory
class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        
    def print(self):
        print(self.ingredients)
        
class BurgerFactory:
    
    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["bun", "tomato", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["bun", "special-sauce", "veggie-patty"]
        return Burger(ingredients)
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()

# Builder: protocol buffers
class Burger2:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None
        
    def setBuns(self, bunStyles):
        self.buns = bunStyles
    
    def setPatty(self, pattyStyle):
        self.patty = pattyStyle
        
    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

class BurgerBuilder:
    def __init__(self):
        self.burger = Burger2()
        
    def addBuns(self, bunStyles):
        self.burger.setBuns(bunStyles)
        return self
    
    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger
    
burger = BurgerBuilder()\
            .addBuns("sesame")\
            .addPatty("fish-patty")\
            .addCheese("swiss-cheese")\
            .build()
# each method will return a reference to the Builder     

#Singleton: for example: maintaining a single copy of Application State; start having a static instance variable
# In our app: 1. If our user is logged in or not? (we won't use the Constructor to actually instantiate the application state )

class ApplicationState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False # the login vlaue will be initially be False
        
    # will use a @staticmethod called getAppState(): will first check if there's already an existing instance of the application State
    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance # if yes, return the existing instance, will never create more than one

appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn) # will get the initial False

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn) #True
print(appState2.isLoggedIn) #True


    
    
            
    