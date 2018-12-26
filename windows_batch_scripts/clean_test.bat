@echo off
Rem Equivalent for clean-test: ## remove test and coverage artifacts

if exist .tox\ rmdir /S /Q .tox\ >NUL;
if exist htmlcov\ rmdir /S /Q htmlcov\ >NUL;
del /S /F /Q .pytest_cache >NUL;
if exist  .coverage rmdir /S /Q .coverage >NUL;
del /S /F /Q .coverage >NUL;
