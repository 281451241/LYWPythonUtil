'''
Created on 2013-8-16

@author: GB
'''

class HelloWorld:
    '''
    classdocs
    '''

    def println(self,string):
        s=string+"aaaa"
        print s.count(s[6:8])
        print s[1]
        print "The sum of 1 + 2 is {0}".format(10+5)
        print '%(language)s has %(number)03d quote types.' % \
            {"language": "Python", "number": 12}
    def testIf(self,string):
        s=string+"aaaa"
        print s.find('a')
        if s.find('a') > 0 :
            print "haha"
        else:
            print "hehe"
        
hello = HelloWorld()
hello.testIf('HelloWorl')
        