# Generated by Django 2.2.13 on 2021-02-15 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0061_remove_project_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='location',
            field=models.ForeignKey(blank=True, help_text="Points to the organization's location", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_loc', to='location.Location', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='project',
            name='loc',
            field=models.ForeignKey(blank=True, help_text="Points to the project's location", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_loc', to='location.Location', verbose_name='Location'),
        ),
    ]
