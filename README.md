# PokeBerriesStatisticsApi
Api in charge to get all the berries statistics.

Maintainer: Humberto Reyes

# Software to install
- Python 3.8 or greater. 
- Or instead of install python globally, a virtual environment can be created:
  From the PokeBerriesStatisticsApi folder type this command: py -3 -m venv .venv. To activate the virtual environment: .venv\Scripts\activate. Now, any python version can be installed.

- Git 2.40

# Steps to run the API locally

1. In Windows, open the cmd terminal and get to the root folder where you want to place the repository.
2. Once there, clone the repository with this comman: git clone https://github.com/HumbertoReyesA/PokeBerriesStatisticsApi.git.
3. Change to the PokeBerriesStatisticsApi folder with "cd PokeBerriesStatisticsApi."
4. In the .flaskenv file, set the FLASK_DEBUG variable to True so the minimum change won't need to stop and restart the application every time.               Note: Set it to False when it goes to production environment.
5. Install all the requirements with this command: pip install -r requirements.txt
6. Now, to run the application, use the next command: flask run.
7. You will see something similar in your local console: 
   * Serving Flask app 'api'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 312-187-867
8. Now open your browser on http://127.0.0.1:5000.
9. In a few seconds you will see the Poke Berries Statistics in a JSON format.

# Testing
- To run the tests, from the console command line type: pytest tests.py.
- Pytest runs automatically all the unit tests available in the tests.py module.

# Warning
When running this API, sometimes the Pokeapi is not available and sends a 403 HTTP code indicating that it is Forbidden. Don't worry, the api catches this kind of exception.
