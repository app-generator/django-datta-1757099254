# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Usuario(models.Model):

    #__Usuario_FIELDS__
    telefono = models.CharField(max_length=255, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=255, null=True, blank=True)

    #__Usuario_FIELDS__END

    class Meta:
        verbose_name        = _("Usuario")
        verbose_name_plural = _("Usuario")


class Estudiante(models.Model):

    #__Estudiante_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=255, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)

    #__Estudiante_FIELDS__END

    class Meta:
        verbose_name        = _("Estudiante")
        verbose_name_plural = _("Estudiante")


class Institucionreceptora(models.Model):

    #__Institucionreceptora_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    link_google_maps = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    aprobada = models.BooleanField()
    reglamento_interno = models.CharField(max_length=255, null=True, blank=True)
    personal = models.TextField(max_length=255, null=True, blank=True)
    actividades = models.TextField(max_length=255, null=True, blank=True)

    #__Institucionreceptora_FIELDS__END

    class Meta:
        verbose_name        = _("Institucionreceptora")
        verbose_name_plural = _("Institucionreceptora")


class Asesorexterno(models.Model):

    #__Asesorexterno_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    #__Asesorexterno_FIELDS__END

    class Meta:
        verbose_name        = _("Asesorexterno")
        verbose_name_plural = _("Asesorexterno")


class Asesorinterno(models.Model):

    #__Asesorinterno_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    #__Asesorinterno_FIELDS__END

    class Meta:
        verbose_name        = _("Asesorinterno")
        verbose_name_plural = _("Asesorinterno")


class Responsablepe(models.Model):

    #__Responsablepe_FIELDS__
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    #__Responsablepe_FIELDS__END

    class Meta:
        verbose_name        = _("Responsablepe")
        verbose_name_plural = _("Responsablepe")


class Documento(models.Model):

    #__Documento_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    archivo = models.CharField(max_length=255, null=True, blank=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Documento_FIELDS__END

    class Meta:
        verbose_name        = _("Documento")
        verbose_name_plural = _("Documento")


class Galeria(models.Model):

    #__Galeria_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    fecha_subida = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Galeria_FIELDS__END

    class Meta:
        verbose_name        = _("Galeria")
        verbose_name_plural = _("Galeria")


class Foro(models.Model):

    #__Foro_FIELDS__
    titulo = models.CharField(max_length=255, null=True, blank=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Foro_FIELDS__END

    class Meta:
        verbose_name        = _("Foro")
        verbose_name_plural = _("Foro")


class Comentarioforo(models.Model):

    #__Comentarioforo_FIELDS__
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField(max_length=255, null=True, blank=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Comentarioforo_FIELDS__END

    class Meta:
        verbose_name        = _("Comentarioforo")
        verbose_name_plural = _("Comentarioforo")



#__MODELS__END
