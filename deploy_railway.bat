@echo off
REM ========================================
REM Railway CLI automated deployment script
REM ========================================

REM Step 0: Activate your Python virtual environment
echo Activating virtual environment...
call "C:\Users\Syed Qasim Bukhari\Desktop\blog\venv\Scripts\activate.bat"

REM Step 1: Log in to Railway CLI
echo Logging in to Railway CLI...
railway login
IF %ERRORLEVEL% NEQ 0 (
    echo Railway login failed. Exiting.
    exit /b 1
)

REM Step 2: Link to Railway project
echo Linking local folder to Railway project...
railway link
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to link project. Make sure you select blog-project-repo.
    exit /b 1
)

REM Step 3: Run Django migrations
echo Running Django migrations on Railway...
railway run python manage.py migrate
IF %ERRORLEVEL% NEQ 0 (
    echo Migrations failed. Exiting.
    exit /b 1
)

REM Step 4: Collect static files
echo Collecting static files...
railway run python manage.py collectstatic --noinput
IF %ERRORLEVEL% NEQ 0 (
    echo Collectstatic failed. Exiting.
    exit /b 1
)

REM Step 5: Optional: create superuser
REM railway run python manage.py createsuperuser

REM Step 6: Restart Railway deployment
echo Restarting Railway deployment...
railway restart
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to restart Railway deployment. Exiting.
    exit /b 1
)

echo ========================================
echo Deployment complete! Open your app at:
echo https://blog-project-repo-production.up.railway.app/
echo ========================================
pause