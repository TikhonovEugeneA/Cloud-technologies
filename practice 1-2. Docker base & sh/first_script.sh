while true; do
echo "Введите команду:"
read command

if [ "$command" = "exit" ]; then
echo "Возврат в меню..."
sh menu.sh
break
fi
    
if [ -z "$command" ]; then
continue
fi

eval "$command"
echo ""
done