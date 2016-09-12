bl_info = {
    "name": "Quick Menu",
    "category": "3D View"
}

import bpy

class QuickMenu(bpy.types.Menu):
    bl_label = "Quick Menu"
    bl_idname = "view3D.quick_menu"
    
    def draw(self, context):
        l = self.layout
        
        l.operator("object.convert_to_local_space")
        l.operator_context = 'INVOKE_DEFAULT'
        l.operator("object.batch_rename")

def register():
    bpy.utils.register_class(QuickMenu)
    
def unregister():
    bpy.utils.unregister_class(QuickMenu)
    
if __name__ == "__main__":
    register()