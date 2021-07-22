# -*- coding: utf-8 -*-
#
# cesar documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('../../src'))
import sphinx_rtd_theme


import cesarp

# enable git-lfs ressources on readthedocs
if not os.path.exists('./git-lfs'):
    os.system('wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.1/git-lfs-linux-amd64-v2.7.1.tar.gz')
    os.system('tar xvfz git-lfs-linux-amd64-v2.7.1.tar.gz')
    os.system('./git-lfs install')  # make lfs available in current repository
    os.system('./git-lfs fetch')  # download content from remote
    os.system('./git-lfs checkout')  # make local files to have the real content on them

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', "sphinx_rtd_theme", "sphinx.ext.autosectionlabel"]
autosectionlabel_prefix_document = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'cesar-p'
copyright = u"2021, Leonie Fierz, Urban Energy Systems Lab, Eidg. Materialprüfungsanstalt Empa"
author = u"Leonie Fierz"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = cesarp.__version__
# The full version, including alpha/beta/rc tags.
release = cesarp.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# ADDED api/modules.rst - this is just an additional layer of menu hierarchy we do not need but is generated by the api doc
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'api/modules.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# ADDED by leonie
# custom css - used that in HTML the tables do not have a horizontal scroll bar
# where possible, if class/module names are too long there will still be scroll bars
# this custom.css must be in the path specifeid by html_static_path
html_css_files  = ['custom.css']

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'cesardoc'


# -- Options for LaTeX output ------------------------------------------
#
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'inputenc': '',
    'utf8extra': '',
    'fontpkg': r'''
\usepackage{times}
''',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'cesar-p.tex',
     u'cesar-p Documentation',
     u'Leonie Fierz', 'manual'),
]

# format for the code-block elements - added by leonie
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter

# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cesar-p',
     u'cesar-p Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'cesar-p',
     u'cesar-p Documentation',
     author,
     'cesar-p',
     'Combined Energy Simulation and Retrofit - Python.',
     'Miscellaneous'),
]

def autodoc_skip_member(app, what, name, obj, skip, options):
    if name == '__init__':
        return False
    return skip

def run_apidoc(_):
    module = '../../../src/cesarp'
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    output_path = os.path.join(cur_dir,'api')
    cmd_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # Check to see if we are in a virtualenv
        # If we are, assemble the path manually
        cmd_path = os.path.abspath(os.path.join(sys.prefix, 'bin', 'sphinx-apidoc'))

    # -M option does place package description (from __init__.py) at the beginning of the page for a package
    # -f does overwrite existing files
    # -e put documentation for each module on its own page.
    # for list of all options for sphinx-apidoc see https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html
    subprocess.check_call([cmd_path, '-efM', '-o', output_path, module])

def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
    app.connect('builder-inited', run_apidoc)

