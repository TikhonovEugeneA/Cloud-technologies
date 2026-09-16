while true; do
echo "0 - Выйти в меню"
echo "1 - Проверить размеры файлов"

read choice

if [ "$choice" = "1" ]; then

    echo "Название первого файла:"
    read file1

    echo "Название второго файла:"
    read file2
    
    if [ "$file1" = "$file2" ]; then
        echo "Указан один и тот же файл!"
        echo ""
        continue
    fi

    if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
        echo "Файлы не найдены или не являются обычными файлами!"
        echo ""
        continue  
    fi

    NX=$(grep -c '^' "$file1")
    NY=$(grep -c '^' "$file2")

    if [ $NX -eq 0 ] || [ $NY -eq 0 ]; then
        echo "Один из файлов пустой!"
        echo ""
        continue
    fi

    echo "Изначальное кол-во строк в:"
    echo "Первый файл: $NX"
    echo "Второй файл: $NY"
    echo ""

    if [ $NX -eq $NY ]; then
        echo "В файлах одинаковое кол-во строк"
        echo ""
    elif [ $NX -gt $NY ]; then
        echo "В первом файле больше строк"
        sed -i "1,${NY}!d" "$file1"
        echo ""
    else
        echo "Во втором файле больше строк"
        sed -i "1,${NX}!d" "$file2"
        echo ""
    fi

    echo "Итог:"
    echo "$(grep -c '^' "$file1")"
    echo "$(grep -c '^' "$file2")"
    echo ""

elif [ "$choice" = "0" ]; then
echo "Выход из скрипта..."
echo ""
sh menu.sh
break

else
echo "Такой опции нет!"
echo ""
continue
fi

done