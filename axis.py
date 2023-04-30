import maya.cmds as cmds
import pymel as pm


move_context = "moveSuperContext"
rotate_context = "RotateSuperContext"
scale_context = "scaleSuperContext"
xform_context = "xformManipContext"


def init_context(ctx):
    if ctx is None:
        return cmds.currentCtx()
    return ctx


def toggle_object_world_orient(ctx=None):
    ctx = init_context(ctx)
    if cmds.superCtx(ctx, exists=True):
        tool = cmds.superCtx(ctx, q=True)
        if tool == 'Move':
            mode = cmds.manipMoveContext(tool, q=True, mode=True)
            if mode != 0:  # if not object mode, go to object mode
                cmds.manipMoveContext(tool, e=True, mode=0)
            else:  # else go to world mode
                cmds.manipMoveContext(tool, e=True, mode=2)

        elif tool == 'Rotate':
            mode = cmds.manipRotateContext(tool, q=True, mode=1)
            if mode != 0:  # if not object mode, go to object mode
                cmds.manipRotateContext(tool, e=True, mode=0)
            else:  # else go to world mode
                cmds.manipRotateContext(tool, e=True, mode=1)

        elif tool == 'Scale':
            mode = cmds.manipScaleContext(tool, q=True, mode=1)
            if mode != 0:  # if not object mode, go to object mode
                cmds.manipScaleContext(tool, e=True, mode=0)
            else:  # else go to world mode
                cmds.manipScaleContext(tool, e=True, mode=2)
    else:
        ctxClass = pm.contextInfo(ctx, c=True)  # c = class
        if ctxClass == "xformManipulator":
            toWorldSpace = not pm.setXformManip(q=True, worldSpace=True)
            pm.setXformManip(worldSpace=toWorldSpace)


def set_axis_orient(move_mode, rotate_mode, scale_mode, xform_world_space, ctx=None):
    ctx = init_context(ctx)
    if cmds.superCtx(ctx, exists=True):
        tool = cmds.superCtx(ctx, q=True)
        if tool == 'Move':
            cmds.manipMoveContext(tool, e=True, mode=move_mode)
        elif tool == 'Rotate':
            cmds.manipRotateContext(tool, e=True, mode=rotate_mode)
        elif tool == 'Scale':
            cmds.manipScaleContext(tool, e=True, mode=scale_mode)
    else:
        ctxClass = pm.contextInfo(ctx, c=True)  # c = class
        if ctxClass == "xformManipulator":
            pm.setXformManip(worldSpace=xform_world_space)


def set_object_orient(ctx=None):
    set_axis_orient(0, 0, 0, False, ctx)


def set_world_orient(ctx=None):
    set_axis_orient(2, 1, 2, True, ctx)


def set_component_orient(ctx=None):
    set_axis_orient(10, 10, 10, False, ctx)


def set_custom_orient(ctx=None):
    set_axis_orient(6, 3, 6, False, ctx)


def get_axis_orient(ctx=None):
    ctx = init_context(ctx)
    if cmds.superCtx(ctx, exists=True):
        tool = cmds.superCtx(ctx, q=False)
        if tool == 'Move':
            return cmds.manipMoveContext(tool, q=True, mode=True)
        elif tool == 'Rotate':
            return cmds.manipRotateContext(tool, q=True, mode=True)
        elif tool == 'Scale':
            return cmds.manipScaleContext(tool, q=True, mode=True)
    else:
        ctxClass = pm.contextInfo(ctx, c=True)  # c = class
        if ctxClass == "xformManipulator":
            return pm.setXformManip(q=True, worldSpace=True)
    return None
