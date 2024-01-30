"""add content column to posts table

Revision ID: a42bf0f237b6
Revises: 532658cb81fa
Create Date: 2024-01-29 14:31:31.777830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a42bf0f237b6'
down_revision: Union[str, None] = '532658cb81fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
