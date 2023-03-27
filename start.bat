@echo off

call .env\Scripts\activate.bat
python ui__Launch.pyw
call deactivate