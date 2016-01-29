"""
Mini Zen Garden Script
Tess Atkins
i7643172

Introductory Comments

The main idea for this script was to simulate building a minature zen garden, allowing a player to import objects into 
a scene one by one.

I have used dialogue boxes, while, if and elif statements to build the script, and enable the player to make choices. 

Firstly all shaders used within the scene are create to keep the main section of the script simple and succinct.
Then all the objects are defined as functions to later be called on throughout the script as needed.
Next the player is welcomed to the game, the scene is set and they are able to choose whether to play or not.
The player is then given their first choice of trees or wild flowers. Currently the script doesn't work as smoothly as I
would have liked, and only progresses through if wild flowers are selected. If trees are picked, the game returns to the 
start and adds another base. The same problem is found if 'no' is answered to the wendy house or pebble choices.

After all the options have been given, the player is asked if they are happy with their creation. If yes,
the game will send a message in response and subsequently quit. If no, the player is invited to play again.

Acknowledgemnts



"""
import maya.cmds as cmds

import random

cmds.file( new = True, force = True)

#First I will create all the shaders for the objects

green=cmds.shadingNode('blinn', asShader=True, name = 'new_blinn')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(green + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = green + '.color'
cmds.setAttr (attr, 0.1,0.5,0.1)

brown=cmds.shadingNode('blinn', asShader=True, name = 'new_blinn')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(brown + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = brown + '.color'
cmds.setAttr (attr, 0.8,0.4,0.4)

darkbrown=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(darkbrown + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = darkbrown + '.color'
cmds.setAttr (attr, 0.2,0,0)

purple=cmds.shadingNode('blinn', asShader=True, name = 'new_blinn')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(purple + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = purple + '.color'
cmds.setAttr (attr, 0.6,0.3,0.6)

roofred=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(roofred + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = roofred + '.color'
cmds.setAttr (attr, 0.5,0,0)

sand=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(sand + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = sand + '.color'
cmds.setAttr (attr, 0.7,0.6,0.4)

boxbrown=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(boxbrown + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = boxbrown + '.color'
cmds.setAttr (attr, 0.1,0,0.2)

blue=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(blue + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = blue + '.color'
cmds.setAttr (attr, 0.2,0.3,0.4)

grey=cmds.shadingNode('lambert', asShader=True, name = 'new_lambert')
shading_group = cmds.sets(renderable=True,noSurfaceShader = True,empty = True, name = 'new_shading_group')
cmds.connectAttr(grey + '.outColor', shading_group + '.surfaceShader')   
cmds.sets(e=True, forceElement = shading_group)
attr = grey + '.color'
cmds.setAttr (attr, 0.28,0.3,0.3)

#Next I will define all the functions that I will use within my scene

#defining function to make the garden base
def make_base(width,height,depth,xp,yp,zp):
    cmds.polyCube( w=width, h=height, d=depth)
    cmds.hyperShade(assign=blue)     
    cmds.move(xp, yp, zp)     
    cmds.select('pCube1.f[1]', r = True)     
    cmds.delete()      
#make_base(20,2,15,0,1,0)  
    cmds.polyPlane (width = 20, height =15)
    cmds.hyperShade(assign=sand) 
    cmds.move(0,1.2,0)          
 

#Defining function to make a tree
def make_tree():

    #make the tree trunk
    
    cmds.polyCylinder(r=0.3,h=5, name='treeTrunk' + str(i)) # (SB) The i in this line needs a value or will cause an error
    cmds.select('treeTrunk' + str(i), r=True) # (SB) The i in this line needs a value or will cause an error
    cmds.move(0,2,0)
    cmds.hyperShade(assign=darkbrown)    
    
    #make the main mass of leaves/foliage
    cmds.polySphere(sx=10,sy=10,r=2, name='treeLeaves' + str(i)) # (SB) The i in this line needs a value or will cause an error
    cmds.move(0,4,0)
    cmds.hyperShade(assign=green)    
    #grouped all geo together and named tree
    cmds.group('treeTrunk' + str(i),'treeLeaves' + str(i),name = 'tree' + str(i)) # (SB) The i in this line needs a value or will cause an error
    cmds.select('tree' + str(i), r = True) # (SB) The i in this line needs a value or will cause an error
    cmds.move(0,1.2,-5)
    
#defining function to make a flower
def make_wild_flower():
    
    #define make_petal to create flower petals and move to origin
    def make_petal(radius,height,xp,yp,zp):
        cmds.polyCylinder(r=radius, h=height)
        cmds.move(xp,yp,zp)
        cmds.hyperShade(assign=purple)    
    #making three simple petals using the function just created    
    make_petal(0.3,0.2,0.1,0,0.3)
    make_petal(0.3,0.2,-0.15,0,-0.1)
    make_petal(0.3,0.2,-0.4,0,0.3)
    
    #making petals into a group to move as one
    cmds.group('pCylinder1','pCylinder2','pCylinder3', name = 'petals')
    cmds.move(0.15,0,-0.1)
    
    #making stem of the flower   
    cmds.polyCylinder(r=0.09,h=0.9, name = 'stem')
    cmds.hyperShade(assign=green) 
    cmds.move(0,-0.25,0.02)
    cmds.select('petals','stem')
    cmds.group('petals','stem', name = 'wildFlower' + str(i))# (SB) The i in this line needs a value or will cause an error
    
#defining function to make pebbles

def pebbles():

    for i in range (200):
        randX = random.uniform(-9.5,9.5)
        randZ = random.uniform(-7.4,7.4)
        randY = random.uniform(0.05,0.25)
        rValue = random.uniform(0.1,0.4)
    
        cmds.polySphere(sx = rValue,sy = rValue,r = rValue)
        cmds.move(randX, 1.25, randZ, r = True)
        
        cmds.scale(rValue,randY,rValue, r = True)
        cmds.hyperShade(assign=grey)


#defining function to make the wendy house

def make_house():

    cmds.polyCube(h=3.4,d=4,w=4, name = 'houseBase')
    cmds.select('houseBase', r = True)
    cmds.move(4, 1.7, 3) 
    cmds.hyperShade(assign=roofred)
    cmds.polyPrism( l=4.5, sh=0, w=4.5, name = 'houseRoof')
    cmds.rotate(0,0,90)
    cmds.move(4, 4.3, 3)
    cmds.hyperShade(assign=grey) 
        
    cmds.polyCube(h=2,d=0.9,w=0.2, name = 'door') 
    cmds.move(6.1, 1, 2)
    cmds.hyperShade(assign=grey) 
        
    cmds.polyCube(h=1.5,d=0.9,w=0.2, name = 'window') 
    cmds.move(6.1, 1.5, 4)
    cmds.hyperShade(assign=grey)
    cmds.group('houseBase','houseRoof','door','window', name = 'house')
cmds.refresh()
#Introduce player to the scene and invite them to play
cmds.confirmDialog(message='Feeling stressed? Come on in and create a Mini Zen Garden!')

#User given choice of making Zen Garden or not                        
response = cmds.confirmDialog( title ='Mini Zen Garden',message='Would you like to build a mini Zen Garden? Its very theraputic!',
								button=['Yes','No'], defaultButton='Yes',
								cancelButton='No', dismissString='No' )

if response == 'No':
	cmds.confirmDialog(message='Ok no worries, maybe another time...')
	quit
while response == 'Yes': # (SB) At some point in this loop 'response' has to be assigned a value other than 'Yes' or the loop will be infinite
	#		For example, it could be set to either 'Yes' or 'No' depending on the value in 'final_choice' (see below)
	cmds.confirmDialog( title = 'Mini Zen Garden', message='Great! Lets add a base first...')
	
	make_base(20,2,15,0,1,0)
	#i = 0
	cmds.refresh()
	first_choice = cmds.confirmDialog( title = 'Mini Zen Garden',
										message='What would you like to add first, some trees or wild flowers?',
										button=['Trees','Wild flowers'])
	if first_choice == 'Trees':
		#make_tree()
	    for i in range (0,8): 
	    
	        randX = random.uniform(-9.5,9)
	        randZ = random.uniform(-1.4,10)   
	        
	        make_tree()
	        cmds.move(randX,1.2,randZ, r = True)
	        cmds.refresh()
	
	        #i = i + 1                
	elif first_choice == 'Wild flowers':
		make_wild_flower()
		cmds.move(0,1.9,0, r = True)
		cmds.refresh()
    #else: # (SB) edited this line 
	second_choice = cmds.confirmDialog( title = 'Mini Zen Garden',
										message='Would you like to add a Wendy house?',
										button=['Yes','No'])
	if second_choice == 'Yes':
		make_house()
		cmds.move(0,1.2,0, r = True)
		cmds.refresh()
	#else : # (SB) edited this line
	third_choice = cmds.confirmDialog( title = 'Mini Zen Garden',
										message='What would you like to add some decorative pebbles?',
										button=['Yeah','Nope'])
	if third_choice =='Yeah':
		pebbles()
		cmds.refresh()
	#else:
	final_choice = cmds.confirmDialog( title = 'Mini Zen Garden',
										message='Are you happy with your Mini garden?',
										button=['I am!','Not really'])
	if final_choice == 'I am!':
		cmds.confirmDialog( title = 'Mini Zen Garden',message='Great, the game will quit now')
		response = 'No'
		cmds.refresh() # (SB)edited this line
	else:
		response = 'Yes' # (SB)edited this line
        cmds.refresh()
		#return to start    
                        
'''
else == 'No':
    cmds.promptDialog( title = 'Mini Zen Garden',
    message='Ok, the game will quit now')
'''
