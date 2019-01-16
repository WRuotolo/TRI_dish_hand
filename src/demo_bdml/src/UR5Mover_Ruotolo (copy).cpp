#include <ros/ros.h>
#include <tf/transform_datatypes.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <math.h>
#include <string.h>
#include <sys/time.h>
#include <stdio.h>
#include <unistd.h>
#include <boost/thread/thread.hpp>
#include "sensor_msgs/JointState.h"
#include "geometry_msgs/WrenchStamped.h"
#include "roboticArm.h"
#include "URcontrolV2.h"
#include "std_msgs/String.h"

#include <tf/transform_listener.h>
#include <geometry_msgs/Vector3.h>

#include <ur_msgs/FollowCartesianTrajectoryAction.h>
#include <actionlib/client/simple_action_client.h>
typedef ur_msgs::FollowCartesianTrajectoryGoal CartesianTrajectory;

//Using boost and std namespaces
using namespace std;
using namespace boost::posix_time;

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  //ROS_INFO("I heard: [%s]", msg->data.c_str());
  ROS_INFO("TESTING");
}

int main(int argc, char **argv)
{

  // Original initialization stuff
  ros::init(argc, argv, "ur5_mover");
  ros::NodeHandlePtr n = boost::make_shared<ros::NodeHandle>();
  ros::Rate loop_rate(1000);
  ROS_INFO("Old Init");

/*
  // Subscriber initialization stuff
  ros::NodeHandle n2;
  ros::Subscriber sub = n2.subscribe("ar_base_tranform", 1000, chatterCallback);

  ros::spin();
*/

  RoboticArm robot; //Robot control object

  /************* INITIAL POSITIONS AND ORIENTATIONS **************/
  Client client ("follow_cart_trajectory");
//  client.waitForServer();

  tf::Transform tfpose_init, tfpose_oriented, APoseToReach1, APoseToReach2; //Poses
  tf::Vector3 ToolOffset, ASetOfCoordinnates; //Tool offset

  // Preliminary tests to check if robot is moving alright:
  tfpose_init = robot.get_arm_position("base_link");
  orientEffectorTowardsTable(tfpose_init, tfpose_oriented); //Calculate matrix to orient gripper towards table
  ASetOfCoordinnates.setValue(-0.300758,0.425294,0.408129); //Home Position
  APoseToReach1.setBasis(tfpose_oriented.getBasis());
  APoseToReach1.setOrigin(ASetOfCoordinnates);

  // Listen to tf for ar_tag_9 position in base frame
  tf::TransformListener listener;
  ros::Rate rate(10.0);
  while (true) {
	tf::StampedTransform transform;
	try{
		listener.lookupTransform("/ar_marker_9","/base_frame",ros::Time(0),transform);
	}
	catch (tf::TransformException &ex) {
           ROS_ERROR("%s",ex.what());
           ros::Duration(1.0).sleep();
  	   continue;
        }
  tf::Vector3 testVec = transform.getOrigin();
  //float testFloat = testVec.x;
  ROS_INFO("Looping");

  CartesianTrajectory trajectory;
  trajectory.header.frame_id = "base_link";
  trajectory.velocity = .3;
  trajectory.poses = std::vector<geometry_msgs::Pose>(1);
  trajectory.poses[0].position.x = transform.getOrigin().x();
  trajectory.poses[0].position.y = .4; //transform.getOrigin().y();
  trajectory.poses[0].position.z = .5;
  trajectory.poses[0].orientation.x = 1.571;
  trajectory.poses[0].orientation.y = 1.571;
  trajectory.poses[0].orientation.z = -1.571;
  trajectory.poses[0].orientation.w = 0;
  client.sendGoal(trajectory);
  client.waitForResult();
  }


/*
  // Manual path Example
  CartesianTrajectory trajectory;
  trajectory.header.frame_id = "base_link";
  trajectory.velocity = .3;
  trajectory.poses = std::vector<geometry_msgs::Pose>(1);
  trajectory.poses[0].position.x = 0;
  trajectory.poses[0].position.y = .5;
  trajectory.poses[0].position.z = .5;
  trajectory.poses[0].orientation.x = 1.571;
  trajectory.poses[0].orientation.y = 1.571;
  trajectory.poses[0].orientation.z = -1.571;
  trajectory.poses[0].orientation.w = 0;
  client.sendGoal(trajectory);

  client.waitForResult();

  trajectory.poses[0].position.x = .01;
  trajectory.poses[0].position.y = .51;
  trajectory.poses[0].orientation.z = 0;
  trajectory.poses[0].orientation.x = 0;
  client.sendGoal(trajectory);
  client.waitForResult();
*/

  ROS_INFO("READY TO MOVE");
  //robot.move_to_point(APoseToReach1,"base_link", 0.1, client); //Move to home position

  while (ros::ok())
  {
    ros::spinOnce();
    loop_rate.sleep();
  }

  ROS_INFO("Program termination.");

  //translateGripperX(-0.2,APoseToReach1,APoseToReach2);


  ros::shutdown();
  std::cout << "Done!" << std::endl;
  return 0;
}
