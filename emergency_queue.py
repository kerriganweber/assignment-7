class Patient:
    """
    Represents a patient in the emergency queue.

    Attributes:
        name (str): The patient's name.
        urgency (int): An integer from 1 (most urgent) to 10 (least urgent).
    """
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    """
    A min-heap to manage Patient objects by urgency.
    The patient with the lowest urgency score (highest priority) is at index 0.
    """
    def __init__(self):
        self.data = []

    def insert(self, patient):
        """Adds a new patient and restores heap property."""
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        """Prints the current queue of patients."""
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        """Returns the patient with the highest priority without removing them."""
        return self.data[0] if self.data else None

    def remove_min(self):
        """Removes and returns the patient with the highest priority."""
        if not self.data:
            return None
        if len(self.data) == 1:
            return self.data.pop()
        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return min_patient

    def heapify_up(self, index):
        """Moves the patient at index up to restore heap property."""
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        """Moves the patient at index down to restore heap property."""
        size = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    '''
    Current Queue:
    - Taylor (1)
    - Jordan (3)
    - Avery (5)
    '''

    next_up = heap.peek()
    print(next_up.name, next_up.urgency)  # Taylor, 1

    served = heap.remove_min()
    print(served.name)  # Taylor
    heap.print_heap()
    '''
    Current Queue:
    - Jordan (3)
    - Avery (5)
    '''
