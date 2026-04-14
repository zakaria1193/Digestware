"""Shared base model and enums for all digest output types."""

from enum import Enum

from pydantic import BaseModel


class ConsensusStatus(str, Enum):
    PROPOSED = "Proposed"
    UNDER_REVIEW = "Under Review"
    NEEDS_REVISION = "Needs Revision"
    NACKED = "NACK'd"
    READY_TO_LAND = "Ready to Land"
    COMMITTED = "Committed"


class BimodalBase(BaseModel):
    project: str
    subsystem: str
    patch_id: str | None = None  # git patch-id --stable for cross-referencing
