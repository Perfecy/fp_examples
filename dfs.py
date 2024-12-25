def dfs_collect(tree, node_func, children_key="children"):
    """
    Универсальная рекурсивная функция, которая:
    1) Применяет node_func к самому узлу (tree),
    2) Рекурсивно обходит все дочерние узлы (если они есть в tree[children_key]),
    3) Возвращает список результатов, собранных по всему дереву.
    
    :param tree: словарь, например: {"name": "root", "children": [ ... ]}
    :param node_func: функция от одного аргумента (словаря) -> результат
    :param children_key: ключ, в котором хранится список дочерних узлов
    """
    result = [node_func(tree)]
    children = tree.get(children_key, [])
    for child in children:
        result.extend(dfs_collect(child, node_func, children_key))
    return result

# Пример: у нас древовидная структура
my_tree = {
    "name": "root",
    "value": 1,
    "children": [
        {
            "name": "child1",
            "value": 2,
            "children": [
                {"name": "grandchild1", "value": 5},
                {"name": "grandchild2", "value": 6},
            ]
        },
        {
            "name": "child2",
            "value": 3
        }
    ]
}

# Соберём все "value"
all_values = dfs_collect(my_tree, node_func=lambda node: node.get("value"))
print(all_values)  # [1, 2, 5, 6, 3]

# Соберём все "имена" узлов
all_names = dfs_collect(my_tree, node_func=lambda node: node["name"])
print(all_names)  # ["root", "child1", "grandchild1", "grandchild2", "child2"]
