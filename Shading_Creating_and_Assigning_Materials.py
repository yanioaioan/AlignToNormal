import maya.cmds as cmds
import math as math

def createMaterial(name,color,type):
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name + 'SG' )
    cmds.shadingNode( type, asShader=True, name=name )
    cmds.setAttr( name+".color", color[0], color[1], color[2], type='double3')
    cmds.connectAttr(name+".outColor", name+"SG.surfaceShader")

def assignMaterial (name, object):
    cmds.sets(object, edit=True, forceElement=name+'SG')


def assignNewMaterial( name, color, type, object):
    createMaterial (name, color, type)
    assignMaterial (name, object)

cmds.polyPlane(name = 'ground', sw = 15, sh = 15, w = 15, h = 15)
for i in xrange(0,13):
    cmds.polySphere(name = 'ball' + str(i), radius = 0.5)
    pos = 2 + 1.5*math.sin( (1.6/math.pi)*(6-i) )
    val = (1 + math.sin( (1.6/math.pi)*(6-i) ))/2
    cmds.setAttr( 'ball' + str(i) + '.translateX', 6-i)
    cmds.setAttr( 'ball' + str(i) + '.translateY', pos)
    assignNewMaterial( 'ballShader' + str(i), (val, val, 1), 'blinn', 'ball' + str(i) )
    assignNewMaterial( 'ground' + str(i), (1, 1, 1), 'lambert', 'ground.f[' + str(118-i) + ']' )