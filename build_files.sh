
echo "BUILD START"
pip3 install --upgrade pip --break-system-packages
pip3 install -r requirements.txt --break-system-packages
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"
