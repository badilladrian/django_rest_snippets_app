from django.db import models

# Create your models here.
#Bank of choices
GENDER_CHOICES = (
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('binary','BINARY'),
)
MARITAL_STATUS_CHOICES = (
    ('single','SINGLE'),
    ('maried', 'MARIED'),
)
SCHEDULE_CHOICES = (
    ('morning','MORNING'),
    ('afternoon', 'AFTERNOON'),
    ('night','NIGHT'),
)

class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
    cedula = models.BigIntegerField()
    date_of_entry = models.DateField()
    date_of_birth = models.DateField()
    id_unique= models.CharField(max_length=255)
    email = models.EmailField(max_length = 254) 
    nationality = models.CharField(max_length=255)
    telephone_number = models.BigIntegerField()
    schedule = models.CharField(choices=SCHEDULE_CHOICES, max_length=25)
    picture = models.ImageField(blank=True)
    #language = models.CharField(max_length=255)
    #salary_rate = models.PositiveIntegerField()

    def get_full_name(first, middle, last):
        space = " "
        self.full_name = first+space+middle+space+last+space
        return self.full_name

    def __str__(self):
        name = get_full_name(self.first_name,self.middle_name,self.last_name)
        id = "ID: "+ self.id_unique
        return name + id
         

    class Meta:
         db_table = 'Employees' 
         # Le doy de nombre 'Empleados' 
         # a nuestra tabla en la Base de Datos