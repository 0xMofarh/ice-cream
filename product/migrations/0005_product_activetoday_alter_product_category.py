# Generated by Django 4.2.5 on 2023-10-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_delete_biscut_delete_cups'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='activetoday',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('بسكوت', 'بسكوت'), ('كوب', 'كوب'), ('مشروب', 'مشروب')], max_length=50, null=True),
        ),
    ]
