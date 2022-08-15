# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Basestack'
copyright = '2022, Basestack'
author = 'Brian Merritt'

release = '2.0.0'
version = '2.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_toolbox.collapse',
    'sphinx.ext.intersphinx',
    'linuxdoc.rstFlatTable'      # Implementation of the 'flat-table' reST-directive.
    , 'linuxdoc.rstKernelDoc'    # Implementation of the 'kernel-doc' reST-directive.
    , 'linuxdoc.kernel_include'  # Implementation of the 'kernel-include' reST-directive.
    , 'linuxdoc.manKernelDoc'    # Implementation of the 'kernel-doc-man' builder
    , 'linuxdoc.cdomain'         # Replacement for the sphinx c-domain.
    , 'linuxdoc.kfigure'         # Sphinx extension which implements scalable image handling.
]

localhost="localhost:5003"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
}
# -- Options for EPUB output
epub_show_urls = 'footnote'
