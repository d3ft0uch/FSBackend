from fastapi import HTTPException, status
from sqlmodel import Session, select
from api.public.user.models import User
from api.public.reviews.models import Review, ReviewRead, ReviewCreateOrUpdate
from api.utils.generic_functions import set_model_from_another_model


def read_reviews_gave(offset: int = 0, limit: int = 20, user: User = None, db: Session = None):
    stmt = select(Review).where(Review.user_id_from == user.id).offset(offset).limit(limit)
    reviews = db.exec(stmt).all()
    return [ReviewRead.from_orm(r) for r in reviews]


def read_reviews_got(offset: int = 0, limit: int = 20, user: User = None, db: Session = None):
    stmt = select(Review).where(Review.user_id_to == user.id).offset(offset).limit(limit)
    reviews = db.exec(stmt).all()
    return [ReviewRead.from_orm(r) for r in reviews]


def update_or_create_review(review: ReviewCreateOrUpdate, user: User = None, db: Session = None):
    review_in_db = db.exec(select(Review).where(Review.user_id_from == user.id)).first() or Review()
    review_in_db = set_model_from_another_model(from_model=review, to_model=review_in_db)
    review_in_db.user_id_from = user.id
    # TODO move validation on model layer
    if review_in_db.user_id_from == review_in_db.user_id_to:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"You can't give a review to yourself",
        )
    db.add(review_in_db)
    db.commit()
    db.refresh(review_in_db)
    return ReviewRead.from_orm(review_in_db)


def delete_review(review_id: int, user: User = None, db: Session = None):
    review = db.get(Review, review_id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review not found with id: {review_id}",
        )
    if not review.user_id_from == user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You don't have a permission to perform this operation",
        )
    db.delete(review)
    db.commit()
    return {"ok": True}
