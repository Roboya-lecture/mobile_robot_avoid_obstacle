from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args1 = generate_distutils_setup(
    packages=['Pubmsg'],
    package_dir={'': 'src'}
)

setup(**setup_args1)

# fetch values from package.xml
setup_args2 = generate_distutils_setup(
    packages=['Submsg'],
    package_dir={'': 'src'}
)

setup(**setup_args2)
