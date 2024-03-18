# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TestRTDocs'
copyright = '2024, a.stratmann'
author = 'a.stratmann'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["exhale", "breathe", "myst_parser"]
breathe_projects = {"trtd": "../../docs/build/xml/"}
breathe_default_project = "trtd"
exhale_args = {
    "containmentFolder": "./api",
    "rootFileName": "reference.rst",
    "rootFileTitle": "Library API",
    "doxygenStripFromPath": "..",
    "createTreeView": True
}
primary_domain = 'cpp'
highlight_language = 'cpp'

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
