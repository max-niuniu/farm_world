# farm_world

[English](README.md) | 简体中文

用于移动机器人仿真的农场环境，包含农田、道路、建筑、植被及障碍物场地。

https://github.com/user-attachments/assets/1bd8ca30-7f76-465e-9e34-2b9442a16091

## 环境要求

- ROS 2 Humble
- Gazebo Classic 11
- Git LFS

## 安装

安装并初始化 Git LFS：

```bash
sudo apt update
sudo apt install git-lfs
git lfs install
```

在所需工作空间的 `src/` 下克隆本包：

```bash
git clone https://github.com/max-niuniu/farm_world.git
git -C farm_world lfs pull
```

在工作空间根目录安装依赖并构建：

```bash
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select farm_world
source install/setup.bash
```

## 启动

```bash
ros2 launch farm_world world.launch.py
```

无界面运行：

```bash
ros2 launch farm_world world.launch.py gui:=false
```

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `gui` | `true` | 启用 Gazebo 图形界面 |
| `paused` | `false` | 启动时暂停仿真 |
| `verbose` | `false` | 输出详细日志 |
| `world` | 包内 `worlds/farm.world` | 加载的 world 文件 |

## 集成到其他包

在使用方的 `package.xml` 中声明依赖：

```xml
<exec_depend>farm_world</exec_depend>
```

在 launch 文件中加载农场环境：

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

已有 Gazebo 启动入口时，将其 world 路径设为本包的 `worlds/farm.world`。
机器人及导航节点单独启动，并设置 `use_sim_time:=true`。

## 场景坐标

世界名称为 `farm_world`，场景模型名称为 `farm`。坐标单位为米，Z 轴向上。
原点位于仓棚旁的障碍物场地，地面高度为 `z=0`。
机器人可从 `(x, y) = (0, 0)` 生成，Z 高度按机器人尺寸和初始姿态设置。

## 许可证

集成代码采用 [MIT 许可证](LICENSE)。第三方模型与贴图不适用此许可，
来源及许可状态见 [NOTICE.md](NOTICE.md)。

## 维护者

Tianwei Niu — <tianwei.niu@cau.edu.cn>
