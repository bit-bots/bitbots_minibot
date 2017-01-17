

There are 3 different possibilities to start the minibot model:

Standalone visualisation only:
    This launches only Rviz (not Gazebo) and shows the robot model. You can inspect the links, the collision modell and much more. Does no real simulation, but gives you the possibility to change the robots pose by using some sliders.
    roslaunch minibot_description minibot_standalone.launch

Empty World simulation:
    This launches Gazebo with an an empty world. Useful if you want to test some motion capabilities of the robot.
    roslaunch minibot_description minibot_gazebo.launch

Robocup Field Simulation:
    This launches a simulation of a robocup field. You need some additional stuff to run this!
    Put the package nimbro_op_gazebo in your catkin workspace and compile it. Copy the content of the models folder of this package to ~./gazebo/models/
    roslaunch minibot_description minibot_robocup.launch