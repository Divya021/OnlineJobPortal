# Generated by Django 2.2.2 on 2020-06-07 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0003_recruiter_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=30, null=True)),
                ('experience', models.CharField(max_length=30, null=True)),
                ('location', models.CharField(max_length=30, null=True)),
                ('recruiter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobportal.Recruiter')),
            ],
        ),
    ]
