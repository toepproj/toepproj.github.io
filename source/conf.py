# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Toeplitz Project'
copyright = '2022, Toeplitz Project contributors'
author = 'Toeplitz Project contributors'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = project

html_favicon = '_static/img/dark_icon_32.ico'

html_theme_options = {
    'sidebar_hide_name': False,
    "light_logo": "img/222_logo.png",
    "dark_logo": "img/ddd_logo.png",
}
