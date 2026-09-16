echo "Меню:"
echo "0 - Выход из меню"
echo "1 - Выполнить команду"
echo "2 - Действие из варианта" 

while true; do

read choice

if [ "$choice" = "1" ]; then 
echo "Запуск скрипта выполнения команд..."
sh "first_script.sh"
elif [ "$choice" = "2" ]; then 
echo "Запуск скрипта из варианта..."
sh "second_script.sh"
elif [ "$choice" = "0" ]; then
echo "Выход из меню..."
break

else
echo "Неправильный ввод"
fi

done