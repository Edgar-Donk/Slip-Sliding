# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Slip Sliding'
copyright = '2026, Edga Donk'
author = 'Edgar Donk'
release = '0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc",
    'sphinx.ext.napoleon',
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    'sphinx.ext.mathjax',
    'sphinx_copybutton',]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

pygments_style = 'sphinx'
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# pydata_sphinx_theme

html_theme_options = {
  "show_prev_next": True,
  # search bar options are ‘navbar’ and ‘sidebar’.
  "search_bar_position": "navbar", # sidebar
  #  "use_edit_page_button": True,
}

html_sidebars = {
    "contributing": ["sidebar-search-bs.html", "custom-template.html"],
    "changelog": [],
}

html_theme_options = {
   "logo": {
      "text": "Slip Sliding",
      "image_light": 'bigbenc.avif',
      "image_dark": "bigbencneon.avif",
   }
}

html_favicon = '_static/ben1.ico'

smartquotes = False

source_encoding = 'utf-8'

rst_prolog = f"""
.. role:: AL
    :class: keys
"""


#rst_epilog = f"""
#..role:: BT
#    :class: swim
#"""
