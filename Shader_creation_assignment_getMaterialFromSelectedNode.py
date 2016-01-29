import maya.cmds as cmds

# check if material exists or not
for i in cmds.ls(mat=1):
    print i
    if not cmds.objExists('myblinn'):
        myBlinn = cmds.shadingNode('blinn', asShader=True, name = 'myblinn')
    if not cmds.objExists('myphong'):
        myPhong = cmds.shadingNode('phong', asShader=True, name = 'myphong')

# Create objects and assign shaders
cube = cmds.polyCube( sx=1, sy=1, sz=1, h=1 )
cmds.select(cube)

#cmds.hyperShade( assign=myBlinn) .. slows things down so replaced by the following
#a file texture node
file_node=cmds.shadingNode("file",asTexture=True)
# a shading group
shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
#connect shader to sg surface shader
cmds.connectAttr('%s.outColor' %myBlinn ,'%s.surfaceShader' %shading_group)
#connect file texture node to shader's color
cmds.connectAttr('%s.outColor' %file_node, '%s.color' %myBlinn)

mySphere = cmds.sphere(n='Sphere')
cmds.select(mySphere)

#cmds.hyperShade( assign=myPhong).. slows things down so replaced by the following
#a file texture node
file_node=cmds.shadingNode("file",asTexture=True)
# a shading group
shading_group= cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
#connect shader to sg surface shader
cmds.connectAttr('%s.outColor' %myPhong ,'%s.surfaceShader' %shading_group)
#connect file texture node to shader's color
cmds.connectAttr('%s.outColor' %file_node, '%s.color' %myPhong)

# add objects to a list
objectList = []
objectList.append(mySphere)
objectList.append(cube)
print objectList

# focus on Maya's HypershadeWindow
cmds.HypershadeWindow()
hsPanel = cmds.getPanel(withFocus=True)
for i in objectList:
    if len(i) > 0:
        # select current node        
        cmds.select(i[0], r=1)
        print i[0]
        # get the assigned material
        cmds.hyperShade(shaderNetworksSelectMaterialNodes=1)
        # list selected materials        
        materialList = cmds.ls(sl=1)
        print 'materialList='+str(materialList)
        ## Loop over the materials and print them        
        for material in materialList:
            print 'material='+str(material)                   
                 
