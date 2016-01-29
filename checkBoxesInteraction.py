import maya.cmds as cmds

def fun1():
    cmds.checkBox('Left', e=True, v=False)
    cmds.checkBox('Centre', e=True, v=False)
    cmds.checkBox('Right', e=True, v=False)
    
def fun2():
    cmds.checkBox('Left', e=True, v=True)
    cmds.checkBox('Centre', e=True, v=True)
    cmds.checkBox('Right', e=True, v=True)



if (cmds.window("window", exists=True)):
    cmds.deleteUI("window")
    

window1 = cmds.window('window', width=150)
cmds.columnLayout( adjustableColumn=True )

Default = cmds.checkBox("Default", label='Default', v=False, onCommand='fun1()', offCommand='fun2()' )
Left = cmds.checkBox("Left", label='Left', v=True,align='left' )
Centre = cmds.checkBox("Centre", label='Centre', v=True, align='center' )
Right = cmds.checkBox("Right", label='Right', v=True, align='right' )

cmds.showWindow( window1 )
 

