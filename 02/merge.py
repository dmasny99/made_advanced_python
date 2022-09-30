def merge(nums1, nums2):
    left_ptr = 0
    right_ptr = 0
    merged = []
    while left_ptr < len(nums1) and right_ptr < len(nums2):
        if nums1[left_ptr] < nums2[right_ptr]:
            left_ptr += 1
        elif nums1[left_ptr] > nums2[right_ptr]:
            right_ptr += 1
        else:
            if nums1[left_ptr] not in merged:
                merged.append(nums1[left_ptr])
            left_ptr += 1
            right_ptr += 1
    return merged

    
if __name__ == '__main__':
    assert merge([1, 1, 2, 5, 7], (1, 1, 2, 3, 4, 7)) == [1, 2, 7]
    assert merge([1, 2, 3], [1]) == [1]
    assert merge([], []) == []
    assert merge([3, 4, 6, 7, 9, 10], (1, 2, 5, 6, 7, 8, 9, 10)) == [6, 7, 9, 10]