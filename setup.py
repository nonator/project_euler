from setuptools import setup, find_packages

setup(
    name='project_euler',
    version='0.0.1',
    author='Noah Biederbeck',
    author_email='noah.biederbeck@tu-dortmund.de',
    description='Solutions for Project Euler',
    license='MIT',
    packages=find_packages(),
    # install_requires=[],
    # entry_points={},
    setup_requires=['pytest-runner'],
    test_requires=['pytest'],
)
