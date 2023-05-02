from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        #Crea y guarda un usuario con el nombre de usuario y la contraseña.        
        if not username:
            raise ValueError('El usuario debe tener un nombre')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
        #Para este modelo no es necesario la creación de SuperUsuario
    """
    def create_superuser(self, username, password):       
        user = self.create_user(
        username=username,
        password=password,
    )
        user.is_admin = True
        user.save(using=self._db)
        return user
    """    
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True) #tocaría cambiar la primary_key de username por 'Username'
    username = models.CharField('Username', max_length = 15, unique=True)    
    password = models.CharField('Password', max_length = 256)
    perfil = models.CharField('Perfil', max_length = 40)
    nombre = models.CharField('Nombre', max_length = 40)
    apellidos = models.CharField('Apellidos', max_length = 40)
    telefono = models.CharField('Telefono', max_length = 35)
    genero = models.CharField('Genero', max_length = 30)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'username'