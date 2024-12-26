"""Added Analysis table with trigger

Revision ID: a2ddbd64c809
Revises: 
Create Date: 2024-12-24 16:19:12.539109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY, TEXT

# revision identifiers, used by Alembic.
revision = 'a2ddbd64c809'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Tabloyu oluştur
    op.create_table(
        'analysis',
        sa.Column('row_id', sa.Integer(), autoincrement=True, primary_key=True),
        sa.Column('task_key', sa.String(), nullable=False),
        sa.Column('epic_name', sa.String(), nullable=True),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('contained_task_keys', ARRAY(TEXT()), server_default='{}', nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.Column('is_updated', sa.Boolean(), server_default=sa.text('false')),
        sa.UniqueConstraint('task_key', name='analysis_task_key_unique'),
        sa.CheckConstraint("task_key IS NOT NULL AND trim(task_key) != ''", name='analysis_task_key_not_empty'),
    )

    # Trigger fonksiyonunu oluştur
    op.execute("""
    CREATE OR REPLACE FUNCTION update_updated_at_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated_at = CURRENT_TIMESTAMP;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Trigger'ı ekle
    op.execute("""
    CREATE TRIGGER update_timestamp
    BEFORE UPDATE
    ON analysis
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
    """)


def downgrade():
    # Trigger'ı ve fonksiyonu kaldır
    op.execute("DROP TRIGGER IF EXISTS update_timestamp ON analysis")
    op.execute("DROP FUNCTION IF EXISTS update_updated_at_column")
    op.drop_table('analysis')
