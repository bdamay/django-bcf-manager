git pull
python manage.py collectstatic --noinput
python manage.py migrate
cd frontend
npm install
npm run build
cd ..
