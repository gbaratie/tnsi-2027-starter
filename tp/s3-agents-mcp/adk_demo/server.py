"""Serveur MCP public local, exclusivement sur les données synthétiques."""
import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

server = FastMCP("music-discovery-readonly")


@server.tool()
def search_library(query: str) -> dict:
    """Recherche un titre ou une ambiance, avec dix résultats maximum."""
    if not isinstance(query, str) or not query.strip() or len(query) > 200:
        raise ValueError("query est une chaîne non vide de 200 caractères maximum.")
    data = json.loads(Path(os.environ["FILROUGE_MUSIC_LIBRARY"]).read_text())
    items = [track for track in data["tracks"] if query.lower() in
             (track["title"] + " " + " ".join(track.get("moods", []))).lower()][:10]
    return {"items":items, "count":len(items)}


if __name__ == "__main__":
    server.run(transport="stdio")
