# Reproduced from `scienceplots`

import os  # pathlib.Path.walk not available in Python <3.12

import matplotlib.pyplot as plt

import socolors

from .styles_discovery import read_styles_in_folders

# register the bundled stylesheets in the matplotlib style library
socolors_path = socolors.__path__[0]
styles_path = os.path.join(socolors_path, "styles")

# Reads styles in /styles folder and all subfolders
stylesheets = read_styles_in_folders(styles_path)

# Update dictionary of styles - plt.style.library
plt.style.core.update_nested_dict(plt.style.library, stylesheets)
plt.style.core.available[:] = sorted(plt.style.library.keys())
