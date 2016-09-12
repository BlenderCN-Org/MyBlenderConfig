bl_info = {
    "name": "Convert To Local Space",
    "category": "Object"
}

import bpy


class ConvertToLocalSpace(bpy.types.Operator):
    """Converts the object from pseudo world space, to local space."""
    bl_idname = "object.convert_to_local_space"
    bl_label = "Convert to Local Space"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        for obj in context.selected_objects:
            obj.matrix_basis = obj.matrix_parent_inverse * obj.matrix_basis
            obj.matrix_parent_inverse.identity()
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ConvertToLocalSpace)

def unregister():
    bpy.utils.unregister_class(ConvertToLocalSpace)

def menu_draw(self, context):
    self.layout.operator(ConvertToLocalSpace.bl_idname)

bpy.types.VIEW3D_MT_object_parent.append(menu_draw)


if __name__ == "__main__":
    register()