"""Abstract base class for all source plugins."""

from abc import ABC, abstractmethod

from tanuki.models import Chapter, Manga, Page


class TanukiSource(ABC):
    """
    Contract every source plugin must fulfill.

    Subclasses declare class-level metadata and capability flags.
    """

    id: str
    name: str
    lang: str
    version: str = "1.0.0"
    base_url: str

    @abstractmethod
    async def popular(self, page: int) -> ...:
        """Return a page of currently popular manga."""
        ...

    @abstractmethod
    async def latest(self, page: int) -> ...:
        """Return a page of recently updated manga."""
        ...

    @abstractmethod
    async def search(self, query: str, page: int, filters: ...) -> ...:
        """Search manga by query string and optional filters."""
        ...

    @abstractmethod
    async def manga_detail(self, manga_id: str) -> Manga:
        """Return full metadata for a single manga."""
        ...

    @abstractmethod
    async def chapter_list(self, manga_id: str) -> list[Chapter]:
        """Return all chapters for a manga, newest first."""
        ...

    @abstractmethod
    async def page_list(self, chapter_id: str) -> list[Page]:
        """Return all image pages for a chapter."""
        ...

    @abstractmethod
    async def ping(self) -> bool:
        """Lightweight health check. Override if the site has a better endpoint."""
        ...
