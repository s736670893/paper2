@ECHO OFF
CLS
REM *****************************************************************
REM *                                                               *
REM *                    CiteSpace                                  *
REM *                                                               * 
REM *   RAM:                                                        *
REM *     -Xms1g: request at least 1GB ram for Java Virtual Machine *
REM *     -Xmx1g: request at most 1GB, depending on your computer   *
REM *     -Xss5m: request 5MB ram for Java stack                    *
REM *   Localte:                                                    *
REM *     US: US/en         UK: GB/en        Portuguese: BR/pt      *
REM *     Chinese: CN/zh    German: DE/de    Korean: KR/ko          *
REM *                                                               *
REM *****************************************************************

ECHO.
ECHO Enter the number of your locale from the following options:
ECHO   1 - USA: US, en
ECHO   2 - Chinese: CN, zh
ECHO   3 - Any Other Locale, i.e. country/language
ECHO   4 - Exit
ECHO.
CHOICE /C:1234

IF errorlevel 4 EXIT
IF errorlevel 3 goto THREE
IF errorlevel 2 goto TWO
IF errorlevel 1 goto ONE

:ONE
ECHO. 
ECHO Starting CiteSpace ......
java -Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
EXIT

:TWO
ECHO. Starting CiteSpace ......
java -Dfile.encoding=UTF-8 -Duser.country=CN -Duser.language=zh -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
EXIT

:THREE
ECHO. Starting CiteSpace ......
java -Dfile.encoding=UTF-8 -Duser.country=US -Duser.language=en -Xms1g -Xmx4g -Xss5m -jar CiteSpaceV.jar 
EXIT