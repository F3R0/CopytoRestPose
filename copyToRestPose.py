# CopyToRestPose by F3R0 (twitter: @ferotanman)

# This script simply copies the CURRENT POSE of a target armature to the 
# selected armature and applies it as the REST POSE. 

# It uses COPY_TRANSFORMS constraints and after completing the job
# IT REMOVES ALL 'COPY_TRANSFORMS' CONSTRAINTS ON THE TARGET ARMATURE. 

# Target Armature must be in a collection named "TargetArmature"
# Select ONLY the Rig you want to change it's rest pose and run the script.

bl_info = {
    "name": "Copy Rest Pose",
    "author": "Ferhat 'F3R0' Tanman",
    "version": (0, 0, 2),
    "blender": (2,93,5),
    "location": "View3D",
    "category": "FTools",
    "description": "Copies the CURRENT POSE of a target armature to the selected armature and applies it as the REST POSE. (twitter:@ferotanman)"
}

import bpy
from bpy.types import Operator

class FTOOLS_OT_CopyToRestPose(Operator):
  bl_idname = "ftools.copytorestpose"
  bl_label = "CopyPose to RestPose"
  bl_description = "Copies the CURRENT POSE of a target armature to the selected armature and applies it as the REST POSE. "

  def execute(self, context):
    # Target / Source definitions
    TARGET_COLLECTION_NAME = 'TargetArmature'
    ownerBoneList = context.active_object.pose.bones
    target_armature = bpy.data.collections[TARGET_COLLECTION_NAME].objects[0]
    targetBoneList = target_armature.pose.bones

    # Create COPY_TRANSFORM constraints on the source armature and define constraint targets.
    def CreateConstraints():
      for bone in ownerBoneList:
        targetBone = targetBoneList.get(bone.name)
        if targetBone == None:
          continue
        cons = bone.constraints.new('COPY_TRANSFORMS')
        cons.target = target_armature
        cons.subtarget = targetBone.name
        cons.target_space = 'POSE'
        cons.owner_space = 'WORLD'

    # Applies the pose as the rest pose
    def ApplyPoseAsRest():
      bpy.ops.object.posemode_toggle() 
      bpy.ops.pose.armature_apply(selected=True)

    # Removes COPY_TRANSFORM constraints from the source armature.
    def RemoveConstraints():
      for bone in ownerBoneList:
        for cons in bone.constraints:
          if cons.type == 'COPY_TRANSFORMS':
            bone.constraints.remove(cons)

    CreateConstraints()
    ApplyPoseAsRest()
    RemoveConstraints()

    bpy.ops.object.posemode_toggle()
    
    return {"FINISHED"}


def register():
  bpy.utils.register_class(FTOOLS_OT_CopyToRestPose)

def unregister():
  bpy.utils.unregister_class(FTOOLS_OT_CopyToRestPose)

# Uncomment if you are using this file by copying into Blender 's script editor.
# if __name__ == '__main__':
#    register()