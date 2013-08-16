from string.DEF_STRING import DEF_STRING

class TestString:
    
    def __init__(self,message):
        self.message = message
    
    def replace(self):
        string = "this is my python!!" +DEF_STRING().LINEBREAK()+ "this is my python!!"
        string = string.replace("my", "your");
        print string
        
    def replaces(self, old, new):
        string = self.message.replace(old, new);
        print string
        
t = TestString("this is my python!!" +DEF_STRING().LINEBREAK()+ "this is my python!!")
t.replaces("my", "your")