
#!/usr/bin/env sh

set -e




git init
# git remote add origin https://github.com/pacelouis09/simpleApiAPP.git
git add -A
git commit -m 'deploy'

git push origin master
