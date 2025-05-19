```python
jupyter-book build --all jupyterbook
jupyter-book build --all --builder pdfhtml jupyterbook/
jupyter-book config sphinx jupyterbook # to create conf.py
sphinx-build jupyterbook jupyterbook/_build/html -a -b html
```