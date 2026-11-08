
set -e
LOGIN="$1"
[ -z "$LOGIN" ] && { echo "Укажите логин: bash publish.sh ваш_логин"; exit 1; }
cd "$(dirname "$0")/clinic-project"
git config user.name  >/dev/null || { echo "Задайте имя:   git config --global user.name \"Фамилия Имя\""; exit 1; }
git config user.email >/dev/null || { echo "Задайте почту:  git config --global user.email \"you@example.com\""; exit 1; }
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$LOGIN/clinic-project.git"
git push -u origin main
git push origin --tags
echo "Готово: https://github.com/$LOGIN/clinic-project"
