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


class Users(models.Model):

    class Meta:
        db_table = 'user_file'
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'

    userID = models.BigIntegerField(primary_key=True)
    user_name = models.TextField()
    user_login = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.TextField()
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_sraff = models.BooleanField()
    is_superuser = models.BooleanField()
    first_login = models.DateTimeField()
    lastJoin = models.DateTimeField()
    dateJoin = models.DateTimeField()

    def __str__(self):
        return f'{self.email}, {self.user_login}'


class Profile(models.Model):

    class Meta:
        db_table = 'profile'
        verbose_name = 'данные пользователя'

    id = models.BigIntegerField()
    user_id = models.BigIntegerField(primary_key=True)
    user_login = models.TextField()
    city = models.TextField()
    education = models.TextField()
    university = models.TextField()
    sex = models.CharField(max_length=1)
    born_date = models.DateField()
    job = models.TextField()
    job_position = models.TextField()
    receipt_date = models.DateField()
    bio = models.TextField()
