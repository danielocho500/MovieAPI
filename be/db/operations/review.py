import logging
from db.db import get_database
from models.review import SchemaReview

def create_review(review: SchemaReview,  user_id: str) -> bool:
    db = get_database()
    try:
        db.reviews.insert_one({
            "movie_id": review.movie_id,
            "user_id": user_id, 
            "cigars": review.cigars,
            "description": review.description,
        })
        return True
    except Exception as e:
        logging.error(f'create genre: {e}')
        return False