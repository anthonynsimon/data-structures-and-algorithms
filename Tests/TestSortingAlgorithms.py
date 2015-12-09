import unittest
from SortAndSearch import BubbleSort
from SortAndSearch import SelectionSort
from SortAndSearch import InsertionSort
from SortAndSearch import ShellSort
from SortAndSearch import MergeSort
# from SortAndSearch import QuickSort

class TestSortingAlgorithms(unittest.TestCase):
    def getUnsortedList(self):
        return [14,17,15,6,4,0,19,7,13,12,20,10,2,5,1,11,18,16,3,9,8]

    def getCorrectResult(self):
        correctResult = []
        for i in range(21):
            correctResult.append(i)
        return correctResult

    def runTest(self, sortingAlgorithm):
        numbers = self.getUnsortedList()
        sortingAlgorithm.sort(numbers)
        self.assertEqual(numbers, self.getCorrectResult())

    def testBubbleSort(self):
        self.runTest(BubbleSort.BubbleSort())

    def testSelectionSort(self):
        self.runTest(SelectionSort.SelectionSort())

    def testInsertionSort(self):
        self.runTest(InsertionSort.InsertionSort())

    def testShellSort(self):
        self.runTest(ShellSort.ShellSort())

    def testMergeSort(self):
        self.runTest(MergeSort.MergeSort())

    # def testQuickSort(self):
    #     self.runTest(QuickSort.QuickSort())


suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAlgorithms)
unittest.TextTestRunner(verbosity=2).run(suite)