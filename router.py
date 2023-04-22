from fastapi import Depends, HTTPException, status, APIRouter, Request
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime, timedelta
from jose import jwt, JWTError
from config import JWT_Settings
from functools import lru_cache
import exceptions as exceptions
from pydantic.validators import dict_validator
from pydantic import EmailStr
from utils.token import validate_token
from sqlalchemy import or_
from logging import info

hospital_router = APIRouter()