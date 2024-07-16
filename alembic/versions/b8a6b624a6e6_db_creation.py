"""DB creation

Revision ID: b8a6b624a6e6
Revises: 
Create Date: 2024-06-17 15:58:06.828341

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b8a6b624a6e6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "pictures",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("link", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("api_key", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "subscriptions",
        sa.Column("subscriber_id", sa.Integer(), nullable=False),
        sa.Column("subscribed_to_id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["subscribed_to_id"], ["users.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["subscriber_id"], ["users.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("subscriber_id", "subscribed_to_id"),
    )
    op.create_table(
        "tweets",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("content", sa.String(), nullable=True),
        sa.Column("tweet_media_ids", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("likes_count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "likes",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("tweet_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["tweet_id"], ["tweets.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("user_id", "tweet_id"),
        sa.UniqueConstraint("user_id", "tweet_id"),
    )
    op.create_table(
        "medias",
        sa.Column("tweet_id", sa.Integer(), nullable=False),
        sa.Column("picture_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["picture_id"], ["pictures.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["tweet_id"], ["tweets.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("tweet_id", "picture_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("medias")
    op.drop_table("likes")
    op.drop_table("tweets")
    op.drop_table("subscriptions")
    op.drop_table("users")
    op.drop_table("pictures")
    # ### end Alembic commands ###