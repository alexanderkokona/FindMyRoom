import json
import heapq
import re

# -----------------------------
# Load JSON graph
# -----------------------------
with open("nodes&edges.json", "r") as f:
    data = json.load(f)

nodes = {n["id"]: n for n in data["nodes"]}
edges = data["edges"]

# -----------------------------
# Build adjacency list
# -----------------------------
graph = {}

for edge in edges:
    a = edge["from"]
    b = edge["to"]
    dist = edge["distance"]
    instr = edge["instruction"]

    graph.setdefault(a, []).append((b, dist, instr))
    graph.setdefault(b, []).append((a, dist, instr))  # bidirectional


# -----------------------------
# Find which node contains a room
# -----------------------------
def find_room_node(room_number):
    room_number = str(room_number)

    for node_id, node_data in nodes.items():
        label = node_data.get("label", "")

        # Extract numbers from label
        rooms = re.findall(r'\b\d+\w*\b', label)

        if room_number in rooms:
            return node_id

    return None


# -----------------------------
# Dijkstra shortest path
# -----------------------------
def shortest_path(start, goal):
    pq = [(0, start, [])]  # (distance, current_node, path)
    visited = set()

    while pq:
        dist, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return dist, path

        for neighbor, ndist, instr in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (dist + ndist, neighbor, path + [(neighbor, instr)])
                )

    return None, None


# -----------------------------
# Navigation Function
# -----------------------------
def navigate(start_node, room_number):

    if start_node not in nodes:
        raise ValueError(f"Start node '{start_node}' does not exist.")

    goal_node = find_room_node(room_number)

    if not goal_node:
        raise ValueError(f"Room {room_number} not found in map.")

    total_distance, steps = shortest_path(start_node, goal_node)

    if steps is None:
        print("No path found.")
        return

    print(f"\nNavigation from {nodes[start_node]['label']} to Room {room_number}")
    print(f"Total distance: {total_distance} units\n")

    current = start_node
    for node, instruction in steps:
        if instruction:
            print(f"- {instruction}")
        current = node

    print(f"\nYou have arrived at Room {room_number}.")

call(test_navigation.py)
# -----------------------------
# Example Call
# -----------------------------
# navigate("ENT_WEST", "375")
