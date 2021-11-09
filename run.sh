#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate yt
python ./youtube_download_playlist.py
read