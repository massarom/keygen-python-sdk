from importlib.metadata import version as pkg_version


# -- Project information -----------------------------------------------------

project = "keygen-python-sdk"
copyright = "2024-2025, Marcello Massaro"
author = "Marcello Massaro"
release = pkg_version("keygen-python-sdk")
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "pydantic": ("https://docs.pydantic.dev/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

autodoc_member_order = "groupwise"
# Show only class docstrings, which should call .. automethod:: __init__ if necessary
autoclass_content = "class"

# Show inheritance and private and special members.
autodoc_default_options = {
    "undoc-members": False,
    "private-members": False,  # _private
    "special-members": False,  # __special__
    "show-inheritance": True,
    "inherited-members": False,
    # The following attributes and methods are typically built-ins which are not
    # overridden. Therefore, we do not document them.
    "exclude-members": (
        "__abstractmethods__,__annotations__,"
        "__dataclass_fields__,__dataclass_params__,__post_init__,"
        "__dict__,__hash__,__init__,__match_args__,__module__,__slots__,__weakref__,"
        "model_computed_fields,model_config,model_fields"
    ),
}

# napoleon config
napoleon_preprocess_types = True
napoleon_attr_annotations = True
napoleon_use_param = True

# nitpicky fixes
nitpick_ignore = {
    ("py:class", "dataclasses.InitVar"),
    ("py:class", "InitVar"),
}
nitpick_ignore_regex = [
    ("py:class", r"annotated_types.*"),
    ("py:class", r"pathlib.*"),
    ("py:class", "Field"),
]

# Add any path that contains templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# copybutton customisations - exclude line-numbers, prompt characters, and outpus
copybutton_exclude = ".linenos, .gp, .go"
