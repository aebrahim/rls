"""initial updates

Revision ID: 479bd311af91
Revises:
Create Date: 2024-09-30 15:47:22.747484

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "479bd311af91"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_policy(  # type: ignore
        table_name="items",
        policy_name="items_permissive_all_policy_0",
        cmd="ALL",
        definition="PERMISSIVE",
        expr="owner_id > NULLIF(current_setting('rls.account_id', true),'')::INTEGER",
    )  # type: ignore
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_policy(tablename="items", policyname="items_permissive_all_policy_0")  # type: ignore
    # ### end Alembic commands ###
