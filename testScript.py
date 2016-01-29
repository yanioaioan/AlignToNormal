import maya.cmds as cmds


def createBubbles(self):
    print 'here bubbles code is to be placed'

def createShip(self):
    print 'here ship code is to be placed'
    

if (cmds.window("window", exists=True)):
    cmds.deleteUI("window")
    

window1 = cmds.window('window', width=150)
cmds.columnLayout( adjustableColumn=True )

#eveything is handled by the functions createBubbles & createShip which they are attached to each of the buttons
def main():
    cmds.button( label='Button1', command=createBubbles )
    cmds.button( label='Button2', command=createShip )
    cmds.showWindow( window1 )


#here you are calling main function just once
main()
 


