from django.db import models
from records.constants import field_sizes # importing constant objects to be used for values
from login.models import Person

class Tokens( models.Model ):
    """
        The Token model to store the tokens for validating an user 
    """
    login_id = models.ForeignKey( Person,  on_delete = models.CASCADE )
    Tokens = models.TextField(null=False,unique=True)
    

    class Meta:
        db_table = "Tokens"
        app_label = "records"