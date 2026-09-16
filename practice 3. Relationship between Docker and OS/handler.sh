read -r first_line

mode="on"

if echo "$first_line" | grep -q "mode=off"; then
    mode="off"
elif echo "$first_line" | grep -q "mode=on"; then
    mode="on"
fi

file_info=""
for file in *; do
    [ -f "$file" ] || continue

    if [ "$mode" = "off" ]; then
        file_info="${file_info}  $file\n"
    elif [ "$mode" = "on" ]; then
        lines=$(grep -c '^' "$file")
        chars=$(wc -m < "$file")
        file_info="${file_info}  $file - $lines - $chars\n"
    fi
done

if [ -z "$file_info" ]; then
    file_info="Нет файлов в директории\n"
fi

echo -e "HTTP/1.1 200 OK\n\n${file_info}"