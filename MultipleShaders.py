import maya.cmds as cmds

cmds.select(all=True)
cmds.delete()

def shaderCreation(shadername,rgbColor=[1,1,1]):
    shadingnode=cmds.shadingNode("lambert",asShader=True, name = shadername)
    shading_group = cmds.sets(renderable=True,noSurfaceShader=True,empty=True, name = "newShadingGroup#")
    cmds.connectAttr(shadingnode + '.outColor', shading_group + '.surfaceShader')
    cmds.sets( e=True, forceElement = shading_group)
    attr = shadingnode + ".color"
    cmds.setAttr (attr, rgbColor[0], rgbColor[1], rgbColor[2]) # this line sets the values for R,G
    return shadername
    

#create shading node and shading group
myshadingNodeName1=shaderCreation("testShader1", [1,1,0])
myshadingNodeName2=shaderCreation("testShader2", [1,1,0])

#create object
s1=cmds.polySphere(r=sphereradius)
s2=cmds.polySphere(r=sphereradius*3)
cmds.xform(s2,translation=[50,0,0])
#select object
cmds.select("pSphere1")
#assing shader to this object
cmds.hyperShade(assign=myshadingNodeName1)
cmds.select("pSphere2")
cmds.hyperShade(assign=myshadingNodeName2)

#change each shading node's 1 color (already assigned to pSphere1)
attr1 = myshadingNodeName1 + ".color"
tmpColor=[0,0,1]#blue color
cmds.setAttr (attr, tmpColor[0], tmpColor[1], tmpColor[2]) # this line sets the values for R,G

#change each shading node's 2 color (already assigned to pSphere2)
attr2 = myshadingNodeName2 + ".color"
tmpColor=[1,0,0]#red color
cmds.setAttr (attr, tmpColor[0], tmpColor[1], tmpColor[2]) # this line sets the values for R,G

#make the big red sphere..blue
cmds.select("pSphere2")
#assing shader to this object
cmds.hyperShade(assign=myshadingNodeName1)

#make the small blue sphere..red
#assing shader to this object
cmds.hyperShade(assign=myshadingNodeName2)