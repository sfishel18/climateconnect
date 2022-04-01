# Generated by Django 2.2.24 on 2022-04-01 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0093_auto_20220101_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membershiprequests',
            options={'verbose_name': 'Member Requests'},
        ),
        migrations.AlterField(
            model_name='membershiprequests',
            name='user',
            field=models.ForeignKey(help_text='Points to the user who sent the request', on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Requesting user'),
        ),
    ]
