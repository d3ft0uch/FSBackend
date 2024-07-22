from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.auth import current_active_user
from api.database import get_session
from api.public.user.models import User
from api.public.reviews.models import ReviewRead, ReviewCreateOrUpdate
from api.public.reviews.crud import read_reviews_gave, read_reviews_got, delete_review, update_or_create_review

router = APIRouter()


@router.get("/gave", response_model=list[ReviewRead])
def get_reviews(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        db: Session = Depends(get_session),
        user: User = Depends(current_active_user)
):
    return read_reviews_gave(offset=offset, limit=limit, user=user, db=db)


@router.get("/got", response_model=list[ReviewRead])
def get_reviews(
        offset: int = 0,
        limit: int = Query(default=100, lte=100),
        db: Session = Depends(get_session),
        user: User = Depends(current_active_user)
):
    return read_reviews_got(offset=offset, limit=limit, user=user, db=db)


@router.post("", response_model=ReviewRead)
def create_or_update_review(review: ReviewCreateOrUpdate, user: User = Depends(current_active_user), db: Session = Depends(get_session)):
    return update_or_create_review(review=review, user=user, db=db)


@router.delete("/{review_id}")
def delete_a_user(review_id: int, db: Session = Depends(get_session), user: User = Depends(current_active_user)):
    return delete_review(review_id=review_id, user=user, db=db)