from setuptools import setup, find_packages
import os, sys

stable = os.environ.get('PYGERBV_STABLE', "YES")
branch_name = os.environ.get('PYGERBV_BRANCH', None)

if stable == "YES":
    version_format = '{tag}'
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],
elif branch_name:
    version_format = '{tag}b{commitcount}+%s' % branch_name
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],
else:
    version_format = '{tag}b{commitcount}+{gitsha}'
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.6',
    ],

install_requires = []

# Add enum34 **ONLY** if necessary -- installing in 3.5+ will break things
if (sys.version_info.major < 3) or (sys.version_info.major == 3 and sys.version_info.minor < 4):
    install_requires.append('enum34')
         
setup(
    name = 'pygerbv',
    version_format=version_format,
    description = 'Python wrapper for libgerbv',
    url = 'https://github.com/holmosapien/PyGerbv',
    author = 'Elephantec',
    author_email = 'development@macrofab.com',
    license = 'Other/Proprietary License',
    classifiers = classifiers,
    packages = find_packages(),
    install_requires = install_requires,
    extras_require = {},
    package_data = {},
    data_files = [],
    entry_points = {},
    setup_requires=['setuptools-git-version']
)
