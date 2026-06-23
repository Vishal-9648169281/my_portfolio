from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, default="Vishal")
    title = models.CharField(max_length=200, default="Full Stack Developer")
    bio = models.TextField(default="Passionate developer building innovative solutions.")
    email = models.EmailField(default="vishal@example.com")
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, default="India")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True)
    years_experience = models.IntegerField(default=2)
    projects_completed = models.IntegerField(default=20)
    happy_clients = models.IntegerField(default=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ]
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='frontend')
    icon = models.CharField(max_length=100, blank=True, help_text="Font Awesome class e.g. fab fa-python")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma separated technologies")
    image = models.ImageField(upload_to='projects/', blank=True)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.degree


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
