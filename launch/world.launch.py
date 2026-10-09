# SPDX-License-Identifier: MIT
"""Launch the farm environment in Gazebo Classic."""
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true',
                              description='Open the Gazebo graphical client.'),
        DeclareLaunchArgument('paused', default_value='false',
                              description='Start physics paused.'),
        DeclareLaunchArgument('verbose', default_value='false',
                              description='Enable Gazebo diagnostic output.'),
        DeclareLaunchArgument(
            'world',
            default_value=PathJoinSubstitution([
                FindPackageShare('farm_world'), 'worlds', 'farm.world']),
            description='Path to the world file.'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([
                FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py'])),
            launch_arguments={
                'world': LaunchConfiguration('world'),
                'gui': LaunchConfiguration('gui'),
                'pause': LaunchConfiguration('paused'),
                'verbose': LaunchConfiguration('verbose'),
                'server_required': 'true',
                'gui_required': 'true',
            }.items()),
    ])
