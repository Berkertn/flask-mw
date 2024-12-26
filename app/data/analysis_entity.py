from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY
from app.extensions import db


class Analysis(db.Model):
    __tablename__ = 'analysis'

    row_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_key = db.Column(db.String, nullable=False, unique=True)
    epic_name = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=False)
    contained_task_keys = db.Column(ARRAY(db.Text), default=[])
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    is_updated = db.Column(db.Boolean, default=False)

    # Constraints
    __table_args__ = (
        db.UniqueConstraint('task_key', name='analysis_task_key_unique'),
        db.CheckConstraint("task_key IS NOT NULL AND task_key != ''", name='analysis_task_key_not_empty'),
    )
