import sys
import json
def load_todos():
    try:
        with open("todo.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []
def save_todos(todos):
    with open("todo.json", "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)
def main():
    if len(sys.argv) < 2:
        print("用法：python todo.py add|list|done|del [参数]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        if len(sys.argv) < 3:
            print("add 需要跟任务名称，例：python todo.py add 刷题")
            return
        task_text = sys.argv[2]
        todos = load_todos()
        new_task = {"task": task_text, "done": False}
        todos.append(new_task)
        save_todos(todos)
        print(f"已添加：{task_text}")
    elif cmd == "list":
        todos = load_todos()
        if len(todos) == 0:
            print("暂无任务")
        else:
            for idx, item in enumerate(todos, start=1):
                mark = "[x]" if item["done"] else "[ ]"
                print(f"{idx}. {mark} {item['task']}")
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("done 需要跟任务序号，例：python todo.py done 2")
            return
        try:
            num = int(sys.argv[2])
        except ValueError:
            print("序号必须是数字")
            return
        index = num - 1
        todos = load_todos()
        if index < 0 or index >= len(todos):
            print(f"序号越界，当前共 {len(todos)} 条")
            return
        todos[index]["done"] = True
        task_name = todos[index]["task"]
        save_todos(todos)
        print(f"已完成：{task_name}")

    elif cmd == "del":
        # del 序号：删除任务
        if len(sys.argv) < 3:
            print("del 需要跟任务序号，例：python todo.py del 1")
            return
        try:
            num = int(sys.argv[2])
        except ValueError:
              print("序号必须是数字")
              return
        index = num - 1
        todos = load_todos()
        if index < 0 or index >= len(todos):
            print(f"序号越界，当前共 {len(todos)} 条")
            return
        task_name = todos[index]["task"]
        del todos[index]
        save_todos(todos)
        print(f"已删除：{task_name}")

    else:
        print("未知命令")


if __name__ == "__main__":
    main()
