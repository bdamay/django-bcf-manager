git pull
python manage.py collectstatic --noinput
python manage.py migrate
cd frontend
call npm install
call npm run build
cd ..
