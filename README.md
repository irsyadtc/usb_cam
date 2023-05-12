# [usb_cam](http://wiki.ros.org/usb_cam)
[![ROS1 CI](https://github.com/ros-drivers/usb_cam/actions/workflows/main.yml/badge.svg)](https://github.com/ros-drivers/usb_cam/actions/workflows/main.yml)
[![ROS2 CI](https://github.com/ros-drivers/usb_cam/actions/workflows/build_test.yml/badge.svg)](https://github.com/ros-drivers/usb_cam/actions/workflows/build_test.yml)

## Versions up to 0.3.7
The last ROS 1 version of this package based on "classic" old code of FFMPEG and `libv4l2` is `0.3.7`, currently available via ROS package repository. The `develop` branch of this repository is now based on the **new version of code** with different internal API and configuration process. Please refer to [this page](http://wiki.ros.org/usb_cam/Old%20Versions) on ROS wiki to learn more about how to configure older versions of this package.

## A ROS Driver for V4L USB Cameras

This package is based off of V4L devices specifically instead of just UVC.

For full documentation, see [the ROS wiki](http://ros.org/wiki/usb_cam).

[Doxygen](http://docs.ros.org/indigo/api/usb_cam/html/) files can be found on the ROS wiki.

## ROS2 branch

If you want to use ROS2 version,
please check [ros2](https://github.com/ros-drivers/usb_cam/tree/ros2) branch.

## License

usb\_cam is released with a BSD license. For full terms and conditions, see the [LICENSE](LICENSE) file.

## Authors

See the [AUTHORS](AUTHORS.md) file for a full list of contributors.

## Add on IP camera Android phone

Install IP Webcam apps on your android phone. https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en&gl=US. Make sure both ROS PC and phone are on the same network.

On the phone
Open IP Webcam and press 'Start server' option.  Take note of its IP address e.g. http://192.168.0.174:8080

ROS PC

Terminal 1: ```roscore```

Terminal 2: ```rosrun usb_cam ip_cam_node.py http://192.168.0.174:8080/shot.jpg open```

