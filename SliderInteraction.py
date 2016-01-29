import maya.cmds as cmds

#    Create a window with a couple integer slider groups.  The first will
#    use default limit values, and the second will set up a group that has
#    a field range greater than the slider range.  Try entering values
#    greater than the slider limits in both groups.
#
window = cmds.window( title='intSliderGrp Example' )
cmds.columnLayout()
gr1 = cmds.intSliderGrp( field=True, label='Group 1',changeCommand='fun()' )
gr2 = cmds.intSliderGrp( field=True, label='Group 2', minValue=-10, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=0, changeCommand='fun()')


def fun():
    test = cmds.intSliderGrp(gr1,query=True,value=True)
    if test==0:
        print 'hide'
    elif test==1:
        print 'get 1'
        
    test = cmds.intSliderGrp(gr2,query=True,value=True)
    if test==0:
        print 'hide'
    elif test==1:
        print 'get 1'
        
cmds.showWindow( window )