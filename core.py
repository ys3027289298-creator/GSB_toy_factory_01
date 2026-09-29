"""玩具厂核心逻辑：原料、产线、检测和出货。"""

import json


def new_game():
    return {"orders": {}, "line_load": 0, "line_capacity": 2, "material": 100, "yield_rate": 100, "day": 1, "order_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["order_id"] += 1
    return state


def feed(state, order_id, amount):
    state["orders"][order_id] = amount
    state["material"] -= amount
    return True


def produce_line(state, order_id):
    state["line_load"] += 1
    return True


def fee(state, order_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, order_id):
    return True


def produce(state, amount):
    return True


def defect(state):
    state["yield_rate"] -= 5
    state["yield_rate"] -= 5
    return state["yield_rate"]


def ship(state, order_id):
    return True


def main():
    print("玩具厂 - 命令: feed/line/fee/cancel/produce/defect/ship/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
