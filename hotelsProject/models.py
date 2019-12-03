# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    codename = models.CharField()
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    date_joined = models.DateTimeField()
    email = models.CharField()
    first_name = models.CharField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    last_name = models.CharField()
    password = models.CharField()
    username = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    group_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    permission_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)
# Unable to inspect table 'customers'
# The error was: 'NoneType' object is not subscriptable


class DjangoAdminLog(models.Model):
    action_flag = models.IntegerField()
    action_time = models.DateTimeField()
    change_message = models.CharField()
    content_type_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.CharField()
    object_repr = models.CharField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    model = models.CharField()
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField()
    applied = models.DateTimeField()
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    expire_date = models.DateTimeField()
    session_data = models.CharField()
    session_key = models.CharField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'django_session'
# Unable to inspect table 'hotels'
# The error was: 'NoneType' object is not subscriptable


class HotelsHotel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    index = models.IntegerField()
    location = models.CharField()
    name = models.CharField()
    stars = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'hotels_hotel'
# Unable to inspect table 'reviews'
# The error was: 'NoneType' object is not subscriptable
