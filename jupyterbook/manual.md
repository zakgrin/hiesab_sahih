```python
jupyter-book build --all jupyterbook
jupyter-book build --all --builder pdfhtml jupyterbook/
jupyter-book build --all --builder pdfhtml jupyterbook/chapters/10/10_01.md
jupyter-book build --all --builder pdflatex jupyterbook/
jupyter-book config sphinx jupyterbook # to create conf.py
sphinx-build jupyterbook jupyterbook/_build/pdf -a -b pdfhtml
sphinx-build jupyterbook jupyterbook/_build/html -a -b html
```