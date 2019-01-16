@echo off
Rem Equivalent for clean-build: ## remove build artifacts

if exist build\ rmdir /S /Q build\ >NUL;
if exist dist\ rmdir /S /Q dist\ >NUL;
if exist .eggs\ rmdir /S /Q .eggs\ >NUL;
for /d %%G in ("*.egg-info") do rmdir /s /q "%%~G" >NUL;
del /S /F /Q *.egg-info >NUL;
del /S /F /Q *.egg >NUL;
