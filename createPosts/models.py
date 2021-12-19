from django.db import models


class Posts(models.Model):

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    id = models.BigIntegerField(primary_key=True)
    post = models.TextField()
    user_id = models.BigIntegerField()
    user_login = models.TextField()
    post_date = models.DateField()
