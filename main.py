
def merge(arr1, m, arr2, n):
    res = []

    i, j = 0, 0
    while i < m or j < n:
        if i < m and j < n:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        elif i < m:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    print(res)
# Example usage:
nums1 = [1, 2, 3, 6, 6, 8]
m = 6
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)