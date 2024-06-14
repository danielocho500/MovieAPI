from fastapi import APIRouter, Request
from utils.has_authorization import has_authorization, response_authorization
from utils.response_message import response_message
from db.operations.movie import exist_movie_by_id, update_movie_cigars
from db.operations.review import create_review
from models.review import SchemaReview

review_route = APIRouter()

@review_route.post("")
def post_review(request: Request, review: SchemaReview):
    result, user_id = has_authorization(request)

    if result == response_authorization.invalid_token:
        return response_message(400, "Invalid Token")
    elif result == response_authorization.no_authorization:
        return response_message(400, "No authorization")
    if not exist_movie_by_id(review.movie_id):
        return response_message(404, "Not movie found")
    
    result = create_review(review, user_id)

    if result:
        update_movie_cigars(review.movie_id, review.cigars )
        return response_message(201, "Review created")
    else:
        return response_message(500, "server error")
    
