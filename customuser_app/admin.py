from django.contrib import admin
from customuser_app.models import MyUser
from django.contrib.auth.admin import UserAdmin


# From https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            None,              # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'homepage',
                    'display_name',
                    'age',
                ),
            },
        ),
    )


admin.site.register(MyUser, CustomUserAdmin)
