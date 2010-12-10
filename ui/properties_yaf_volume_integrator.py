import bpy
from bpy.props import *
World = bpy.types.World

World.v_int_type = EnumProperty(attr="v_int_type",
	items = (
		("Volume Integrator","Volume Integrator",""),
		("None","None",""),
		("Single Scatter","Single Scatter",""),
		#("Sky","Sky",""),
),default="None")
World.v_int_step_size =   FloatProperty(attr="v_int_step_size", precision = 3)
World.v_int_adaptive =    BoolProperty(attr="v_int_adaptive")
World.v_int_optimize =    BoolProperty(attr="v_int_optimize")
World.v_int_attgridres =  IntProperty(attr="v_int_attgridres")
World.v_int_scale =       FloatProperty(attr="v_int_scale")
World.v_int_alpha =       FloatProperty(attr="v_int_alpha")
World.v_int_dsturbidity = FloatProperty(attr="v_int_dsturbidity")

class YAF_PT_vol_integrator(bpy.types.Panel):

	bl_label = 'YafaRay Volume Integrator'
	bl_space_type = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context = 'world'
	COMPAT_ENGINES =['YAFA_RENDER']

	@classmethod
	def poll(self, context):

		engine = context.scene.render.engine
		return (context.world and  (engine in self.COMPAT_ENGINES) ) 


	def draw(self, context):

		layout = self.layout
		split = layout.split()
		col = split.column()

		col.prop(context.world,"v_int_type", text= "Volume Integrator")

		#if context.world.v_int_type == 'None':
		#	col.prop(context.world,"v_int_step_size", text= "Step Size")

		if context.world.v_int_type == 'Single Scatter':
			col.prop(context.world,"v_int_step_size", text= "Step Size")
			col.prop(context.world,"v_int_attgridres", text= "Att. grid resolution")
			row = layout.row()
			row.prop(context.world,"v_int_adaptive", text= "Adaptive")
			row.prop(context.world,"v_int_optimize", text= "Optimize")
			

		#if context.world.v_int_type == 'Sky':
		#	col.prop(context.world,"v_int_step_size", text= "Step Size")
		#	col.prop(context.world,"v_int_dsturbidity", text= "Turbidity")
		#	col.prop(context.world,"v_int_scale", text= "Scale")
		#	col.prop(context.world,"v_int_alpha", text= "Alpha")




classes = [
	YAF_PT_vol_integrator,
]

def register():
	register = bpy.types.register
	for cls in classes:
		register(cls)


def unregister():
	unregister = bpy.types.unregister
	for cls in classes:
		unregister(cls)


if __name__ == "__main__":
	register()

