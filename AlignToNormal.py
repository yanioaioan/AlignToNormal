  
    
import maya.cmds as cmds


cmds.select(all=True)
cmds.delete()
cmds.polySphere(n='pSphere1',r=5)
cmds.select('pSphere1')

'''    
#select individual faces of selected object    
list = cmds.ls(sl=True)
for item in list:
    faceCount = cmds.polyEvaluate(f=True)
    for i in range(faceCount):
        #cmds.select(cl=True)
        cmds.select(item+'.f['+str(i)+']', add=True)
        print item+'.f['+str(i)+']'
'''


facenormals=cmds.polyInfo( fn=True )
#for i in range(len(facenormals)):
#    print '%s'%(facenormals[i])
    
'''
#https://www.mail-archive.com/python_inside_maya@googlegroups.com/msg07036.html
normals = [[], [], []]
for normal in facenormals:    
    normals = [[], [], []]
    label, vertex, x, y, z = normal.split()    
    normals[0].append(float(x))
    normals[1].append(float(y))
    normals[2].append(float(z))    
'''       

#numberofAllFaces=len(cmds.xform("pSphere1.f[:]", query=True, translation=True, worldSpace=True))/3

#find number of all selected faces
numberOfSelectedFacesFaces=cmds.polyEvaluate( fc=True )
#iterate through array of faces
i=238

for i in range(numberOfSelectedFacesFaces):
    #a list containing all individual vertex coordinates of a face. Usually 1 faces->1*4 vertices-> 4*3=12 coordianates total
    facepositionWS=cmds.xform("pSphere1.f["+str(i)+"]", query=True, translation=True, worldSpace=True)
    print 'face %d, faceposition=%s'%(i,facepositionWS)
    
    #find center of face (average the face's vertex posiitons)
    sumX=0
    sumY=0
    sumZ=0
    
    faceVertices=len(facepositionWS)/3
    vertexElements=3
    print "faceVertices=%d"%(faceVertices)
    for v in range(0,len(facepositionWS),vertexElements):
        sumX=sumX + facepositionWS[v]
        sumY=sumY + facepositionWS[v+1]
        sumZ=sumZ + facepositionWS[v+2]
        
    #average position of verteces of each faces    
    faceCenter = [sumX/faceVertices, sumY/faceVertices, sumZ/faceVertices]
        
    #place cone
    c=cmds.polyCone( n='myCone', sx=5, sy=5, sz=5)
    cmds.move( faceCenter[0], faceCenter[1], faceCenter[2], c, absolute=True )
    cmds.scale(0.3,0.3,0.3, c, absolute=True)
    
    #split polyinfo unicode , to get normals of each face
    fnormal= []
    label, vertex, x, y, z = facenormals[i].split()    
    fnormal.append(float(x))
    fnormal.append(float(y))
    fnormal.append(float(z))
    
    
    fnormalNormalized=[]
    #normalize vector from point on sphee to origin of sphere
    
    mag=math.sqrt( fnormal[0]*fnormal[0] + fnormal[1]*fnormal[1] + fnormal[2]*fnormal[2] )
    fnormalNormalized.append(fnormal[0]/mag)
    fnormalNormalized.append(fnormal[1]/mag)
    fnormalNormalized.append(fnormal[2]/mag)
        
    print "fnormalNormalized=%s"%(fnormal)
    
    #rotate each cone based on face normal vector
    #print 'x=%d,y=%d,z=%d rot'%(toEuler(normal[0],normal[1],normal[2]))
    
    '''
    r=math.sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2])
    theta=math.acos(normal[2]/r)* (180/math.pi)
    phi=math.atan(normal[1]/normal[0])* (180/math.pi)
    '''
    
    #calculcate axis-angle 
    upVec=[0,0,1]    
    axis=cross(upVec, normal)
    axisNormalized=[]
    mag=math.sqrt( axis[0]*axis[0] + axis[1]*axis[1] + axis[2]*axis[2] )
    axisNormalized.append(axis[0]/mag)
    axisNormalized.append(axis[1]/mag)
    axisNormalized.append(axis[2]/mag)
    
    print "dot(upVec,fnormalNormalized)=%f"%(dot(upVec,fnormal))
    angle=math.acos( dot(upVec,fnormal) )
    
    
    #caclulcate euler angles based on axis-angle
    s=math.sin(angle)
    c=math.cos(angle)
    t=1-c
    heading = axisNormalized[0]*angle#math.atan2(axisNormalized[1] * s- axisNormalized[0] * axisNormalized[2] * t , 1 - (axisNormalized[1]*axisNormalized[1]+ axisNormalized[2]*axisNormalized[2] ) * t);
    attitude =  axisNormalized[1]*angle#math.asin(axisNormalized[0] * axisNormalized[1] * t + axisNormalized[2] * s) ;
    bank = axisNormalized[2]*angle#math.atan2(axisNormalized[0] * s - axisNormalized[1] * axisNormalized[2] * t , 1 - (axisNormalized[0]*axisNormalized[0] + axisNormalized[2]*axisNormalized[2]) * t);
    
    
    heading*=(180/math.pi)
    attitude*=(180/math.pi)
    bank*=(180/math.pi)
    
    print "heading=%d"%(heading)
    print "attitude=%d"%(attitude)
    print "bank=%d"%(bank)
    cmds.refresh()
    #cmds.rotate( str(bank), str(heading), str(attitude),  absolute=True, ws=True )
    cmds.rotate( heading, attitude, bank,  absolute=True, ws=True )
    
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c
    
p=0   
def dot(a,b):
    global p
    p=0 
    for i in range(len(a)):
        p+=a[i]*b[i]
    return p
    

    
    
    
    
    
    
    
    
    
    