# 0x00. AirBnB clone - The console

![Alt text](image.png)

### Description

This project is a simple implementation of the backend for an Airbnb-like platform, specifically focused
on managing user accounts and listing properties. It consists of three main components: User Management, Property
on creating and managing user accounts, listing properties, booking rooms, etc. It consists of
a single file called `console.py` which contains all the necessary code to interact with the system
from the command line interface (CLI).
The CLI allows users to perform actions such as registering new users, viewing existing users,
listing available properties, making reservations, checking on the status of their reservation,
and logging out from the session.

![Alt text](image-1.png)

### Usage

To use this program, you need Python installed in your machine along with pip. Once you have them
installed, follow these steps:

1. Clone or download the repository into any directory of your choice.
2. Open the terminal/command prompt at that location.
3. Make sure you are inside the folder named "airbnb_clone" (the parent
folder of the "console.py" script). You can check this by typing `ls`
or `dir` in Windows Command Prompt. If you see the contents of the "console.
py" file then you're in the right place.
4. Install the required packages by running `pip install -r requirements.txt`. This will install
all dependencies needed for the application to run properly.
5. Run the application using the command `python console.py`.
6. Now you should be able to start interacting with the system through the CLI.</s>

## Tasks

- 0. README, AUTHORS
- 1. Be pycodestyle compliant!
- 2. Unittests
- 3. BaseModel
- 4. Create BaseModel from dictionary
- 5. Store first object
- 6. Console 0.0.1
- 7. Console 0.1
- 8. First User
- 9. More classes!
- 10. Console 1.0

## Unitest

All files, classes, functions has been tested with unit tests
(test_* methods), and all must pass before merging. To run unittest,
you just need to execute the following command on the root directory:

'python3 -m unittest discover tests'

- Unit tests also pass in non-interactive mode
you just need to execute the following command on the root directory:

'echo "python3 -m unittest discover tests" | bash'

If everything is green, you can push your changes. Otherwise, fix what's broken until
everything turns green.
Note: The project uses a modified version of the Django test client which allows us to make requests
to our API without having to setup a full Django server. However, it does not support HTML views
which means we cannot use Django templates or any other Django specific features.
This limitation is due to the fact that Django is not installed as part of this project.
Instead, only Flask (and its testing utilities) are used.</s>

## Authors

- ENG. Mohamed Kamal
- ENG. Hossam Elsahafy
