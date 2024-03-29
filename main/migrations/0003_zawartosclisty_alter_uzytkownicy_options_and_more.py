# Generated by Django 4.2.6 on 2023-11-27 18:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0002_prezent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZawartoscListy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwaPrezentu', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='uzytkownicy',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='uzytkownicy',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RenameField(
            model_name='listy',
            old_name='dataStworzenia',
            new_name='dataUtworzenia',
        ),
        migrations.RenameField(
            model_name='prezent',
            old_name='nazwa',
            new_name='nazwaPrezentu',
        ),
        migrations.RemoveField(
            model_name='uzytkownicy',
            name='haslo',
        ),
        migrations.RemoveField(
            model_name='uzytkownicy',
            name='login',
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='user', to='auth.group'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='plec',
            field=models.CharField(choices=[('M', 'Mężczyzna'), ('K', 'Kobieta')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_set', related_query_name='user', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='username',
            field=models.CharField(default=0, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uzytkownicy',
            name='zdjProfilu',
            field=models.ImageField(default=0, upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DaneUzytkownicy',
        ),
        migrations.AddField(
            model_name='zawartosclisty',
            name='idListy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.listy'),
        ),
        migrations.AddField(
            model_name='listy',
            name='zawartosc',
            field=models.ManyToManyField(blank=True, related_name='zawartoscListy', to='main.zawartosclisty'),
        ),
    ]
