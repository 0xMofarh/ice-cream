# Generated by Django 4.2.5 on 2023-10-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_homepage_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/%y/%m/%d')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Work',
            },
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]
