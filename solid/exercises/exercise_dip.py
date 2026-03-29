from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data: str) -> None:
        pass


class PostgreSQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"[PostgreSQL] Saving '{data}'...")


class MySQLDatabase(Database):
    def save(self, data: str) -> None:
        print(f"[MySQL] Saving '{data}'...")


class MockDatabase(Database):
    def __init__(self):
        self.saved_data = []

    def save(self, data: str) -> None:
        self.saved_data.append(data)


class Register:
    def __init__(self, db: Database):
        self.db = db

    def sign_up(self, user: str) -> None:
        self.db.save(user)


if __name__ == "__main__":
    reg = Register(db=PostgreSQLDatabase())
    reg.sign_up("Alice")