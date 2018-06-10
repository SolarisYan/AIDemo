from django.db import models
from demo.utils.image import ImageStorage


class References(models.Model):
    class Meta:
        db_table = 't_sys_references'

    ReferenceID = models.AutoField(
        max_length=11, db_column='ReferenceID', primary_key=True)
    SubmitTime = models.DateTimeField(
        db_column='SubmitTime', auto_now_add=True)
    UserID = models.ForeignKey(
        'AIUsers', on_delete=models.CASCADE, blank=False, default='')
    MainType = models.CharField(
        max_length=255, db_column='MainType', blank=False)
    SecondType = models.CharField(max_length=255, db_column='SecondType')
    OrgImage1 = models.ImageField(
        db_column='OrgImage1', upload_to='OrgImages', storage=ImageStorage())
    OrgImage2 = models.ImageField(
        db_column='OrgImage2', upload_to='OrgImages', storage=ImageStorage())
    OrgImage3 = models.ImageField(
        db_column='OrgImage3', upload_to='OrgImages', storage=ImageStorage())
    Description = models.CharField(max_length=500, db_column='Description')
    AIResult = models.CharField(max_length=1024, db_column='AIResult')
