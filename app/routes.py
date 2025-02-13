from fastapi import APIRouter, HTTPException
from app.models import Receipt
from app.services import calculate_points, cache
import uuid

router = APIRouter()

@router.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    cache[receipt_id] = points
    return {"id": receipt_id}

@router.get("/receipts/{receipt_id}/points")
def get_points(receipt_id: str):
    if receipt_id not in cache:
        raise HTTPException(status_code=404, detail="No receipt found for that ID")
    return {"points": cache[receipt_id]}