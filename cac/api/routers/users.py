from typing import Sequence, Tuple, Optional, List
from uuid import UUID
from datetime import date

from fastapi import APIRouter, HTTPException, Path, Query, Body, Depends, Security, status
from cac.api.dependencies import user_logic_dependancy, authorize_user

