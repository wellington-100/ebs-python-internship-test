from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Milestone 1, task 1
    enabled = models.BooleanField(default=False)


# Milestone 1, task 4
class Comments(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateField(db_index=True, auto_now_add=True)
