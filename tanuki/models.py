"""Domain models."""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import IntEnum


class MangaStatus(IntEnum):
    """Publication status of a manga/manhwa."""

    UNKNOWN = 0
    ONGOING = 1
    COMPLETED = 2
    HIATUS = 3
    CANCELLED = 4


@dataclass
class Manga:
    """A manga/manhwa as returned by a source."""

    id: str
    title: str
    thumbnail_url: str | None = None
    description: str | None = None
    author: str | None = None
    artist: str | None = None
    status: MangaStatus = MangaStatus.UNKNOWN
    genres: list[str] = field(default_factory=list)
    anilist_id: int | None = None
    mal_id: int | None = None
    sources: dict[str, str] = field(default_factory=dict)


@dataclass
class Chapter:
    """A chapter belonging to a manga, as returned by a source."""

    id: str
    manga_id: str
    source_id: str
    number: float
    title: str | None = None
    date_upload: datetime = field(default_factory=lambda: datetime.now(UTC))
    scanlator: str | None = None


@dataclass
class Page:
    """A single image page within a chapter."""

    index: int
    image_url: str
