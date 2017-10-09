#!/bin/bash
echo "[*]Removing Readme[*]"
rm README.md
echo "[*]Generating New Readme[*]"
python list.py >> README.md
echo "[*]Git Add All[*]"
git add -A
echo "[*]Git Commit[*]"
git commit -m "Auto update"
echo "[*]Git Push[*]"
git push
