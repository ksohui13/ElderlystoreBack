from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from accounts.models import User
from products.models import Product
from mainshop.models import TimeStampModel


#상품문의
class Quest(models.Model):
    qid = models.AutoField(primary_key=True, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qtitle = models.CharField(max_length=50)
    quest_text = models.TextField()
    qimage = models.ImageField(null=True, blank=True)
    qcreated_at = models.DateTimeField(auto_now_add=True)
    qupdated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.qtitle

#상품문의 댓글
class QComment(models.Model):
    quest_id = models.ForeignKey(Quest, related_name="qcomment", on_delete=models.CASCADE, db_column="qid")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.comment_text
    