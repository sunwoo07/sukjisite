# board/models.py

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import resolve_url

# 게시글 model
class Post(models.Model):
    title = models.CharField(  # 제목 field
        verbose_name='제목',  # 표시되는 명칭
        max_length=50,  # 최대 40자
        blank=False,  # 이 값은 반드시 입력되어야 함을 설정
    )
    content = models.TextField(  # 내용 field
        verbose_name='내용',  # 표시되는 명칭
        max_length=9999,  # 최대 9999자
        blank=False,  # 이 값은 반드시 입력되어야 함을 설정
    )
    author = models.ForeignKey( # 작성자 정보
        # User, on_delete=models.CASCADE
        getattr(settings, 'AUTH_USER_MODEL'),  # object가 settings의 AUTH_USER_MODEL에 해당하는 model에 속하도록 설정
        on_delete=models.SET_NULL,  # 작성자 model 삭제되면 값을 null로 변경
        null=True,  # null data를 허용
        editable=False,  # 일반 사용자가 이 data를 건드릴 수 없도록 설정
    )
    created = models.DateTimeField(  # 작성시간 field
        auto_now_add=True  # 최초 등록시에만 저장
    )
    updated = models.DateTimeField(  # 수정시간 field
        auto_now=True  # 수정시 계속 변화 가능
    )
    hits = models.IntegerField(  # 조회수 field
        default=0,  # 기본값을 0으로 설정
        editable=False,  # 일반 사용자가 이 data를 건드릴 수 없도록 설정
    )
    good = models.IntegerField(  # 좋아요 field
        default=0,  # 기본값을 0으로 설정
    )
    bad = models.IntegerField(  # 싫어요 field
        default=0,  # 기본값을 0으로 설정
    )

    def hit(self):
        "조회수 1 추가"
        self.hits = models.F('hits') + 1
        return self.save(update_fields=['hits'])
    # 절대경로(url) 설정
    def get_absolute_url(self): return resolve_url('board:detail', self.pk)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글 모음'
        ordering = ['-created']  # 작성 시간별 내림차순 정렬

class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
