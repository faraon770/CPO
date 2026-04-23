# Граф — модель социальной сети (список смежности)

def create_graph():
    return {}

def add_user(graph, user):
    if user not in graph:
        graph[user] = []
        print(f"✅ Пользователь '{user}' добавлен.")
    else:
        print(f"⚠️  Пользователь '{user}' уже существует.")

def add_connection(graph, user1, user2):
    if user1 not in graph or user2 not in graph:
        print("❌ Один из пользователей не найден.")
        return
    if user2 not in graph[user1]:
        graph[user1].append(user2)
        graph[user2].append(user1)
        print(f"🔗 Связь добавлена: {user1} ↔ {user2}")
    else:
        print(f"⚠️  Связь между '{user1}' и '{user2}' уже существует.")

def print_graph(graph):
    print("\n📊 Структура социальной сети:")
    print("-" * 35)
    if not graph:
        print("  Граф пуст.")
    for user, friends in graph.items():
        friends_str = ", ".join(friends) if friends else "нет друзей"
        print(f"  {user:12} → [{friends_str}]")
    print("-" * 35)

def get_friends(graph, user):
    if user not in graph:
        print(f"❌ Пользователь '{user}' не найден.")
        return
    friends = graph[user]
    if friends:
        print(f"👥 Друзья пользователя '{user}': {', '.join(friends)}")
    else:
        print(f"😶 У пользователя '{user}' пока нет друзей.")

def count_stats(graph):
    users = len(graph)
    edges = sum(len(f) for f in graph.values()) // 2
    print(f"\n📈 Статистика сети:")
    print(f"   Пользователей : {users}")
    print(f"   Связей        : {edges}")

# ——— Основная программа ———

graph = create_graph()

# Добавляем пользователей
print("=== Добавление пользователей ===")
for name in ["Алия", "Бекзат", "Дана", "Ерлан", "Жанна"]:
    add_user(graph, name)

# Добавляем связи (рёбра)
print("\n=== Добавление связей ===")
add_connection(graph, "Алия",   "Бекзат")
add_connection(graph, "Алия",   "Дана")
add_connection(graph, "Бекзат", "Ерлан")
add_connection(graph, "Дана",   "Жанна")
add_connection(graph, "Ерлан",  "Жанна")
add_connection(graph, "Алия",   "Жанна")
add_connection(graph, "Алия",   "Бекзат")   # дубликат — будет предупреждение

# Выводим граф
print_graph(graph)

# Друзья конкретного пользователя
print()
get_friends(graph, "Алия")
get_friends(graph, "Ерлан")

# Статистика
count_stats(graph)