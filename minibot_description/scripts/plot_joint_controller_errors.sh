# plot joint-controller errors on Minibot to visualize problems
#
rosrun rqt_plot rqt_plot \
/minibot/HeadPanPositionController/state/error \
/minibot/HeadTiltPositionController/state/error \
/minibot/LAnklePitchPositionController/state/error \
/minibot/LAnkleRollPositionController/state/error \
/minibot/LElbowPositionController/state/error \
/minibot/LHipPitchPositionController/state/error \
/minibot/LHipRollPositionController/state/error \
/minibot/LHipYawPositionController/state/error \
/minibot/LKneePositionController/state/error \
/minibot/LShoulderPitchPositionController/state/error \
/minibot/LShoulderRollPositionController/state/error \
/minibot/RAnklePitchPositionController/state/error \
/minibot/RAnkleRollPositionController/state/error \
/minibot/RElbowPositionController/state/error \
/minibot/RHipPitchPositionController/state/error \
/minibot/RHipRollPositionController/state/error \
/minibot/RHipYawPositionController/state/error \
/minibot/RKneePositionController/state/error \
/minibot/RShoulderPitchPositionController/state/error \
/minibot/RShoulderRollPositionController/state/error 
