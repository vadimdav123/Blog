from django.db import models

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает представление модели."""
        return self.text

class Article(models.Model):
    """Статья"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'articles'

    def __str__(self):
        """Возвращает строковое представление модели"""
        return f"{self.text[:50]}..."

class User(models.Model):
    """Пользователь"""
    username = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Comment(models.Model):
    """Комментарий"""
    text = models.CharField(max_length=512)
    date_added = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    
    
