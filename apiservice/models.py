# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     """
#     用户信息
#     """
#     gender_lst = (('male', '男'), ('female', '女'))
#     # username = models.CharField(max_length=20, unique=True)
#     nick_name = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=256)
#     phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
#     # email = models.EmailField(null=True, blank=True)
#     real_name = models.CharField(max_length=20, null=True, blank=True)
#     gender = models.CharField(max_length=10, choices=gender_lst, default="男")
#     age = models.IntegerField()
#     job = models.CharField(max_length=20, null=True, blank=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     update_time = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.username
#
#     class Meta:
#         verbose_name = "用户信息"
#         verbose_name_plural = verbose_name
#         ordering = ('id',)


class Collection(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=999)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        #     managed = True
        #     db_table = 'collection'
        ordering = ('order',)


class Api(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    collection = models.ForeignKey('Collection', models.DO_NOTHING)
    method = models.ForeignKey('Method', models.DO_NOTHING)
    protocol = models.ForeignKey('Protocol', models.DO_NOTHING)
    host = models.CharField(max_length=20)
    port = models.IntegerField()
    url = models.CharField(max_length=100)
    header = models.CharField(max_length=100, blank=True, null=True)
    params = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    order = models.IntegerField(blank=True, null=True, default=999)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        #     managed = True
        #     db_table = 'api'
        ordering = ('order',)


class Case(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    api = models.ForeignKey(Api, models.DO_NOTHING)
    header = models.CharField(max_length=100, blank=True, null=True)
    params = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    assertion = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        #     managed = True
        #     db_table = 'case'
        ordering = ['id']


class Result(models.Model):
    # id = models.IntegerField(primary_key=True)
    case = models.ForeignKey(Case, models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    header = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    assert_result = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        #     managed = True
        #     db_table = 'result'
        ordering = ['id']


class Method(models.Model):
    name = models.CharField(max_length=10)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        # managed = True
        # db_table = 'method'
        ordering = ['id']


class Protocol(models.Model):
    name = models.CharField(max_length=10)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_time = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        # managed = True
        # db_table = 'protocol'
        ordering = ['id']
