"""This module contains function for finding n-order statistics in an array."""
import heapq


class InteractiveMedian:
    def __init__(self, mod: int = 10**4):
        self._max_heap = []  # max on the top
        self._min_heap = []  # min on the top

        self.medan_sum = 0
        self.mod = mod

    def insert(self, element: int) -> int:
        """Insert new element and get median value.

        Args:
            element (int): Element to insert.
        """
        if len(self._max_heap) == 0:
            heapq.heappush(self._max_heap, -element)
        else:
            left = -heapq.heappop(self._max_heap)
            heapq.heappush(self._max_heap, -left)
            if element <= left:
                heapq.heappush(self._max_heap, -element)
            else:
                if len(self._min_heap) == 0:
                    heapq.heappush(self._min_heap, element)
                else:
                    right = heapq.heappop(self._min_heap)
                    heapq.heappush(self._min_heap, right)
                    if element >= right:
                        heapq.heappush(self._min_heap, element)
                    else:
                        heapq.heappush(self._max_heap, -element)

        # Balance
        if len(self._max_heap) - len(self._min_heap) > 1:
            heapq.heappush(self._min_heap,
                           -heapq.heappop(self._max_heap))
        elif len(self._min_heap) - len(self._max_heap) > 1:
            heapq.heappush(self._max_heap,
                           -heapq.heappop(self._min_heap))

        # Find median
        if len(self._max_heap) >= len(self._min_heap):
            median = -heapq.heappop(self._max_heap)
            heapq.heappush(self._max_heap, -median)

        else:
            median = heapq.heappop(self._min_heap)
            heapq.heappush(self._min_heap, median)

        self.medan_sum = (self.medan_sum + median) % self.mod
        return median
