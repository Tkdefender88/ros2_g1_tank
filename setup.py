from setuptools import setup
import os
from glob import glob

package_name = 'ros2_g1_tank'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'description'), glob('description/*.xacro'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='juicetin',
    maintainer_email='tkdefender@protonmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "motors = ros2_g1_tank.motorNode:main"
        ],
    },
)
