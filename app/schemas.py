from pydantic import BaseModel, EmailStr


class ContactRequest(BaseModel):
    name: str
    phone: str
    email: EmailStr
    comment: str