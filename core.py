import json


def new_game():
    return {'paused': False, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False, 'processed': set()}

def bug_25(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return None

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    return [row for row in state["audit"] if row[0] == "a"]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state, element=None):
    if element in state["processed"]:
        return False
    state["processed"].add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state, slot=None):
    occupied = set(range(state["used"]))
    if slot is None or slot in occupied:
        return False
    state["used"] += 1
    return True

def bug_28(state, weight=-1):
    if weight < 0:
        return False
    return True

def bug_30(state):
    for entry in state["log"]:
        if len(entry) > 1 and entry[1] == "failed":
            state["value"] = state["snapshot"]
            break
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
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
