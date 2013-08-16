class CAnimal:
    name = 'unname' 
    def __init__(self,voice='hello'):    
        self.voice = voice            
    def __del__(self):   
        print self.voice           
        pass                
    def Say(self):
        print self.voice

t = CAnimal()       
t.Say()        

class CDog(CAnimal):       
    def SetVoice(self,voice):
        self.voice = voice
    def Run(self,voice):
        print 'Running'

bobo = CDog()
bobo.SetVoice('My Name is BoBo!')   
bobo.Say()
bobo.Run('My Name is BoBo!') 

