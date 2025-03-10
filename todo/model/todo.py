# TODO: Add code here
from operator import truediv


class Todo:

    def __init__(self,code_id: int, title: str, description: str ):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self)-> str:
        return f"{self.code_id} - {self.title}"


class  TodoBook:

    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self,title: str, description: str) -> int:
        nue_id = len(self.todos) + 1
        todo  = Todo(nue_id, title, description)
        self.todos[nue_id] = todo
        return nue_id

    def pending_todos(self)-> list[Todo]:
        return [todo  for todo in self.todos.values() if todo.completed == False]

    def completed_todos(self)-> list[Todo]:
        return [ todo for todo in self.todos.values() if todo.completed == True ]

    def tags_todo_count(self) -> dict[str, int]:





