from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class CallRecord(models.Model):
    '''
     Model class representing table in the database for storing call records
    '''
    from_number = models.PositiveIntegerField()
    to_number = models.PositiveIntegerField()
    start_time = models.DateTimeField(auto_now_add=True)

    def clean(self) -> None:
        """
        validation method to ensure that from_number and to_number
        have not more than 15 digits.
        """

        if len(str(self.to_number)) > 15 or len(str(self.from_number)) > 15:
            raise ValidationError("Number cant exceed 15 digits")
        