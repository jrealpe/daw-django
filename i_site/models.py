from django.db import models


class BasicInfo(models.Model):
    name = models.CharField(
            verbose_name = 'Nombre',
            max_length = 100,
            blank = False)
    description = models.TextField(
            verbose_name = 'Descripción',
            blank = True,
            null = True)
    date_created = models.DateField(
            verbose_name = 'Fecha de creación',
            auto_now_add = True)
    is_activated = models.BooleanField(
            verbose_name = 'Activado/Desactivado',
            default = True)

    class Meta:
        abstract = True

class Course(BasicInfo):
    syllabus = HTMLField()
    policies = HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Requirement(BasicInfo):

    TYPE = (
        (1,'Co-Requisito'),
        (2,'Pre-Requisito'),
    )

    course = models.ForeignKey(
            Course,
            verbose_name = 'Curso',
            blank = False)
    type = models.PositiveIntegerField(
            verbose_name = 'Tipo',
            choices = TYPE,
            blank = False)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'requirements'
        verbose_name = 'Requerimiento'
        verbose_name_plural = 'Requerimientos'


class W2W(models.Model):
    name = models.CharField(
            verbose_name = 'Nombre',
            max_length = 50,
            blank = False)
    content = models.FileField(
            upload = 'contents',
            verbose_name = 'Contentido',
            help_text = 'Contenido de la semana',
            blank = False)
    task = models.FileField(
            upload = 'tasks',
            verbose_name = 'Tarea',
            help_text = 'Tarea de la semana',
            blank = False)
    video = models.URLField(
            verbose_name = 'Video',
            help_text = 'Video de la clase subido en youtube',
            blank = False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        default_related_name = 'w2w'
        verbose_name = 'Semana a Semana'
        verbose_name_plural = 'Semana a Semana'


class Staff(BasicInfo):

    CHARGE = (
        (1,'Coordinador(a)'),
        (2,'Profesor(a)'),
        (3,'Ayudante'),
    )

    course = models.ForeignKey(
            Course,
            verbose_name = 'Curso',
            blank = False)
    phone = models.CharField(
            verbose_name = 'Teléfono',
            max_length = 15,
            blank = False)
    email = models.EmailField(
            verbose_name = 'Correo',
            blank = False)
    charge = models.PositiveIntegerField(
            verbose_name = 'Cargo',
            choices = CHARGE,
            blank = False)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'staff'
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'


class Schedule(model.Model):

    DAYS_OF_WEEK = (
        (0,'Lunes'),
        (1,'Martes'),
        (2,'Miércoles'),
        (3,'Jueves'),
        (4,'Viernes'),
        (5,'Sábado'),
        (6,'Domingo'),
    )

    staff = models.ForeignKey(
            Staff,
            verbose_name = 'Personal',
            blank = False)
    day = models.PositiveIntegerField(
            verbose_name = 'Día',
            choices = DAYS_OF_WEEK,
            blank = False)
    hour_start = TimeField(
            verbose_name = 'Hora de inicio',
            blank=False)
    hour_end = TimeField(
            verbose_name = 'Hora de final',
            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'schedules'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'


class News(BasicInfo):
    image = models.FileField(
            upload = 'news',
            verbose_name = 'Imágen',
            blank = True,
            null = True)
    link = models.URLField(
            verbose_name = 'Link',
            help_text = 'Link de la noticia completa',
            blank = True,
            null = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']
        default_related_name = 'news'
        verbose_name = 'Noticias'
        verbose_name_plural = 'Noticias'
