Urls to be tested:
    http://127.0.0.1:8000/api/booking/tables/
        supports both get and post
        get gives list of all booking objects
        post creates a new one
        fields are:
            name
            no_of_guests

    http://127.0.0.1:8000/api/menu-items/
        supports both get and post
        post requires a valid token
        fields are:
            title
            price
            inventory

    http://127.0.0.1:8000/api/menu-items/<int:pk>
        supports both get and delete
        delete requires a valid token
        deletion is done through id
        fields are:
            title
            price
            inventory

    http://127.0.0.1:8000/auth/users/
        supports get and post
        get requires a valid token
        post creates a new user
        fields are:
            username
            password
            re_password

    http://127.0.0.1:8000/api-token-auth/
        can be used to obtain a token for an existing user with post method
        fields are:
            username
            password

    http://127.0.0.1:8000/restaurant/
        home page for the restaurant application
        this page serves the static content this project requires



Notes:
    some of the views require permissions to access so make sure to either create a superuser or remove the "DjangoModelPermissions"
    from the permission_classes list

    Unit tests are located in the restaurant application folder within than in the subfolder named tests
        these can be run with the command "python manage.py test"

    you may also need to change the settings to your configuration of the mysql database as i used a different password than what was suggested

    thank you for your time and have a nice day!    