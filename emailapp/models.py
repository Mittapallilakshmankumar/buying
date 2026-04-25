from django.db import models

class EmailLog(models.Model):

    subject = models.CharField(max_length=200)
    message = models.TextField()
    total_emails = models.IntegerField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject