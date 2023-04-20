import os
from fastapi import FastAPI
from utils import create_message, save_message, search_tree, rebuild_tree, maintain_tree

app = FastAPI()
root_folder = os.getcwd()
max_cluster_size = 5
#root_folder = 'C:/raven_private/REMO/'
# REMO = Rolling Episodic Memory Organizer

@app.post("/add_message")
async def add_message(message: str, speaker: str, timestamp: float) -> dict:
    # Add message to REMO
    new_message = create_message(message, speaker, timestamp)
    print(f"\n\nADD MESSAGE - {new_message}")
    save_message(root_folder, new_message)

    return {"detail": "Message added"}

@app.get("/search")
async def search(query: str) -> dict:
    # Search the tree for relevant nodes
    print(f"\n\nSEARCH - {query}")
    taxonomy = search_tree(root_folder, query)

    return {"results": taxonomy}

@app.post("/rebuild_tree")
async def rebuild_tree_endpoint() -> dict:
     # Trigger full tree rebuilding event
    print("\n\nREBUILD TREE")
    rebuild_tree(root_folder, max_cluster_size)

    return {"detail": "Tree rebuilding completed"}

@app.post("/maintain_tree")
async def maintain_tree_endpoint() -> dict:
     # Trigger tree maintenance event
    print("\n\nMAINTAIN TREE")
    maintain_tree(root_folder)

    return {"detail": "Tree maintenance completed"}