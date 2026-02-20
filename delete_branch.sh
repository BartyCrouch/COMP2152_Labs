#!/bin/bash
BRANCH="lab_week06"
CURRENT=$(git branch --show-current)
if [ "$CURRENT" = "$BRANCH" ]; then
    echo "Currently on '$BRANCH', switching to master..."
    git checkout master || exit 1
fi
echo "Deleting '$BRANCH' locally..."
git branch -D "$BRANCH"
echo "Deleting '$BRANCH' remotely..."
git push origin --delete "$BRANCH"
echo "Done. Branch '$BRANCH' has been deleted locally and remotely."
