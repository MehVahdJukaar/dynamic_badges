############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.pygithub.com>          #
# Copyright 2018 Morgan Goose <morgan.goose@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <pygithub@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.pygithub.com>        #
# Copyright 2023 Liuyang Wan <tsfdye@gmail.com>                                #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

import datetime
import glob
import os
import re
import sys
from typing import Iterable

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(".."))
from importlib.metadata import version  # noqa: E402

setupVersion = version("pygithub")

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.mathjax"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "PyGithub"
copyright = "%d, Vincent Jacques" % datetime.date.today().year

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = setupVersion
# The full version, including alpha/beta/rc tags.
release = setupVersion

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
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

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "PyGithubdoc"


# -- Options for LaTeX output --------------------------------------------------

# latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
# 'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
# 'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
# 'preamble': '',
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "PyGithub.tex", "PyGithub Documentation", "Vincent Jacques", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "pygithub", "PyGithub Documentation", ["Vincent Jacques"], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "PyGithub",
        "PyGithub Documentation",
        "Vincent Jacques",
        "PyGithub",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

autodoc_default_flags = ["members"]
autodoc_member_order = "bysource"
autoclass_content = "both"

githubObjectTypes = {
    variation
    for object_type in ["GithubObject", "CompletableGithubObject", "NonCompletableGithubObject"]
    for variation in [object_type, "GithubObject." + object_type, "pygithub.GithubObject." + object_type]
}
githubObjectClasses: dict[str, str] = {}


def collect_classes(types: set[str]) -> Iterable[tuple[str, str]]:
    def get_base_classes(class_definition: str) -> Iterable[str]:
        if "(" in class_definition and ")" in class_definition:
            for base in class_definition[class_definition.index("(") + 1 : class_definition.index(")")].split(","):
                yield base.strip()
        else:
            return []

    for filename in sorted(glob.glob("../pygithub/*.py")):
        module = f"pygithub.{filename[10:-3]}"
        with open(filename) as r:
            for line in r.readlines():
                if line.startswith("class ") and any([base in types for base in get_base_classes(line)]):
                    class_name = re.match(r"class (\w+)[:(]", line).group(1)
                    if class_name not in types:
                        yield class_name, f"{module}"


# get all classes derived from GithubObject classes directly
classes = list(collect_classes(githubObjectTypes))
while classes:
    githubObjectClasses.update(classes)
    # get all classes derived from detected classes
    githubObjectTypes.update(
        {
            variation
            for object_type in [cls for cls, _ in classes]
            for variation in [object_type, "GithubObject." + object_type, "pygithub.GithubObject." + object_type]
        }
    )
    classes = list(collect_classes(set(githubObjectTypes)))

with open("github_objects.rst", "w") as f:
    f.write("Github objects\n")
    f.write("==============\n")
    f.write("\n")
    f.write(".. autoclass:: pygithub.GithubObject.GithubObject()\n")
    f.write("\n")
    f.write(".. toctree::\n")
    for githubObjectClass in sorted(githubObjectClasses.keys()):
        f.write("   github_objects/" + githubObjectClass + "\n")

for githubObjectClass, module in githubObjectClasses.items():
    with open("github_objects/" + githubObjectClass + ".rst", "w") as f:
        f.write(githubObjectClass + "\n")
        f.write("=" * len(githubObjectClass) + "\n")
        f.write("\n")
        f.write(".. autoclass:: " + module + "." + githubObjectClass + "()\n")

methods = dict()
githubObjectClasses.update([("MainClass", "pygithub.MainClass")])
githubObjectClasses.update([("GithubIntegration", "pygithub.GithubIntegration")])
for githubObjectClass, module in githubObjectClasses.items():
    with open("../" + module.replace(".", "/") + ".py") as f:
        method = None
        isProperty = False
        for line in f:
            line = line.rstrip()
            if line == "    @property":
                isProperty = True
            if line.startswith("    def "):
                if not isProperty:
                    method = line.split("(")[0][8:]
                    if method in [
                        "_initAttributes",
                        "_useAttributes",
                        "__init__",
                        "__create_pull_1",
                        "__create_pull_2",
                        "__create_pull",
                        "_hub",
                        "__get_FIX_REPO_GET_GIT_REF",
                        "__set_FIX_REPO_GET_GIT_REF",
                        "__get_per_page",
                        "__set_per_page",
                        "create_from_raw_data",
                        "dump",
                        "load",
                    ]:
                        method = None
                isProperty = False
            if line.startswith("        :calls: `"):
                for callee in line[16:].split(" or "):
                    verb, url = callee[1:].split(" ")[0:2]
                    if url not in methods:
                        methods[url] = dict()
                    if verb not in methods[url]:
                        methods[url][verb] = set()
                    methods[url][verb].add(":meth:`" + module + "." + githubObjectClass + "." + method + "`")
                method = None

methods["/markdown/raw"] = dict()
methods["/markdown/raw"]["POST"] = ["Not implemented, see ``/markdown``"]
methods["/rate_limit"] = dict()
methods["/rate_limit"]["GET"] = ["Not implemented, see `Github.rate_limiting`"]

with open("apis.rst", "w") as apis:
    apis.write("APIs\n")
    apis.write("====\n")
    apis.write("\n")
    for url, verbs in sorted(methods.items()):
        apis.write("* ``" + url + "``\n")
        apis.write("\n")
        for verb in ["GET", "PATCH", "POST", "PUT", "DELETE"]:
            if verb in verbs:
                apis.write("  * " + verb + ": " + " or ".join(sorted(verbs[verb])) + "\n")
        apis.write("\n")