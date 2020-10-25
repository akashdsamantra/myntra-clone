# Generated by Django 3.1.2 on 2020-10-25 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=256)),
                ('middle_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=1)),
                ('dob', models.DateField()),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('mobile-verification', 'Mobile Verification'), ('email-verification', 'Email Verification'), ('mobile-login', 'Mobile Login'), ('forgot-password', 'Forgot Password')], max_length=50)),
                ('created', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.user')),
            ],
        ),
    ]
