# Generated by Django 2.1.7 on 2019-04-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0004_auto_20190402_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed'))},
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=40, null=True),
        ),
    ]
