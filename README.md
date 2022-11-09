# <center>CR5_Project</center>

Dobot CR5 with Intel Realsense D435i for object detection and pose estimation (bin-picking application).

# Building

## ubuntu 20.04

### Use git to clone the source code
```sh
cd $HOME/catkin_ws/src
git clone https://github.com/monkeyrom/CR5_Project.git
cd $HOME/catkin_ws
```

### building
```sh
catkin_make
```
### set the dobot type
```sh
echo "export DOBOT_TYPE=cr5" >> ~/.bashrc
source ~/.bashrc
source $HOME/catkin_ws/devel/setup.bash
```

## 1.  Launch Project

* Connect the robotic arm with following command, and default robot_ip is 192.168.1.6 

```sh
    roslaunch CR5_Project CR5_with_realsense.launch
```

* this command will launch 
  - dobot_bringup
  - realsense camera pointcloud
  - find object 2d
  - tf synchronisation

### rviz display

![rviz display](./rviz.png)

### find object GUI

![find-object](./find object.png)

## 2.  Add object image for detection

* Using find object gui for adding image
  - > edit
  - > add object from scene
  - > take picture
  - > crop object

![find-object with object](./find object2.png)

### tf synchronize

![rviz display tf](./rviz2.png)

## 3.  Run C++ file for control robot

```sh
    rosrun CR5_Project service_call.launch
```

* this command will run 2 nodes and spawn new terminal for commanding
  - service_call
  - main_control

### new terminal for input command
![new terminal](./main control.png)

## Real Robotic Arm

### Dobot CR5 
![Dobot CR5](./dobot.jpg)

### Intel Realsense D435i
![Intel Realsense D435i](./dobot2.jpg)
