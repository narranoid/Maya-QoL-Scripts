import pymel.core as pm


def set_default_weighted_tangents(weighted_tangents, save_prefs=False):
    pm.keyTangent(g=True, weightedTangents=weighted_tangents)
    if save_prefs:
        pm.savePrefs(general=True)


def toggle_default_weighted_tangents(save_prefs=False):
    weighted_tangents = pm.keyTangent(q=True, g=True, weightedTangents=True)
    set_default_weighted_tangents(not weighted_tangents, save_prefs)


def set_default_tangents(default_in_tangent, default_out_tangent, save_prefs=False):
    pm.keyTangent(g=True, inTangentType=default_in_tangent)
    pm.keyTangent(g=True, outTangentType=default_out_tangent)
    if save_prefs:
        pm.savePrefs(general=True)


def set_default_tangents_stepped(save_prefs=False):
    set_default_tangents("clamped", "step", save_prefs)


def set_default_tangents_linear(save_prefs=False):
    set_default_tangents("linear", "linear", save_prefs)


def set_default_tangents_spline(save_prefs=False):
    set_default_tangents("spline", "spline", save_prefs)


def set_default_tangents_auto(save_prefs=False):
    set_default_tangents("auto", "auto", save_prefs)


def set_evaluation_mode(evaluation_mode, save_prefs=False):
    pm.evaluationManager(mode=evaluation_mode)
    if save_prefs:
        pm.savePrefs(general=True)


def set_evaluation_mode_dg(save_prefs=False):
    set_evaluation_mode("off", save_prefs)


def set_evaluation_mode_parallel(save_prefs=False):
    set_evaluation_mode("parallel", save_prefs)


def set_evaluation_mode_serial(save_prefs=False):
    set_evaluation_mode("serial", save_prefs)
