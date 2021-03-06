cmake_minimum_required(VERSION 2.8.3)
project(c3_trajectory_generator)

find_package(
  catkin
  REQUIRED COMPONENTS
    nav_msgs
    actionlib
    message_runtime
    message_generation
    mil_msgs
    tf
    cmake_modules
    ros_alarms
    mil_tools
)

add_service_files(
  FILES
  SetDisabled.srv
)

find_package(Eigen 3 REQUIRED)

generate_messages(
    DEPENDENCIES
)

catkin_package(
  DEPENDS
    mil_msgs
    Eigen3
  CATKIN_DEPENDS
    nav_msgs
    actionlib
    message_runtime
    message_generation
    mil_msgs
    tf
    ros_alarms
    mil_tools
  INCLUDE_DIRS
    include
    ${Eigen_INCLUDE_DIRS}
  LIBRARIES
)

include_directories(include ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${Eigen_INCLUDE_DIRS})

add_executable(c3_trajectory_generator src/C3Trajectory.cpp src/node.cpp src/AttitudeHelpers.cpp)
target_link_libraries(c3_trajectory_generator ${catkin_LIBRARIES})
add_dependencies(c3_trajectory_generator ${catkin_EXPORTED_TARGETS})
add_dependencies(c3_trajectory_generator ${PROJECT_NAME}_generate_messages_cpp)
add_dependencies(
  ${PROJECT_NAME}
  mil_msgs_generate_messages_cpp
  ${catkin_EXPORTED_TARGETS}
)
set_target_properties(c3_trajectory_generator PROPERTIES COMPILE_FLAGS "-std=c++11 -O2")
