@echo off
Rem Equivalent for clean-pyc:  ## remove Python file artifacts

del /S /F /Q *.pyc >NUL;
del /S /F /Q *.pyo >NUL;
del /S /F /Q *~ >NUL;
del /S /F /Q __pycache__ >NUL;
