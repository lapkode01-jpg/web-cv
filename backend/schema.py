from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    username: str
    email: EmailStr
    text: str

