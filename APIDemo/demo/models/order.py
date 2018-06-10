import uuid
from django.db import models


class Order(models.Model):
    """
    order
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, verbose_name='用户')
    type_class = models.CharField(max_length=64, verbose_name='类别')
    img1 = models.ImageField(
        upload_to='upload/' + str(uuid.uuid4()) + '/',
        null=False,
        blank=False,
        verbose_name='图片1')
    img2 = models.ImageField(
        upload_to='upload/' + str(uuid.uuid4()) + '/',
        null=True,
        blank=True,
        verbose_name='图片2')
    img3 = models.ImageField(
        upload_to='upload/' + str(uuid.uuid4()) + '/',
        null=True,
        blank=True,
        verbose_name='图片3')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'sys_order'

    def __str__(self):
        return "{}".format(self.name)
