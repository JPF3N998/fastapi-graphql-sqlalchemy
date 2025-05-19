from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.orm.models.caught_pokemon import CaughtPokemon
from app.orm.models._base import Base


class PKMNTrainer(Base):
    __tablename__ = "trainers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    caught_pokemon: Mapped[list["CaughtPokemon"]] = relationship(
        back_populates="trainer",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<PKMNTrainer id={self.id} name={self.name}>"
