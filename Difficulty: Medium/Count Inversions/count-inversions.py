class Solution:
    def inversionCount(self, arr):
        def merge(left, right):
            i = 0
            j = 0
            count = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                    count += len(left) - i
            res.extend(left[i:])
            res.extend(right[j:])
            return res, count

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, left_count = mergeSort(arr[:mid])
            right, right_count = mergeSort(arr[mid:])
            merged, merge_count = merge(left, right)
            return merged, left_count + right_count + merge_count

        _, count = mergeSort(arr)
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends