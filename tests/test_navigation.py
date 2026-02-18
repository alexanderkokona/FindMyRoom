import pytest
import navigation  # <-- replace with your actual filename (without .py)


# ---------------------------------
# Test Data Setup (Mock Graph)
# ---------------------------------
@pytest.fixture(autouse=True)
def mock_graph():
    navigation.nodes = {
        "A": {"id": "A", "label": "Entrance"},
        "B": {"id": "B", "label": "Hallway 101"},
        "C": {"id": "C", "label": "Room 375"},
    }

    navigation.graph = {
        "A": [("B", 5, "Walk straight")],
        "B": [
            ("A", 5, "Walk back"),
            ("C", 10, "Turn right")
        ],
        "C": [("B", 10, "Turn left")]
    }


# ---------------------------------
# find_room_node Tests
# ---------------------------------

def test_find_room_node_valid():
    result = navigation.find_room_node("375")
    assert result == "C"


def test_find_room_node_invalid():
    result = navigation.find_room_node("999")
    assert result is None


def test_find_room_node_with_string_and_int():
    assert navigation.find_room_node(375) == "C"


# ---------------------------------
# shortest_path Tests
# ---------------------------------

def test_shortest_path_valid():
    dist, path = navigation.shortest_path("A", "C")

    assert dist == 15
    assert path == [
        ("B", "Walk straight"),
        ("C", "Turn right")
    ]


def test_shortest_path_no_path():
    navigation.graph = {
        "A": [],
        "C": []
    }

    dist, path = navigation.shortest_path("A", "C")

    assert dist is None
    assert path is None


# ---------------------------------
# navigate Tests
# ---------------------------------

def test_navigate_invalid_start():
    with pytest.raises(ValueError):
        navigation.navigate("Z", "375")


def test_navigate_invalid_room():
    with pytest.raises(ValueError):
        navigation.navigate("A", "999")
