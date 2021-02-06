# Setting-up the project

  * Download and install Python 3.7
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone  https://github.com/<your_user_name>/CityonBikes.git`
  * Change directory to CityonBikes `$ cd CityonBikes`
  * Install virtualenv `$ pip3 install virtualenv`
  * Create a virtual environment `$ virtualenv env -p python3.7`  
  * Activate the env: `$ source env/bin/activate` (for linux) `> .\env\Scripts\activate` (for Windows)
  * Install the requirements: `$ pip install -r requirements.txt`
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create admin `$  winpty python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`
This will start the project and you can view it on 127.0.0.1:8000.
