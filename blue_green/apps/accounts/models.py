from django.db import models
from django.contrib.postgres.fields import CIEmailField


class PersonMixin(models.Model):
    first_name = models.CharField("nome", max_length=150, blank=True)
    last_name = models.CharField("sobrenome", max_length=150, blank=True)
    birthdate = models.DateField("data de nascimento", null=True, blank=True)
    picture = models.ImageField("foto", null=True, blank=True)
    

    class Meta:
        abstract = True

    def __str__(self):
        return self.get_short_name()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


class User(PersonMixin):
    email = CIEmailField("email", unique=True)
    is_staff = models.BooleanField("status de admin", default=False)

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
        db_table = "users"
    
    
