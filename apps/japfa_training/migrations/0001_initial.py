# Generated by Django 3.2.13 on 2023-02-17 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mt_division',
            fields=[
                ('id_division', models.AutoField(primary_key=True, serialize=False)),
                ('division_code', models.CharField(max_length=10)),
                ('division_name', models.CharField(max_length=50)),
                ('division_description', models.CharField(max_length=100)),
                ('division_status', models.CharField(max_length=1)),
                ('created_by', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=20, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'mt_division',
                'db_table': 'mt_division',
            },
        ),
        migrations.CreateModel(
            name='mt_employee',
            fields=[
                ('id_employee', models.AutoField(primary_key=True, serialize=False)),
                ('nik', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('url_photo', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(max_length=20, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('mt_division', models.ForeignKey(db_column='id_division', on_delete=django.db.models.deletion.CASCADE, related_name='mt_employee_mt_division', to='japfa_training.mt_division')),
            ],
            options={
                'verbose_name_plural': 'mt_employee',
                'db_table': 'mt_employee',
            },
        ),
    ]
