#!/usr/bin/env python3

import catkin_pkg
import catkin_pkg.package
import catkin_pkg.topological_order
import yaml

#make package xml file with correct contents
#make a package from the xml file
#use that package and find dependencies using path

# file_name = "foxy-cache.yaml"
# file_name = "noetic-cache.yaml"
# file_name = "melodic-cache.yaml"
file_name = "kinetic-cache.yaml"

stream = open(file_name, 'r')
data = yaml.load(stream, Loader=yaml.FullLoader)
pack = data['release_package_xmls']
packages = dict()
for name, xmlstr in pack.items():
    packages[name] = catkin_pkg.package.parse_package_string(xmlstr)
dependencies = set()
q_check = []
pack_dep = dict()
#get direct dependencies of current packages
def add_to_set(name,lis):
    for dep in lis:
        pack_dep[name].add(dep.name)
        if dep.name not in dependencies: #if you haven't seen it already
            dependencies.add(dep.name)
            q_check.append(dep.name)
def add_check(name):
    # use start package given and find all it's dependencies
    # add them to dependecies set and the q_check
    # pop first one off q and repeat until q empty and add to dependencies
    # print(name)
    pack_dep[name] = set()
    if name in packages.keys(): #do i need to include ones not in release package xmls
        add_to_set(name,packages[name].build_depends)
        add_to_set(name,packages[name].build_export_depends)
        add_to_set(name,packages[name].buildtool_depends)
        add_to_set(name,packages[name].buildtool_export_depends)
        add_to_set(name,packages[name].doc_depends)
        add_to_set(name,packages[name].exec_depends)
        add_to_set(name,packages[name].test_depends)
    #else:
        # dependencies.add(name)
def queue():
    while True: #check if empty
        if q_check == []:
            break
        name = q_check.pop(0)
        add_check(name)
add_check('roscpp')
queue()
dependencies_two = set()
for key in pack_dep:
    dependencies_two = dependencies_two.union(pack_dep[key])

print(len(dependencies), len(dependencies_two),dependencies)

# Resolve repository names from package names in dependencies.
repository_dependencies = set()
for name, data in data['distribution_file'][0]['repositories'].items():
  if 'release' in data and 'packages' in data['release']:
    # is any dependency package in data['release']['packages']?
    if set(data['release']['packages']) & dependencies:
       repository_dependencies.add(name)
  else: # only one package in repo
    if name in dependencies:
       repository_dependencies.add(name)

print('Repositories of dependencies for source-build files')
print(repository_dependencies)

#depend = catkin_pkg.topological_order.topological_order_packages(packages)
#print([t[0] for t in depend])
