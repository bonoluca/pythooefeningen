#!/bin/bash

# Ga naar de map van je Git-repository
cd /home/rpi/weatherheat-python/ICT-projecten || exit

# Haal eventuele wijzigingen van GitHub op
git pull origin main --no-rebase

# Voeg nieuwe of gewijzigde bestanden toe
git add .

# Maak een commit met automatische datum/tijd
git commit -m "Auto update $(date '+%Y-%m-%d %H:%M:%S')"

# Push naar GitHub
git push origin main