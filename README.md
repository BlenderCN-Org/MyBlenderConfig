# boingyman_BlenderConfig

(This repository is mainly for me.)

My Blender configuration files and scripts. Includes a customized color scheme based off of the Elsyiun preset. Main changes to the scheme are the dropdown tab coloring in the properties panel and anywhere else that features the same kind of dropdown tab. The stats that show on the info panel's menu bar are now a more readable shade of white. Most notable of all, most of the panel layouts are customized for their specific purposes:


-Default: Usually the first thing one does in Blender is start modeling, as it is a 3D modeling program first and formost. This layout no longer has the Timeline panel on the bottom of the layout and the left side menu in the 3D View panel is now hidden by default. The Properties panel is now set to the Object tab by default.

-Material Editing: A layout made for process of creating and modifying materials. Consists of a large area for the Node Editor, a Properties panel next to the node editor with a Timeline panel below it, and small 3D View and UV/Image Editor panels on the right. Since editing materials while having the render preview running (Shift + Z) can slow down your computer, having a smaller 3D View panel will help improve productivity by reducing wait time on the preview rendering. The Timeline panel is included for any animated materials one could create. 

-Motion Tracking: Not customized.

-Rendering: Consists of a large UV/Image Editor panel for viewing renderings. A small 3D View panel is included in the top right corner for quick scene editing or camera placement (obviously, use a larger 3D View for more accurate control). Properties panel in the bottom right corner.

-Rigging: Not much to say other than the Default panel layout, but with 4 3D Views instead of 1.

-Scripting: A layout made for scripting. Includes the Text Editor, Python Console, 3D View, Outliner, and Properties panels.

-UV Editing: Layout consisting of a UV/Image Editor on the left, and 3D View panel on the right.

-Video Editing: Not customized.

-3D View Full: Not changed.

-Animation: Consists of all the things needed for animating. Dope Sheet, Graph Editor, Timeline, 2 3D Views, Outliner, and Properties panels. The large 3D View is meant to be used as the main window to animate in, while the small one is meant for a camera perspective preview.

-Compositing: A layout made for compositing renders. Includes a 3D View for changing the scene if needed, an UV/Image Editor for viewing renders and composites, and a large space for compositing. Also has the Properties and Timeline panels on the right.

Download and place in "%APPDATA%/Blender Foundation/Blender". Rename the folder to the version currently being used.

Scripts can be removed if only the theme is wanted.

Scripts included:

-convert_to_local_space.py: Parenting objects in Blender saves a reference point to a pseudo local space origin. There is a command to parent without this, but it sets the child's position to the local origin. This script fixes the pseudo origin of an existing child using the normal parenting command.

-batch_rename.py: Searches for part of the name of the currently selected objects and replaces them with the given string the user inputs in the popup menu. NOTE: Very basic. Does not protect from "" (empty string) searches.

-quick_menu.py: [DEFAULT: Q Key in 3D View] Opens a menu that provides quick access to the listed commands above.
