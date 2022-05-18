cs340 flask test starter app. on port 9286 on flip 3

How to run on bash in linux (after cloning repo): 
1: python3 -m venv ./venv 
2: source ./venv/bin/activate
3: pip3 install -r requirements.txt
4: python -m flask run -h 0.0.0.0 -p PORT --reload
                                     ^^^^
Change PORT to desired port. I am using 9286
