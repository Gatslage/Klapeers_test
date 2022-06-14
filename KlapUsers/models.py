from tokenize import group
from typing_extensions import Required
import django
from django.db import models
from django.contrib.auth.models import AbstractUser,Group



class KlapGroups(Group):
    date_created=models.DateField(auto_now_add=True)
    member_max=models.IntegerField(default=100)

class KlapUser(AbstractUser):

    class state(models.TextChoices):
        CAMEROUN='CMR'
        NIGERIA='NG'
    class city(models.TextChoices):
        DOUALA='DL'
        LAGOS='LG'

    username=None
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'

    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=40)
    state=models.CharField(choices=state.choices,null=False,max_length=20)
    city=models.CharField(choices=city.choices,null=False,max_length=20)
    



class personnalUser(KlapUser):
    class sex(models.TextChoices):
        MASCULIN='M'
        FEMININ='F'
    birth_date=models.DateField()
    sex=models.CharField(choices=sex.choices,null=False,max_length=9)



class enterpriseCategory(models.Model):
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100,null=True)

class entrepriseUser(KlapUser):
    class status(models.TextChoices):
        SARL='SARL'
        SA='SA'

    enterprise_name=models.CharField(max_length=50)
    status=models.CharField(choices=status.choices,null=False,max_length=9)
    category=models.ForeignKey(enterpriseCategory,on_delete=models.SET_NULL,null=True,related_name='enterprise')

