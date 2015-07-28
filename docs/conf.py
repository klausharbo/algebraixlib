#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Configuration file for our documentation build configuration file.

This file is execfile()d with the current directory set to its containing dir. Note that not all
possible configuration values are present in this file (originally auto-generated by
:command:`sphinx-quickstart`). All configuration values have a default; the default values are
shown in comments.

See also `The build configuration file <http://sphinx-doc.org/config.html>`_.
"""

# $Id: conf.py 22698 2015-07-28 17:09:23Z gfiedler $
# Copyright Algebraix Data Corporation 2015 - $Date: 2015-07-28 12:09:23 -0500 (Tue, 28 Jul 2015) $
#
# This file is part of algebraixlib <http://github.com/AlgebraixData/algebraixlib>.
#
# algebraixlib is free software: you can redistribute it and/or modify it under the terms of version
# 3 of the GNU Lesser General Public License as published by the Free Software Foundation.
#
# algebraixlib is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with algebraixlib.
# If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------------------------
import os
import sys

# --------------------------------------------------------------------------------------------------
# Release-related items

# Information about the project.
project = 'Algebraix Technology Core Library'
# noinspection PyShadowingBuiltins
copyright = '2015, Algebraix Data Corporation'
author = "Algebraix Data Corporation"

# The version info for the project you're documenting, acts as replacement for |version| and
# |release|, also used in various other places throughout the built documents.
version = '1.0'  # The short X.Y version.
release = '1.0'  # The full version, including alpha/beta/rc tags.

# --------------------------------------------------------------------------------------------------
# Project configuration

# If extensions (or modules to document with autodoc) are in another directory, add these
# directories to sys.path here. If the directory is relative to the documentation root, use
# os.path.abspath to make it absolute.
sys.path.insert(0, os.path.abspath('..'))

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and directories to ignore when
# looking for source files.
exclude_patterns = ['_build/*']

# Minimal Sphinx version. Accepts only the first two elements of the version number.
needs_sphinx = '1.3'  # Default '1.0'.

# Sphinx extension modules.
extensions = [  # Default []
    'sphinx.ext.autodoc',       # http://sphinx-doc.org/ext/autodoc.html
    'sphinx.ext.coverage',      # http://sphinx-doc.org/ext/coverage.html
    'sphinx.ext.doctest',       # http://sphinx-doc.org/ext/doctest.html
    'sphinx.ext.intersphinx',   # http://sphinx-doc.org/ext/intersphinx.html
    'sphinx.ext.mathjax',       # http://sphinx-doc.org/ext/math.html#module-sphinx.ext.mathjax
    'sphinx.ext.todo',          # http://sphinx-doc.org/ext/todo.html
    'sphinx.ext.viewcode',      # http://sphinx-doc.org/ext/viewcode.html
]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = 'any'  # Default: None

# Primary domain for explicit roles.
primary_domain = 'py'

# Provide additional diagnostic output.
nitpicky = True  # See also '-n' command line switch.

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

# The theme to use for HTML and HTML Help pages. See choice of themes in
# http://sphinx-doc.org/theming.html#builtin-themes.
html_theme = 'nature'


# sphinx.ext.autodoc -------------------------------------------------------------------------------

# Append the docstring of __init__() to the docstring of the class.
autoclass_content = 'both'

# Leave autodoc-generated source documentation in the order found in the source.
autodoc_member_order = 'bysource'

autodoc_default_flags = [
    'members',
    'undoc-members',
    'show-inheritance',
]


# A construct that allows us to add double-underscore functions selectively.
# (If we want to add all, we can add 'special-members' to autodoc_default_flags.)
#
# noinspection PyUnusedLocal
def skip_member(app, what, name, obj, skip, options):
    include_methods = [
        '__new__',
        '__str__', '__repr__',
        '__hash__', '__eq__', '__ne__', '__le__',
        '__contains__', '__call__', '__getitem__'
    ]
    if name in include_methods:
        return False
    return skip


def setup(app):
    app.connect('autodoc-skip-member', skip_member)


# sphinx.ext.intersphinx ---------------------------------------------------------------------------

# Reference the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3.4', None)}


# sphinx.ext.todo ----------------------------------------------------------------------------------

# If true, 'todo' and 'todoList' produce output, else they produce nothing.
todo_include_todos = True


# -- Auto-generated configuration and added interesting items --------------------------------------

# A string of reStructuredText that will be included at the beginning of every source file that is
# read. Could be interesting for including a common file in every other file.
# TODO Including a common file didn't work well.
# rst_prolog = '..include:: /include.rst\n\n'


# -- General configuration ------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
# We don't have templates (yet).
# templates_path = []

# The suffix(es) of source file names. You can specify multiple suffix as a list of string.
# source_suffix = ['.rst', '.md']

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some non-false value, then
# it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description unit titles (such as
# .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the output. They are ignored
# by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ----------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme further.  For a list
# of options available for each theme, see the documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to "<project> v<release>
# documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the docs.  This file
# should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here, relative to this
# directory. They are copied after the builtin static files, so a file named "default.css" will
# overwrite the builtin "default.css".
# html_static_path = []

# Add any extra paths that contain custom files (such as robots.txt or .htaccess) here, relative to
# this directory. These files are copied directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom, using the given
# strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to typographically correct
# entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will contain a <link> tag
# referring to it.  The value of this option must be the base URL from which the finished HTML is
# served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index. Sphinx supports the following
# languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja' 'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default. Now only 'ja' uses
# this config value.
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that implements a search
# results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
# htmlhelp_basename = ''

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples (source start file, target name,
# title, author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,                         # Source start file.
        'mathobjectspy.tex',                # Target name.
        'mathobjects.py Documentation',     # Title.
        'Algebraix Data Corporation',       # Author.
        'manual'                            # Document class.
    ),
]

# The name of an image file (relative to this directory) to place at the top of the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts, not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples (source start file, name, description, authors,
# manual section).
man_pages = [
    (
        master_doc,                         # Source start file.
        'mathobjectspy',                    # Name.
        'mathobjects.py Documentation',     # Description.
        [author],                           # Authors.
        1                                   # Manual section.
    ),
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples (source start file, target name,
# title, author, dir menu entry, description, category).
texinfo_documents = [
    (
        master_doc,                             # Source start file.
        'mathobjectspy',                        # Target name.
        'mathobjects.py Documentation',         # Title.
        author,                                 # Author.
        'mathobjectspy',                        # Dir menu entry.
        'One line description of project.',     # Description.
        'Miscellaneous'                         # Category.
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# -- Options for doctest --------------------------------------------------

# doctest_global_setup = """\
# import algebraixlib.mathobjects
# """
