https://code.djangoproject.com/ticket/30475#ticket

Setup
-----

python -m venv venv
pip install -r requirements.txt
. venv/bin/activate
./manage.py runserver


Case 1, correct behaviour
-------------------------

With DEBUG=True

http://127.0.0.1:8000/
    -> 404 page not found, correct

http://127.0.0.1:8000/test/
    -> redirect to the default language URL "/de/test/", correct output


Case 2, incorrect behaviour
---------------------------

With DEBUG=False

http://127.0.0.1:8000/
    -> just a Server Error 500, no backtrace in server log
    excepted outcome:
        backtrace in server log, as the Django test client does

http://127.0.0.1:8000/test/
    -> just a Server Error 500, no backtrace in server log

http://127.0.0.1:8000/en/test/
    -> correct output
