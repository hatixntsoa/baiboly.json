from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

import json
from pathlib import Path


class BaibolyAPI:
    def __init__(self) -> None:
        self.api = FastAPI()
        self.mount_assets()
        self.set_templates()
        self.set_paths()
        self.register_routes()


    def mount_assets(self) -> None:
        self.api.mount("/js", StaticFiles(directory="assets/js"), name="js")
        self.api.mount("/css", StaticFiles(directory="assets/css"), name="css")
        self.api.mount("/font", StaticFiles(directory="assets/font"), name="font")


    def set_paths(self) -> None:
        self.OLD_TESTAMENT_PATH = Path("data/testamenta_taloha")
        self.NEW_TESTAMENT_PATH = Path("data/testamenta_vaovao")
        self.FAVICON_PATH = Path("assets/images/favicon.ico")


    def set_templates(self):
        self.templates = Jinja2Templates(directory="templates")


    def get_api(self) -> FastAPI:
        return self.api
    

    def register_routes(self) -> None:
        self.api.add_api_route("/", self.index, methods=["GET"])
        self.api.add_api_route("/favicon.ico", self.favicon, methods=["GET"], include_in_schema=False)
        self.api.add_api_route("/books/{category}", self.get_books, methods=["GET"])
        self.api.add_api_route("/chapters/{category}/{book}", self.get_chapters, methods=["GET"])
        self.api.add_api_route("/verses/{category}/{book}/{chapter}", self.get_verses, methods=["GET"])
        self.api.add_api_route("/render/{category}/{book}/{chapter}/{start}/{end}", self.render_verses, methods=["GET"])


    def load_json_files(self, directory: Path) -> list[str]:
        """Load all JSON filenames from a directory."""
        return [file.stem for file in directory.glob("*.json")]


    def load_json_content(self, filepath: Path):
        """Load the content of a JSON file."""
        with filepath.open(encoding="utf-8") as f:
            return json.load(f)


    async def index(self) -> _TemplateResponse:
        """Render the main page."""
        return self.templates.TemplateResponse("index.html", {"request": {}})


    async def favicon(self) -> FileResponse:
        return FileResponse(self.FAVICON_PATH)


    async def get_books(self, category: str) -> JSONResponse:
        """API to fetch all books for a category (old/new)."""
        directory = self.OLD_TESTAMENT_PATH if category == "old" else self.NEW_TESTAMENT_PATH
        if not directory.exists():
            raise HTTPException(status_code=404, detail="Category not found")

        books = []
        for book in self.load_json_files(directory):
            filepath = directory / f"{book}.json"
            content = self.load_json_content(filepath)
            meta = content.get("meta", {})
            book_name = meta.get("name", book)
            book_order = meta.get("order", 999)  # Default to 999 if no order specified

            # Append book data with meta information and standardized file name
            books.append({
                "name": book_name,
                "order": book_order,
                "file": book
            })

        # Sort books by the 'order' field
        books.sort(key=lambda x: x['order'])

        # Return the sorted list of books' names and their corresponding file names
        return JSONResponse(content=[{
            'display_name': book['name'],
            'file_name': book['file']
        } for book in books])


    async def get_chapters(self, category: str, book: str) -> JSONResponse:
        """API to fetch chapters for a given book."""
        directory = self.OLD_TESTAMENT_PATH if category == "old" else self.NEW_TESTAMENT_PATH
        filepath = directory / f"{book}.json"
        if not filepath.exists():
            raise HTTPException(status_code=404, detail="Book not found")
        content = self.load_json_content(filepath)
        chapters = [key for key in content.keys() if key != "meta"]
        return JSONResponse(content=chapters)


    async def get_verses(self, category: str, book: str, chapter: int) -> JSONResponse:
        """API to fetch verses for a given chapter in a book."""
        directory = self.OLD_TESTAMENT_PATH if category == "old" else self.NEW_TESTAMENT_PATH
        filepath = directory / f"{book}.json"
        if not filepath.exists():
            raise HTTPException(status_code=404, detail="Book not found")
        content = self.load_json_content(filepath)
        chapter_key = str(chapter)
        if chapter_key not in content:
            raise HTTPException(status_code=404, detail="Chapter not found")
        verses = list(content[chapter_key].keys())
        return JSONResponse(content=verses)


    async def render_verses(self, category: str, book: str, chapter: int, start: int, end: int):
        """API to fetch and render verses for a given range."""
        directory = self.OLD_TESTAMENT_PATH if category == "old" else self.NEW_TESTAMENT_PATH
        filepath = directory / f"{book}.json"
        if not filepath.exists():
            raise HTTPException(status_code=404, detail="Book not found")
        content = self.load_json_content(filepath)
        chapter_data = content.get(str(chapter), {})
        verses = {k: v for k, v in chapter_data.items() if start <= int(k) <= end}
        return JSONResponse(content=verses)