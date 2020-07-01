# Custom Users

There are two ways to extend users in Django: the "profile" method and a custom user.
This project is simply about implementing a custom user from the ground up.

The home page should show:

-   `username` and `display name` of the person who is logged in
-   Output the value of `settings.AUTH_USER_MODEL`

The custom user field has the following nullable fields:

-   Homepage **(URLField)**
-   Display Name **(CharField)**
-   Age **(IntegerField)**

## Installation

1. Use the package manager [poetry](https://python-poetry.org/) to start a virtual environment:

```bash
    poetry shell
```

2. Then, install all the dependencies required for this project:

```bash
    poetry install
```

3. Run the respective migrations:

```bash
    python manage.py migrate
```

4. Finally, run the server with the following command:

```bash
    python manage.py runserver
```
