import datetime
from django.db import models

# Create your models here.
class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    password=models.TextField(null=True)
    Usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_login'
class user_register(models.Model):
    user_id=models.AutoField(primary_key=True)
    login_id=models.IntegerField()
    Name=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    Email=models.CharField(max_length=50)
    Address=models.TextField()
    class Meta:
        db_table='tbl_user_register'
class artist_register(models.Model):
    user_id=models.AutoField(primary_key=True)
    login_id=models.IntegerField()
    Name=models.CharField(max_length=50, null=True)
    phone_number=models.BigIntegerField(null=True)
    Email=models.CharField(max_length=50)
    Address=models.TextField()
    class Meta:
        db_table='tbl_artist'

class state(models.Model):
    state_id=models.AutoField(primary_key=True)
    country_id=models.IntegerField()
    state=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_state'

class district(models.Model):
    district_id=models.AutoField(primary_key=True)
    state_id=models.IntegerField()
    district=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_district'

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_category'
class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    category_id=models.IntegerField()
    product=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    image=models.CharField(max_length=50)
    description=models.TextField()
    features=models.TextField()
    painter_name=models.CharField(max_length=50)
    entry_date=models.DateTimeField(default=datetime.datetime.now)


    class Meta:
        db_table='tbl_product'
class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    product_id=models.IntegerField()
    amount=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50)
    entry_date=models.DateTimeField(default=datetime.datetime.now)
    user_login_id=models.IntegerField()
    check_no_order=models.IntegerField()
    class Meta:
        db_table='tbl_order'
class notification(models.Model):
    notification_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_notification'
class raw_materials(models.Model):
    raw_materials_id=models.AutoField(primary_key=True)
    raw_materials=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField()
    class Meta:
        db_table='tbl_raw_materials'
class artist_work(models.Model):
    artist_work_id=models.AutoField(primary_key=True)
    artist_work=models.CharField(max_length=50)
    description=models.TextField()
    image=models.CharField(max_length=50)
    artist_login_id=models.IntegerField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    class Meta:
        db_table='tbl_artist_work'
class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    complaint_subject=models.CharField(max_length=50)
    complaint=models.CharField(max_length=150)
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_complaint'

class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    feedback_subject=models.CharField(max_length=50)
    feedback=models.TextField()
    user_login_id=models.IntegerField()
    reply=models.CharField(max_length=50)
    class Meta:
        db_table='tbl_feedback'
class order_artist_work(models.Model):
    artist_order_id=models.AutoField(primary_key=True)
    artist_work_id=models.IntegerField()
    amount=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50)
    entry_date=models.DateTimeField(default=datetime.datetime.now)
    user_login_id=models.IntegerField()
    class Meta:
        db_table='tbl_order_artist_work'
class order_raw_materials(models.Model):
    raw_materials_order_id=models.AutoField(primary_key=True)
    raw_materials_id=models.IntegerField()
    amount=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50)
    entry_date=models.DateTimeField(default=datetime.datetime.now)
    artist_login_id=models.IntegerField()
    class Meta:
        db_table='tbl_order_raw_materials'
class work_comment(models.Model):
    comment_id=models.AutoField(primary_key=True)
    artist_work_id=models.IntegerField()

    comment=models.TextField()
    entry_date=models.DateTimeField(default=datetime.datetime.now)
    user_login_id=models.IntegerField()
    class Meta:
        db_table='tbl_work_comment'