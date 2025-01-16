from django.db import models
from accounts.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    topics = (
        ('a', 'مشکل یا بیماری گیاهان'),
        ('b', 'نحوه نگهداری'),
        ('c', 'مواد مغذی گیاهان'),
        ('d', 'ظاهر گیاهان'),
        ('e', 'اطلاعات عمومی درباره گیاهان'),
        ('f', 'روش های تکثیر گیاهان'),
        ('g', 'زادگاه گیاهان'),
        ('h', 'خاک گیاه'),
        ('i', 'آب گیاه'),
        ('j', 'نور گیاه'),
        ('k', 'دما و رطوبت گیاه'),
        ('l', 'هرس کردن گیاه'),
        ('m', 'محصولات گیاه'),
        ('n', 'نام کاشف'),
        ('o', 'محل اکتشاف'),
        ('p', 'نام علمی گیاهان'),
        ('q', 'نام فارسی گیاهان'),

    )

    topic = models.CharField(max_length=100, choices=topics, blank=True, null=True)

    title = models.CharField(max_length=100)
    detail = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    detail = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer by {self.user.username} to: {self.question.title}"


