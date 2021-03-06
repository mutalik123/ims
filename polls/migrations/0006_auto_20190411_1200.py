# Generated by Django 2.1.7 on 2019-04-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_product_models_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature_varient',
            name='feature_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.FeatureMaster'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature_varient',
            name='variant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Variant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variant',
            name='idnumber',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Product_Models'),
            preserve_default=False,
        ),
    ]
