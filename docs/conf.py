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
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

% === GREEK LETTERS, ETC
\DeclareUnicodeCharacter{0394}{\ensuremath{\Delta}}
\DeclareUnicodeCharacter{03B1}{\ensuremath{\alpha}}
\DeclareUnicodeCharacter{03B4}{\ensuremath{\delta}}
\DeclareUnicodeCharacter{03B6}{\ensuremath{\zeta}}
\DeclareUnicodeCharacter{03B8}{\ensuremath{\theta}}
\DeclareUnicodeCharacter{03BC}{\ensuremath{\mu}}
\DeclareUnicodeCharacter{03C4}{\ensuremath{\tau}}
\DeclareUnicodeCharacter{03C6}{\ensuremath{\phi}}
\DeclareUnicodeCharacter{03C8}{\ensuremath{\psi}}
\DeclareUnicodeCharacter{03C9}{\ensuremath{\omega}}
% Superscripts
\DeclareUnicodeCharacter{00B2}{\ensuremath{^{2}}}
\DeclareUnicodeCharacter{00B3}{\ensuremath{^{3}}}
% Math operators and symbols
\DeclareUnicodeCharacter{00B0}{\ensuremath{^{\circ}}}
\DeclareUnicodeCharacter{00B1}{\ensuremath{\pm}}
\DeclareUnicodeCharacter{00D7}{\ensuremath{\times}}
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
% Arrows
\DeclareUnicodeCharacter{2190}{\ensuremath{\leftarrow}}
\DeclareUnicodeCharacter{2191}{\ensuremath{\uparrow}}
\DeclareUnicodeCharacter{2192}{\ensuremath{\rightarrow}}
\DeclareUnicodeCharacter{2193}{\ensuremath{\downarrow}}
% Dashes and punctuation
\DeclareUnicodeCharacter{2013}{\textendash}
\DeclareUnicodeCharacter{2014}{\textemdash}
\DeclareUnicodeCharacter{2026}{\textellipsis}
% Box-drawing characters (used in ASCII diagrams)
\DeclareUnicodeCharacter{2500}{-}
\DeclareUnicodeCharacter{2502}{|}
\DeclareUnicodeCharacter{2514}{-}
\DeclareUnicodeCharacter{2518}{-}
% Dot-above accented letters
\DeclareUnicodeCharacter{1E8B}{\ensuremath{\dot{x}}}
\DeclareUnicodeCharacter{1E8D}{\ensuremath{\ddot{x}}}
\DeclareUnicodeCharacter{1E8F}{\ensuremath{\dot{y}}}

% === FONTS
\usepackage{pifont} % for dingbats
\usepackage{marvosym} % for \Keyboard etc
% \usepackage{lmodern}
% \usepackage{newtxtext}
\usepackage[osf]{erewhon}% extension of Utopia, osf=old-style-figures
\usepackage[varqu,varl]{inconsolata}% sans typewriter
\usepackage[scaled=.95]{cabin}% sans serif
\usepackage[utopia,vvarbb]{newtxmath}
\usepackage{textcomp}% AFTER newtxtext to avoid clashes

% === MATH
\usepackage[intlimits]{amsmath}
\usepackage{amsfonts}
\usepackage{amsbsy}
\usepackage{fixmath}
\usepackage{mathtools}
\usepackage{amssymb}

% === UNITS
\usepackage{siunitx}
\sisetup{
  inter-unit-product={\,},
  number-unit-product={\,},
  output-decimal-marker = {.},
  exponent-product={\cdot},
  group-separator={},
  group-four-digits=false,
  round-mode=places,
}
\DeclareSIUnit\inch{in}
\DeclareSIUnit\foot{ft}
\DeclareSIUnit\feet{ft}
\DeclareSIUnit\lb{lb}
\DeclareSIUnit\lbf{lbf}
\DeclareSIUnit\slug{slug}
\DeclareSIUnit\rankine{\ensuremath{^\circ}R}
\DeclareSIUnit\fahrenheit{\ensuremath{^\circ}F}
\DeclareSIUnit\kilopond{kg\ensuremath{_\mathrm{f}}}
\DeclareSIUnit\knots{kts}

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
