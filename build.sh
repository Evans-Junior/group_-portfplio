# build.sh
#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt
python app.py

chmod +x build.sh
#start the app

./build.sh