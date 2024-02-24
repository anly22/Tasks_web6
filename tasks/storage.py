from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    if type(index) is int and index in range(len(_DB)):
        _DB.pop(index)
    else:
        print("Incorrect index")
        
        
def mark_task_completed(index: int, completed: bool) -> None:
    if type(index) is int and index in range(len(_DB)):
        _DB[index]["completed"] = completed
    else:
        print("Incorrect index")


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [(i, task["title"], task["completed"]) for i, task in enumerate(_DB)]
