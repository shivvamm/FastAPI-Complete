"""Create due date for todos column

Revision ID: 1d807f64daa1
Revises: 7bcd40d197d0
Create Date: 2024-08-22 15:10:45.900881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d807f64daa1'
down_revision: Union[str, None] = '7bcd40d197d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('todos',sa.Column('due_date',sa.String(),nullable=True))


def downgrade() -> None:
    op.drop_column('todos','due_date')
