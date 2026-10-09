cmake_minimum_required(VERSION 3.8)
project(farm_world)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch worlds models
  DESTINATION share/${PROJECT_NAME}
  PATTERN "__pycache__" EXCLUDE
  PATTERN "*.pyc" EXCLUDE)
install(FILES README.md README.zh-CN.md LICENSE NOTICE.md DESTINATION share/${PROJECT_NAME})
ament_environment_hooks(env-hooks/farm_world.dsv.in)

ament_package()
