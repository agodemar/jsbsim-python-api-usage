# Configuration file for the Sphinx documentation builder.
#
# For a full list of configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# NOTE: This conf.py lives in docs/ but is used with the project root as the
# Sphinx source directory.  Run from the docs/ folder with:
#     make html
# which calls: sphinx-build -M html .. _build -c .

import os
import sys

# -- Path setup ---------------------------------------------------------------

sys.path.insert(0, os.path.abspath('..'))

# -- Project information ------------------------------------------------------

project   = 'JSBSim Python Examples'
copyright = '2026, <a href="https://github.com/agodemar/">Agostino De Marco</a> (<a href="https://www.linkedin.com/in/agostino-de-marco-08398a7">LinkedIn</a>)'
author    = 'Agostino De Marco'
release   = '1.0'
version   = '1.0'

# -- General configuration ----------------------------------------------------

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'myst_parser',
]

# The main document (relative to the project root, which is the source dir)
master_doc = 'index'

# Suppress execution: notebooks are pre-run by CI before the Sphinx build
nbsphinx_execute = 'never'

# Allow errors in notebooks so the doc build doesn't fail on import issues
nbsphinx_allow_errors = True

# Custom prolog that appears above every notebook page
nbsphinx_prolog = """
.. note::
   This page was generated from a Jupyter notebook.
"""

templates_path   = ['_templates']
exclude_patterns = [
    'docs/_build',        # Sphinx build output (relative to project-root sourcedir)
    'Thumbs.db',
    '.DS_Store',
    'README.md',          # not part of the doc tree
    '**/.ipynb_checkpoints',
]

# Ensure .md files are processed by myst_parser
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output --------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False,
}

html_static_path = ['_static']

html_title = 'JSBSim Python Examples'

# -- nbsphinx options ---------------------------------------------------------

# Timeout for notebook execution (seconds); only used when nbsphinx_execute != 'never'
nbsphinx_timeout = 600

# -- Options for LaTeX/PDF output ---------------------------------------------

latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
\usepackage{amsmath}
\usepackage{amssymb}
''',
}

latex_documents = [
    (
        master_doc,
        'JSBSimPythonExamples.tex',
        'JSBSim Python Examples',
        'Agostino De Marco',
        'manual',
    ),
]
