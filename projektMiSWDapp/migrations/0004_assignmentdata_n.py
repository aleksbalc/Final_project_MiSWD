# Generated by Django 4.2.2 on 2023-11-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projektMiSWDapp', '0003_alter_assignmentdata_name_alter_knapsackdata_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentdata',
            name='n',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
