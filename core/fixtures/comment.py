import pytest

from core.comment.models import Comment

from .user import user
from .post import post

@pytest.fixture
def comment(db, user, post):
    return Comment.objects.create(
        author=user, 
        post=post, 
        body="Test Comment Body"
    )