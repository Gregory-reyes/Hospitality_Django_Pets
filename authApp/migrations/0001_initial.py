# Generated by Django 4.2 on 2023-05-02 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('perfil', models.CharField(max_length=40, verbose_name='Perfil')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=40, verbose_name='Apellidos')),
                ('telefono', models.CharField(max_length=35, verbose_name='Telefono')),
                ('genero', models.CharField(max_length=30, verbose_name='Genero')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Signos_vitales',
            fields=[
                ('id_signos_vitales', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=20, verbose_name='Oximetria')),
                ('frecuencia_respiratoria', models.CharField(max_length=20, verbose_name='Frecuencia_respiratoria')),
                ('frecuencia_cardiaca', models.CharField(max_length=20, verbose_name='Frecuencia_cardiaca')),
                ('temperatura', models.CharField(max_length=20, verbose_name='Temperatura')),
                ('glicemias', models.CharField(max_length=20, verbose_name='Glicemias')),
                ('presion_arterial', models.CharField(max_length=20, verbose_name='Presion_arterial')),
                ('fecha_hora', models.DateField()),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signos_vitales', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Personal_salud',
            fields=[
                ('id_personalsalud', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=30, verbose_name='Rol')),
                ('especialidad', models.CharField(max_length=40, verbose_name='Especialidad')),
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_de_salud', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_personalsalud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='authApp.personal_salud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('id_histClinica', models.AutoField(primary_key=True, serialize=False)),
                ('sugerencias_cuidado', models.CharField(max_length=250, verbose_name='Sugerencias_cuidado')),
                ('diagnostico', models.CharField(max_length=250, verbose_name='Diagnostico')),
                ('entorno', models.CharField(max_length=250, verbose_name='Entorno')),
                ('fecha_sugerencia', models.DateField()),
                ('descripcion', models.CharField(max_length=100, verbose_name='Diagnostico')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_clinica', to='authApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id_familiar', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=35, verbose_name='Parentesco')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo')),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to='authApp.paciente')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
