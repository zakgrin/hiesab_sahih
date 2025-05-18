"""conf file"""

from datetime import datetime

# Project information:
project = "Hiesab in Islam"
author = ": ابن يوسف زكريا الطرابلسي"
disclaimer = "Third-party components are copyrighted by their respective authors"
copyright = f"{datetime.now().year}, {author}. {disclaimer}"
master_doc = "cover"
language = "ar"


# Remove warnings:
suppress_warnings = [
    "myst.domains",
]

exclude_patterns = [
    "**.ipynb_checkpoints",
    ".DS_Store",
    "Thumbs.db",
    "_build",
]

bibtex_bibfiles = ["references.bib"]
comments_config = {
    "hypothesis": False,
    "utterances": False,
}
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_design",
    "sphinx_book_theme",
    "sphinxcontrib.bibtex",
    "sphinx_jupyterbook_latex",
]


toc_object_entries_show_parents = "hide"
external_toc_exclude_missing = True
external_toc_path = "_toc.yml"

html_baseurl = ""
html_css_files = ["custom.css"]
html_favicon = ""
html_logo = ""
html_show_copyright = False
html_sourcelink_suffix = ""
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "search_bar_text": "               بحث",
    "launch_buttons": {
        "notebook_interface": "classic",
        "binderhub_url": "",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
        "deepnote_url": "",
    },
    "path_to_docs": "docs",
    "repository_url": "https://github.com/zakgrin/hiesab_in_islam",
    "repository_branch": "main",
    "extra_footer": "",
    "home_page_in_toc": False,
    "announcement": "",
    "analytics": {
        "google_analytics_id": "",
        "plausible_analytics_domain": "",
        "plausible_analytics_url": "https://plausible.io/js/script.js",
    },
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
}
html_title = " الحساب الصحيح من بنيان الحكم الرشيد <br> <small> تأليف: <br> ابن يوسف زكريا الطرابلسي </small> "
latex_engine = "pdflatex"
myst_enable_extensions = [
    "attrs_block",
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_url_schemes = ["mailto", "http", "https"]
nb_execution_allow_errors = False
nb_execution_cache_path = ""
nb_execution_excludepatterns = []
nb_execution_in_temp = False
nb_execution_mode = "force"
nb_execution_timeout = 30
nb_output_stderr = "show"
numfig = True
pygments_style = "sphinx"

use_jupyterbook_latex = True
use_multitoc_numbering = True


# html_sidebars = {
#     "**": ["searchbox.html"],
# }

# singlehtml_sidebars = {
#     "secondary": ["searchbox.html"],
# }
