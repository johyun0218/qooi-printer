@echo off
REM 현재 bat 파일이 있는 경로로 이동
cd /d %~dp0

REM 가상환경 활성화
call venv\Scripts\activate

REM Python 서버 백그라운드 실행
start "" python run.py
exit