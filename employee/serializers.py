from rest_framework import serializers
from .models import Employee, GENDER_CHOICES, MARITAL_STATUS_CHOICES, SCHEDULE_CHOICES

#This are constructors of the models - Serializers
class EmployeeSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    full_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(choices=GENDER_CHOICES, max_length=25)
    marital_status = serializers.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
    cedula = serializers.BigIntegerField()
    date_of_entry = serializers.DateField()
    date_of_birth = serializers.DateField()
    id_harmond = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length = 254) 
    nationality = serializers.CharField(max_length=255)
    telephone_number = serializers.BigIntegerField()
    schedule = serializers.CharField(choices=SCHEDULE_CHOICES, max_length=25)
    picture = serializers.ImageField()

    #To create itself
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    #To Update itself
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = serializers.CharField(max_length=255)
        instance.middle_name = serializers.CharField(max_length=255)
        instance.last_name = serializers.CharField(max_length=255)
        instance.full_name = serializers.CharField(max_length=255)
        instance.gender = serializers.CharField(choices=GENDER_CHOICES, max_length=25)
        instance.marital_status = serializers.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
        instance.cedula = serializers.BigIntegerField()
        instance.date_of_entry = serializers.DateField()
        instance.date_of_birth = serializers.DateField()
        instance.id_unique = serializers.CharField(max_length=255)
        instance.email = serializers.EmailField(max_length = 254) 
        instance.nationality = serializers.CharField(max_length=255)
        instance.telephone_number = serializers.BigIntegerField()
        instance.schedule = serializers.CharField(choices=SCHEDULE_CHOICES, max_length=25)
        instance.picture = serializers.ImageField()

        instance.save()
        return instance

    