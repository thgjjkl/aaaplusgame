from enemy.enemy import Enemy

enemy_types = {
    "EnemyType1": {
        "size":  50,
        "speed": 10,
        "spawn_x": 0,
        "spawn_y": 1000
    },
    "EnemyType2": {
        "size": 100,
        "speed": 3,
        "spawn_x": 0,
        "spawn_y": 750
    }
}

class EnemyType1(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        # Logic for updating EnemyType1
        pass


class EnemyType2(Enemy):
    def __init__(self, x, y, size, speed, target_x, target_y):
        super().__init__(x, y, size, speed, target_x, target_y)

    def update(self):
        # Logic for updating EnemyType2
        pass
