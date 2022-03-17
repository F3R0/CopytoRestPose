# CopyToRestPose by F3R0 (twitter: @ferotanman)

# This script simply copies the CURRENT POSE of an armature to a target 
# armature and applies it as the REST POSE. 

# It uses COPY_TRANSFORMS constraints and after completing the job
# IT REMOVES ALL 'COPY_TRANSFORMS' CONSTRAINTS ON THE TARGET ARMATURE. 

# Target Armature must be in a collection named "TargetArmature"
# Select ONLY the Rig you want to change it's rest pose and run the script.


import bpy

TARGET_COLLECTION_NAME = 'TargetArmature'

collections = bpy.data.collections

# Get selected / active objects
targetCollection = bpy.data.collections[TARGET_COLLECTION_NAME]
target_armature = targetCollection.objects[0]
selected_armature = bpy.context.active_object

#Set Owner Rig
ownerBoneList = selected_armature.pose.bones

#Set Target Rig
targetBoneList = target_armature.pose.bones

for bone in ownerBoneList:
    targetBone = targetBoneList.get(bone.name)
    if targetBone == None:
      continue
    cons = bone.constraints.new('COPY_TRANSFORMS')
    cons.target = target_armature
    cons.subtarget = targetBone.name
    cons.target_space = 'POSE'
    cons.owner_space = 'WORLD'

bpy.ops.object.posemode_toggle() 
bpy.ops.pose.armature_apply(selected=True)

for bone in ownerBoneList:
  for cons in bone.constraints:
    if cons.type == 'COPY_TRANSFORMS':
      bone.constraints.remove(cons)

bpy.ops.object.posemode_toggle()

