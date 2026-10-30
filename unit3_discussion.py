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
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary
      depending on where the insertion occurs.
    """

    # insert() adds the new value at the selected index.
    # Elements after that position move one spot to the right.
    # Inserting near the beginning takes more work because
    # more elements need to move compared to inserting at the end.
    # Inserting at the beginning or middle can take O(n) time.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion
      are important.
    """

    # Check the index before removing anything.
    # This prevents an IndexError if the list is empty
    # or someone tries to remove an index that does not exist.
    if index < 0 or index >= len(lst):
        return None

    # pop() removes the item and returns its value.
    # Items after the removed position shift left to fill the gap.
    # Removing from the beginning or middle can take O(n) time.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search
      and why it scans sequentially.
    """

    # Check each element starting from the beginning.
    # This is a linear search because we go through the list
    # one item at a time until we find the value.
    # We cannot assume the list is sorted.
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    # Return -1 if we checked everything and did not find it.
    # The worst-case runtime is O(n) because we may
    # need to check every item.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # =============================
    # TODO (Student): INSERTION TESTS
    # =============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step.

    print("\n=== INSERTION TESTS ===")

    # Start with a simple list so the changes are easy to see.
    numbers = [10, 20, 30, 40]
    print("Original list:", numbers)

    # Insert 5 at the beginning.
    # All existing elements move right to make room.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at beginning:", numbers)

    # Insert 25 in the middle.
    # Only the values at or after this index need to move.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in middle:", numbers)

    # Insert 50 at the end.
    # No existing elements need to shift.
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at end:", numbers)

    # Insertion near the front can be slower than at the end
    # because Python needs to move more elements.

    # =============================
    # TODO (Student): DELETION TESTS
    # =============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments explaining the output.

    print("\n=== DELETION TESTS ===")

    # Remove the first item.
    # The remaining elements shift left one position.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Remove the item with value 25 from the middle.
    # We use search_value to find its current position.
    middle_index = search_value(numbers, 25)
    removed = delete_at(numbers, middle_index)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Remove the last item.
    # Nothing has to shift because it is already at the end.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # Checking the index before deletion makes the program
    # safer and prevents it from crashing on invalid positions.

    # =============================
    # TODO (Student): SEARCH TESTS
    # =============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the results with explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    print("Current list:", numbers)

    # Search for 30, which is in the list.
    # The search stops when the value is found.
    result = search_value(numbers, 30)
    print("Searching for 30. Index found:", result)

    # Search for 99, which is not in the list.
    # The search checks every element and returns -1.
    result = search_value(numbers, 99)
    print("Searching for 99. Index found:", result)

    # Linear search is O(n) in the worst case.
    # Searching takes longer when the value is near the end
    # or is missing because more comparisons are needed.

    # =============================
    # TODO (Student): EDGE CASES
    # =============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Try removing an index that does not exist.
    # The function returns None instead of causing an error.
    print("Deleting invalid index 100:", delete_at(numbers, 100))
    print("List after invalid deletion:", numbers)

    # Edge case 2: Try deleting from an empty list.
    # There is nothing to remove, so None is returned.
    empty_list = []
    print("Deleting from empty list:", delete_at(empty_list, 0))

    # Edge case 3: Insert a value into an empty list.
    # This works because index 0 is a valid insertion position.
    insert_at(empty_list, 0, 100)
    print("After inserting into empty list:", empty_list)

    # Edge case 4: Search for a value that does not exist.
    # The search returns -1 instead of an invalid index.
    print("Searching for missing value 500:",
          search_value(numbers, 500))

    # Edge case 5: Try deleting using a negative index.
    # Our validation rejects negative indexes to avoid
    # accidentally removing an unintended item.
    print("Deleting negative index -1:", delete_at(numbers, -1))
    print("Final list:", numbers)


if __name__ == "__main__":
    main()
