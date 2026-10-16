#====================================================
#|                                                  |
#|       6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ        |
#|                                                 |
#===================================================

class MyCollection:
    """Base collection defining shared storage and common behaviors."""

    def __init__(self):
        self.items = []

    def show(self):
        """Displays all elements currently stored in the collection."""
        print(
            f"{self.__class__.__name__} ({len(self.items)} items): {self.items}"
        )

    def remove(self, item):
        """Removes a single instance of the item from the collection."""
        if item in self.items:
            self.items.remove(item)
            print(f"Removed: {item}")
        else:
            print(f"Cannot remove '{item}': not found in collection.")


class myBag(MyCollection):
    """A Bag (multiset) collection inheriting from MyCollection.

    Allows duplicate items of any type.
    """

    def add(self, item):
        """Adds an item into the bag, preserving duplicates."""
        self.items.append(item)
        print(f"Added: {item}")

if __name__ == "__main__":
    # Custom class to demonstrate storing arbitrary objects
    class Book:

        def __init__(self, title):
            self.title = title

        #built-in method to describe the object
        def __repr__(self):
            return f"Book('{self.title}')"
        #built-in method to help when remove object
        def __eq__(self, other):
            return isinstance(other, Book) and self.title == other.title

    bag = myBag()

    print("--- 1. Testing with Integers (duplicates allowed) ---")
    bag.add(10)
    bag.add(20)
    bag.add(10)  #Testing a duplicate integer
    bag.show()

    bag.remove(10)
    bag.show()

    print("\n--- 2. Testing with Any Type of Objects ---")
    bag.add("hello")
    bag.add(3.14)
    b1 = Book("Das Kapital")
    bag.add(b1)
    bag.show()

    bag.remove(3.14)
    #If doesn't has __eq__() it will not remove.
    bag.remove(Book("Das Kapital"))
    bag.show()