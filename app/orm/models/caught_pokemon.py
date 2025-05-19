from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer

from app.orm.models.trainer import PKMNTrainer
from app.orm.models._base import Base


class CaughtPokemon(Base):
    __tablename__ = "caught_pokemon"

    id: Mapped[int] = mapped_column(primary_key=True)
    trainer_id: Mapped[int] = mapped_column(Integer, nullable=False)
    pokemon_id: Mapped[int] = mapped_column(Integer, nullable=False)

    trainer: Mapped["PKMNTrainer"] = relationship(
        back_populates="caught_pokemon",
    )

    def __repr__(self):
        return f"<CaughtPokemon id={self.id} trainer_id={self.trainer_id} pokemon_id={self.pokemon_id}>"
