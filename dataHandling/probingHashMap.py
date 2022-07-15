class ProbingHashMap:
    def __init__(self, array_size: int, collision_step: int = 1):
        self.array_size = array_size
        self.array = [None for _ in range(array_size)]
        self.collision_step = collision_step

    def get_size(self) -> int:
        return self.array_size

    def get_step(self) -> int:
        return self.collision_step

    def get_index(self, key: str, count_collisions: int = 0) -> int:
        hash = self.hash(key, count_collisions)
        return self.compress(hash)

    def hash(self, key: str, count_collisions: int = 0) -> int:
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compress(self, hash_code: int) -> int:
        return hash_code % self.get_size()

    def assign(self, key: str, value, assign_collisions: int = 0) -> None:
        array_index = self.get_index(key, assign_collisions)
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        assign_collisions += self.get_step()
        if assign_collisions >= self.get_size():
            return
        else:
            self.assign(key, value, assign_collisions)

    def retrieve(self, key: str, retrieval_collisions: int = 0):
        array_index = self.get_index(key, retrieval_collisions)
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions += self.get_step()
        if retrieval_collisions >= self.get_size():
            return
        else:
            self.retrieve(key, retrieval_collisions)

    def delete(self, key, deletion_collisions: int = 0):
        array_index = self.get_index(key, deletion_collisions)
        possible_delete_value = self.array[array_index]

        if possible_delete_value is None:
            return

        if possible_delete_value[0] == key:
            self.array[array_index] = None
            return
        
        deletion_collisions += self.get_step()
        if deletion_collisions >= self.get_size():
            return
        else:
            self.delete(key, deletion_collisions)