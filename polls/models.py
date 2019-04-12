from django.db import models
from django.utils.timezone import now


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now, editable=False)
    created_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

class Brand(models.Model):
    brand_name=models.CharField(max_length=30)
    brand_description=models.CharField(max_length=30)
    brand_contact = models.IntegerField(default=True)
    created_date = models.DateTimeField(default=now, editable=False)
    created_by = models.CharField(max_length=30)
    modi_by = models.CharField(max_length=100)
    status = models.BooleanField(default=False)


class ProductCategory(models.Model):
    product_category_name = models.CharField(max_length=100)

class Product_Models(models.Model):
    idname = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name=models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now,editable=False)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)

class Variant(models.Model):
    idnumber = models.ForeignKey(Product_Models, on_delete=models.CASCADE)
    variant_name=models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now,editable=False)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)

class FeatureMaster(models.Model):
    feature_name=models.CharField(max_length=100)
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now,editable=False)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)

class Feature_Varient(models.Model):
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(FeatureMaster, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now,editable=False)
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    Active = models.BooleanField(default=False)

class Items(models.Model):
    item_name=models.CharField(max_length=100)
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
    qr_Code=models.TextField()
    created_date = models.DateTimeField(default=now,editable=False)
    modified_date = models.DateTimeField(default=now,editable=False)
    Active = models.BooleanField(default=False)


class Sales(models.Model):
    sales_quantity=models.IntegerField(default=True)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)

    # sales_price=models.IntegerField(default=True)
    mrp=models.FloatField(default=True)
    discount=models.FloatField(default=True)
#
# class Services(models.Model):
#     service_type=models.CharField(max_length=100)
#     modified_date = models.DateTimeField(default=now,editable=False)
#     Active = models.BooleanField(default=False)
#     defected_part_name=models.CharField(max_length=100)
#     defected_part_number=models.IntegerField(default=False)
#     replaced_partid=models.IntegerField(default=False)
#     replaced_partname=models.CharField(default=False)
#     service_price=models.RealField(default=False)
#     service_charges=models.IntegerField(default=False)

