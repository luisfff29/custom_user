# Custom Users

There are two ways to extend users in Django: the "profile" method and a custom user.
This project is simply about implementing a custom user from the ground up.

The home page should show:

- `username` and `display name` of the person who is logged in
- Output the value of `settings.AUTH_USER_MODEL`

Extend the custom user field so that it has the following nullable fields:

- Homepage **(URLField)**
- Display Name **(CharField)**
- Age **(IntegerField)**
