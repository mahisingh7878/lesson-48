#Write a program to create two classes Dog and Cat, with the same attributes - (name and age) and methods - (info and make_sound). Create different objects for each class and pass the parameters. Showcase the concept of polymorphism in this program

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print("my name is {}and i am {} years old ".format(self.name,self.age))


    def makesound(self):
        print("i bark at the person i have not seen ")





class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print("my name{}and i am {}this year".format(self.name,self.age))

    def makesound(self):
        print("hi i am cat i meow on people to whom i do not like")





d=dog("coco",2)
c=cat("cutie",3)

for animal in(d,c):
    animal.info()
    animal.makesound()


                  

        
        
    
    