# Generated by Django 4.2.2 on 2023-11-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projektMiSWDapp', '0002_datasets_knapsackdata_assignmentdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentdata',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='knapsackdata',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
