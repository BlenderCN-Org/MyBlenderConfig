bl_info = {
    "name": "Find and Replace Names",
    "category": "Object"
}

import bpy


class BatchRename(bpy.types.Operator):
    bl_idname = "object.batch_rename"
    bl_label = "Batch Rename"
    bl_options = {'REGISTER', 'UNDO'}
    
    find_string = bpy.props.StringProperty(
        name = "Find",
        description = "Define the sequence of characters in the names to find.",
    )
    
    replace_string = bpy.props.StringProperty(
        name = "Replace",
        description = "Define the sequence of characters to replace with.",
    )
    
    rename_component = bpy.props.BoolProperty(
        name = "Match Data?",
        description = "Do you want to match the name of the component (data) to the object's name?",
        default = True
    )
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.name = obj.name.replace(self.find_string, self.replace_string)
            if self.rename_component and obj.data != None:
                obj.data.name = obj.name + "." + str(obj.data.rna_type.identifier)
                
        return {'FINISHED'}
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(BatchRename)
    
def unregister():
    bpy.utils.unregister_class(BatchRename)
    
    
if __name__ == "__main__":
    register()