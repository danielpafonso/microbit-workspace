"""Upload python to to Micro:bit"""

import argparse
import os

from datetime import datetime

import microfs
import python_minifier as minifier


MAIN = ""
ADDONS = []
TMP = f"tmp_{datetime.now().strftime('%Y%m%d%H%M%S')}"

def create_tmp() -> None:
    """Create temporary folder"""
    os.makedirs(TMP)

def remove_tmp() -> None:
    """Delete temporary files and folder"""
    # delete files
    os.remove(os.path.join(TMP, MAIN))
    for filename in ADDONS:
        os.remove(os.path.join(TMP, filename))
    # delete folder
    os.removedirs(TMP)

def minify_to_tmp(filename: str) -> str:
    """Read file, minify its and write file in tmp folder with same name.
    Return writen file path
    """
    # read
    with open(filename, "r", encoding="utf8") as ifp:
        fdata = ifp.read()
    # minify
    minified = minifier.minify(
        fdata,
        rename_globals=True,
        remove_literal_statements=True,
    )
    # write
    minified_path = os.path.join(TMP, filename)
    with open(minified_path, "r", encoding="utf8") as ofp:
        ofp.write(minified)

    return minified_path

def clear_microbit() -> None:
    """Clear files from micro:bit file system"""
    print("Cleaning micro:bit file system")
    files = microfs.ls()
    for fname in files:
        microfs.rm(fname)

def flash() -> None:
    """Flash files to micro:bit, setting MAIN as startup script"""
    # create tmp folder
    create_tmp()
    # Copy additional scripts
    if len(ADDONS) > 0:
        print("Copying additional scripts")
        for name in ADDONS:
            print(" ", name)
            mini_path = minify_to_tmp(name)
            microfs.put(mini_path)

    print("Copying main script: ", MAIN)
    # Rename script to main.py setting it as startup script
    mini_path = minify_to_tmp(MAIN)
    microfs.put(mini_path, "main.py")

    # remove tmp folder
    remove_tmp()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Flash main and additional python scripts to micro:bit")
    parser.add_argument("-c", "--clear", action="store_true",
        help="Remove files from microbot before flashing")
    ARGS = parser.parse_args()

    if ARGS.clear:
        clear_microbit()
    flash()
