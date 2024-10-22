
rmdir .\maltechnology\__pycache__ /s /q
rmdir .\usuarios\__pycache__ /s /q
rmdir .\usuarios\migrations\__pycache__ /s /q
rmdir .\usuarios\migrations\__pycache__ /s /q
del .\usuarios\migrations\*.py /s

@REM python manage.py makemigrations usuarios 
@REM python manage.py migrate
