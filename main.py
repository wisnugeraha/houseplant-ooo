#!/usr/bin/env python3
"""The Cactus Cannot Be Bothered — make.fun entry (u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)"""
import os

ENTRY_LINE = "Out of office, photosynthesizing. Hold or don't; this fern has been holding since March and look where that got us."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
