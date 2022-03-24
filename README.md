## CopyToRestPose

This script simply copies the **CURRENT POSE** of an armature to a target 
armature and applies it as the REST POSE. 

It uses **COPY_TRANSFORMS** constraints and after completing the job
IT REMOVES ALL 'COPY_TRANSFORMS' CONSTRAINTS ON THE TARGET ARMATURE. 

Target Armature must be in a collection named **"TargetArmature"**
Select ONLY the Rig you want to change it's rest pose and run the script
or install it as an addon and call the operator named "CopyPose to RestPose"

twitter: @ferotanman
