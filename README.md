Install
-------

    git clone git@github.com:febmuller/filmathon3000.git
    cd filmathon3000
    sudo pip3 install virtualenv
    virtualenv --python=python3 .
    bin/pip install -r requirements.txt

Run
---

    export FLASK_APP=film.py
    export FLASK_ENV=development
    bin/flask run
