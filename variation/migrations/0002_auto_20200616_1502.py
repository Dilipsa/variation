# Generated by Django 3.0.5 on 2020-06-16 09:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('variation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('black', 'black'), ('green', 'green'), ('silky silver', 'silky silver'), ('Dilip Category', 'Dilip Category'), ('Latest added category', 'Latest added category'), ('again new category', 'again new category'), ('github category', 'github category')], max_length=96, null=True),
        ),
    ]
