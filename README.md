# Maya QoL Scripts
Quality of life improvement script pack for the casual artist.

## Features

### Axis Orient Features
To use the axis orient features, import the axis module like this:
````python
from qol_scripts import axis
````

**Toggle object/world orient:**
````python
axis.toggle_object_world_orient()
````

**Set specific orients:**
````python
axis.set_object_orient()
# or
axis.set_world_orient()
# or
axis.set_component_orient()
# or
axis.set_custom_orient()
````

### Animation Features
To use the animation features, import the animation module like this:
````python
from qol_scripts import animation
````

**Set Default Weighted Tangents on or off:**
````python
animation.set_default_weighted_tangents(True/False)
# or alternatively
animation.toggle_default_weighted_tangents()
````

**Set Default Tangents (Stepped, Linear, Spline, Auto):**
````python
animation.set_default_tangents_stepped()
# or
animation.set_default_tangents_linear()
# or
animation.set_default_tangents_spline()
# or
animation.set_default_tangents_auto()
````

**Set Evaluation Mode (DG, Parallel, Serial):**
````python
animation.set_evaluation_mode_dg()
# or
animation.set_evaluation_mode_parallel()
# or
animation.set_evaluation_mode_serial()
````

Optionally, you can save the preferences so they remain the same after restarting Maya by using the `save_prefs` flag for all animation features:
````python
animation.set_evaluation_mode_parallel(save_prefs=True)
````

### Attribute Features
To use the attribute features, import the attribute module like this:
````python
from qol_scripts import attribute
````

**Set shape attribute for all shapes tied to the selected objects:**
````python
attribute.set_selection_shape_attribute("shapeAttributeName", value)
````

## Download & Install Instructions
- Download the release (*Maya QoL Scripts Zip Download*)
- Paste it in your Maya scripts folder 
- Unzip it / Extract all
- Make sure the resulting folder is named *qol_scripts*

## How to Use
- Inside Maya, open the Script Editor, or create a new shelf item
- In the text editor inside the Script Editor or the Shelf Editor, make sure the source language is Python
- Follow the coding instructions of the features listed in this README

Example of object/world axis orient toggle code:
````python
from qol_scripts import axis
axis.toggle_object_world_orient()
````
