from random import uniform
import matplotlib.pyplot as plt

x = 0
y = 0
n = 100
titikX=[]
titikY=[]

for i in range(100):
    R = uniform(0,n)
    if (R <= 19):
        #N dir
        y+=1
    elif (R <= 43) :
        #NE dir
        x+=1
        y+=1
    elif (R <= 60) :
        #E dir
        x+=1
    elif (R <= 70) :
        #SE dir
        x+=1
        y-=1
    elif (R <= 72) :
        #S dir
        y-=1
    elif (R <= 75) :
        #SW dir
        x-=1
        y-=1
    elif (R <= 85) :
        #W dir
        x-=1
    elif (R <= 100) :
        #NW dir
        x-=1
        y+=1
    else :
        print("not a valid number")
        break
    titikX.append(x)
    titikY.append(y)

print("x,y final")
print("x: ", x)
print("y: ", y)

plt.plot(titikX,titikY)
plt.title('Blind Direction Hiker')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()