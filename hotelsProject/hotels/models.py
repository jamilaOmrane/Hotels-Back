from djongo import models

# Create your models here.
class Hotel(models.Model):
    _id = models.ObjectIdField()
    hotel_class = models.FloatField()
    index = models.IntegerField()
    locality = models.CharField(max_length= 100)
    name = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 20)
    postal_code = models.CharField(max_length= 10)
    region = models.CharField(max_length= 20)
    region_id = models.IntegerField()
    street_address = models.CharField(max_length= 200)
    _type = models.CharField(max_length= 50)
    url = models.CharField(max_length= 500)

    def __str__(self):
        return ('name: '+self.name)