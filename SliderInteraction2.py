import maya.cmds as cmds
  
window = cmds.window( title='intSliderGrp Example' )
cmds.columnLayout()

s1=cmds.sphere(n='s1')
s2=cmds.sphere(n='s2')
 
cmds.move(2,0,0,s2)
cmds.select(s1)
cmds.hide (s1)
cmds.select(s2)
cmds.hide (s2) 

numBcases = cmds.intSliderGrp(label='BookCase',field=True, minValue=0, maxValue=5, value=0, cc='getValue()')

def getValue():
    global myNumBcase 
    myNumBcase = cmds.intSliderGrp( numBcases, q=True, value=True )
    
    if(myNumBcase==1):       
       cmds.showHidden (s1, above=True)
        
       print '1'
    if(myNumBcase==2):
       cmds.showHidden (s2, above=True)
       print '2'
    if(myNumBcase==0):
       cmds.select(s1)
       cmds.hide (s1)
       cmds.select(s2)
       cmds.hide (s2)   
       print 'hide'  
     


objName = cmds.shadingNode('phong', asShader=True)
cmds.columnLayout()
cmds.attrColorSliderGrp( at='%s.color' % objName )
    
cmds.showWindow(window)