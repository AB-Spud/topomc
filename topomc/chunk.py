# core
import math
import os, sys
import logging
# dependencies
import anvil

# files
from topomc.common import yaml_open


def chunkpos_to_regionpos(chunk):
    return int(math.floor(chunk / 32))


def load(world, chunkx, chunkz):
    (regionx, regionz) = tuple([
        chunkpos_to_regionpos(chunk_coord) for chunk_coord in (chunkx, chunkz)
    ])

    saves_path = yaml_open.get("saves path")
    saves_path = os.path.normcase(saves_path)
    if saves_path.startswith("~"):
        saves_path = os.path.expanduser(saves_path)
    saves_path = os.path.expandvars(saves_path)
    if not os.path.isdir(saves_path):
        logging.critical(f"App: Could not read path: {saves_path}")
        sys.exit()
    
    world_path = os.path.join(saves_path, world)

    # test to see whether world exists
    if not os.path.isdir(world_path):
        logging.critical("Chunk: Specified world save does not exist!")
        logging.info("Chunk: Available worlds:")
        for world in os.listdir(saves_path):
            if not world[2:-2].endswith("UNDO"):
                logging.info(f"Chunk: {world}")
        sys.exit()


    anvil_file = os.path.join(world_path, "region", f"r.{regionx}.{regionz}.mca")

    # open chunk
    try:
        region = anvil.Region.from_file(anvil_file)
    except Exception:
        logging.critical(f"Chunk: Region {regionx, regionz} for chunk {chunkx, chunkz} is not loaded and does not have an save file")
        sys.exit()

    try:
        chunk = anvil.Chunk.from_region(region, chunkx, chunkz)
    except Exception:
        logging.critical(f"Chunk: Chunk {chunkx, chunkz} is not loaded or corrupt")
        sys.exit()

    return chunk
