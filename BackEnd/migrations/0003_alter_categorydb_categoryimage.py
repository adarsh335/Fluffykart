# Generated by Django 4.1.7 on 2023-05-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0002_categorydb_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydb',
            name='CategoryImage',
            field=models.ImageField(blank=True, null=True, upload_to='CatCategory'),
        ),
    ]
