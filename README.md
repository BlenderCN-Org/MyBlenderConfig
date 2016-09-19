# boingyman_BlenderConfig
My Blender configuration files and scripts.

Download and place in %APPDATA%/Blender Foundation/Blender

Rename the folder to the version currently being used.

Scripts can be removed if only the theme is wanted.

Scripts included:

-convert_to_local_space.py: Parenting objects in Blender saves a reference point to a pseudo local space origin. There is a command to parent without this, but it sets the child's position to the local origin. This script fixes the pseudo origin of an existing child using the normal parenting command.

-batch_rename.py: Searches for part of the name of the currently selected objects and replaces them with the given string the user inputs in the popup menu.

-quick_menu.py: [DEFAULT: Q Key] Opens a menu that provides quick access to the listed commands above.
