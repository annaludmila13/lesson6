# Создаем переменную immutable_var и присваиваем ей кортеж
immutable_var = (1, 2, 'a', 'b', 3.55)
print( immutable_var)
print("Кортежи (tuple) являются неизменяемыми (immutable) структурами данных в Python. Это означает, что после их создания я не могу изменять их элементы.")

mutable_list = [1, 2, 'a', 'b']
# Изменяем элементы списка
mutable_list[0] = 10  # Изменяем первый элемент
mutable_list.append('Modified')  # Добавляем новый элемент в список

# Выводим измененный список на экран
print("Mutable list:", mutable_list)
