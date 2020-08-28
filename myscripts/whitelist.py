#!/usr/bin/env python3
import yaml
import os

# for subdir, dirs, files in os.walk('./'):
#     for file in files:
#         #print os.path.join(subdir, file)
#         filepath = subdir + os.sep + file

#         if filepath.endswith(".yaml"):
for subdir, dirs, files in os.walk('kinetic/'):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".yaml"):
            if 'source' not in file:
                print(filepath)      
                stream = open(filepath, 'r')
                data = yaml.load(stream, Loader=yaml.FullLoader)
                print(data)
                data['package_whitelist'] = ['apr', 'pkg-config', 'message_runtime', 'catkin', 'rosconsole', 'python-rosdep', 'ros_environment', 'python3-empy', 'genpy', 'boost', 'xmlrpcpp', 'roslib', 'rosgraph_msgs', 'cmake', 'cpp_common', 'rosunit', 'gtest', 'python-rospkg', 'python-empy', 'genlisp', 'python', 'python-mock', 'geneus', 'python3-nose', 'message_generation', 'rospack', 'gencpp', 'python-yaml', 'roscpp_serialization', 'python3-mock', 'genmsg', 'python-argparse', 'python-nose', 'std_msgs', 'roslang', 'python-coverage', 'log4cxx', 'rosbuild', 'tinyxml', 'cmake_modules', 'google-mock', 'python3-catkin-pkg', 'rostime', 'roscpp_traits', 'gennodejs', 'python-catkin-pkg', 'rosmake', 'libconsole-bridge-dev']
                with open(filepath, 'w') as f:
                    yaml.dump(data, f)
            # if 'source' in file:
            #     print(filepath)      
            #     stream = open(filepath, 'r')
            #     data = yaml.load(stream, Loader=yaml.FullLoader)
            #     print(data)
            #     data['repository_whitelist'] = ['ros_comm', 'ros_comm_msgs', 'genpy', 'std_msgs', 'ros', 'gencpp', 'cmake_modules', 'geneus', 'genlisp', 'rospack', 'ros_environment', 'rosconsole', 'genmsg', 'catkin', 'gennodejs', 'message_runtime', 'message_generation', 'roscpp_core']
            #     del data['package_whitelist']
            #     with open(filepath, 'w') as f:
            #         yaml.dump(data, f)
