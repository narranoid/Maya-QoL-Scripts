import maya.cmds as mc

def set_selection_shape_attribute(attribute_name, value):
	lSelection = mc.ls(sl=1)
	lShapes = mc.listRelatives(lSelection, s=True)
	for s in lShapes:
		mc.setAttr( str(s) + '.' + attribute_name, value)