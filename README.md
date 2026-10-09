# farm_world

English | [简体中文](README.zh-CN.md)

A farm environment for mobile robot simulation, featuring fields, roads, buildings, vegetation, and an obstacle course.

If you find this project useful, a star would be appreciated.

https://github.com/user-attachments/assets/1bd8ca30-7f76-465e-9e34-2b9442a16091

## Requirements

- ROS 2 Humble
- Gazebo Classic 11
- Git LFS

## Installation

Install and initialize Git LFS:

```bash
sudo apt update
sudo apt install git-lfs
git lfs install
```

Clone the package into your workspace's `src/` directory:

```bash
git clone https://github.com/max-niuniu/farm_world.git
git -C farm_world lfs pull
```

From the workspace root, install dependencies and build:

```bash
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select farm_world
source install/setup.bash
```

## Usage

```bash
ros2 launch farm_world world.launch.py
```

Run without the graphical client:

```bash
ros2 launch farm_world world.launch.py gui:=false
```

| Argument | Default | Description |
| --- | --- | --- |
| `gui` | `true` | Start the Gazebo graphical client. |
| `paused` | `false` | Start with simulation paused. |
| `verbose` | `false` | Enable verbose logging. |
| `world` | Package `worlds/farm.world` | World file to load. |

## Integration

Declare the dependency in your package's `package.xml`:

```xml
<exec_depend>farm_world</exec_depend>
```

Include the environment in a launch file:

```python
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution([
                FindPackageShare('farm_world'), 'launch', 'world.launch.py',
            ])),
            launch_arguments={'gui': 'true'}.items(),
        ),
    ])
```

If your application already starts Gazebo, use this package's `worlds/farm.world`
as its world file. Launch robot and navigation nodes separately with `use_sim_time` enabled.

## Coordinates

The world is named `farm_world` and the scene model is named `farm`.
Coordinates are in metres, with Z pointing up. The origin is on the ground of
the obstacle course beside the shed, at `z=0`.
Spawn robots at `(x, y) = (0, 0)` with a Z height appropriate for their dimensions
and initial pose.

## License

The integration code is licensed under [MIT](LICENSE). This license does not
cover third-party models or textures. See [NOTICE.md](NOTICE.md) for asset
sources and licensing status.

## Maintainer

Tianwei Niu — <tianwei.niu@cau.edu.cn>
