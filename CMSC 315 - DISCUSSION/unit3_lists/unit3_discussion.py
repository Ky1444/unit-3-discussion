"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    - Python lists are dynamic arrays, so inserting at any position
      requires shifting existing elements to the right.
    - Inserting at the beginning is the most expensive because every
      element must move.
    - Inserting in the middle shifts roughly half the list.
    - Inserting at the end (index == len(lst)) behaves like append and
      does not shift any existing elements.
    """
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    - Index validation prevents crashes and ensures safe deletion.
    - If the index is valid, Python shifts all elements after the index
      left by one position to fill the gap.
    - If the index is invalid, return None to indicate no deletion occurred.
    """
    if 0 <= index < len(lst):
        return lst.pop(index)
    return None


def search_value(lst, value):
    """
    Search for a value within the list.

    - This is a linear search: Python checks each element sequentially
      from left to right.
    - Linear search is O(n) because the list must be scanned until the
      value is found or the end is reached.
    """
    for i, v in enumerate(lst):
        if v == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # DIGITAL SCENARIO:
    # A mobile app stores incoming notifications in a list.
    # New notifications appear at the end, urgent ones appear at the top,
    # and the user can delete or search notifications.

    print("\n=== INSERTION TESTS ===")

    # 1. Create a list containing several digital notifications.
    notifications = ["msg_newFollower", "msg_updateAvailable", "msg_friendOnline", "msg_dailyReward"]
    print("Original notifications:", notifications)

    # Insert at the beginning: urgent system alert.
    insert_at(notifications, 0, "SYSTEM_URGENT")
    print("After inserting urgent alert:", notifications)

    # Insert in the middle: medium-priority notification.
    insert_at(notifications, 2, "msg_securityCheck")
    print("After inserting mid-priority:", notifications)

    # Insert at the end: normal incoming notification.
    insert_at(notifications, len(notifications), "msg_backgroundSync")
    print("After inserting normal notification:", notifications)

    print("\n=== DELETION TESTS ===")

    # Delete from beginning: user dismissed urgent alert.
    removed = delete_at(notifications, 0)
    print("Removed (beginning):", removed)
    print("Notifications now:", notifications)

    # Delete from middle: user cleared a mid-list notification.
    mid_index = len(notifications) // 2
    removed = delete_at(notifications, mid_index)
    print(f"Removed (middle index {mid_index}):", removed)
    print("Notifications now:", notifications)

    # Delete from end: expired notification.
    removed = delete_at(notifications, len(notifications) - 1)
    print("Removed (end):", removed)
    print("Notifications now:", notifications)

    print("\n=== SEARCH TESTS ===")

    # Search for an existing notification.
    existing = "msg_friendOnline"
    idx = search_value(notifications, existing)
    print(f"Searching for {existing}: index =", idx)

    # Search for a missing notification.
    missing = "msg_nonexistent"
    idx = search_value(notifications, missing)
    print(f"Searching for {missing}: index =", idx)

    print("\n=== EDGE CASES ===")

    # Edge case 1: invalid deletion index.
    invalid = delete_at(notifications, 999)
    print("Attempt delete at invalid index 999:", invalid)

    # Edge case 2: insert into empty list.
    empty_queue = []
    print("Empty queue before insertion:", empty_queue)
    insert_at(empty_queue, 0, "BOOT_NOTIFICATION")
    print("Empty queue after insertion:", empty_queue)

    # Edge case 3: delete from empty list.
    removed = delete_at(empty_queue, 5)
    print("Attempt delete from empty list:", removed)


if __name__ == "__main__":
    main()
