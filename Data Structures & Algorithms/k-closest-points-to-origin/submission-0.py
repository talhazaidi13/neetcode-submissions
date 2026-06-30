class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def merge_sort(points):
            if len(points) <= 1:
                return points

            mid = len(points) // 2

            left = merge_sort(points[:mid])
            right = merge_sort(points[mid:])

            return merge(left, right)


        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                left_dist = left[i][0]**2 + left[i][1]**2
                right_dist = right[j][0]**2 + right[j][1]**2

                if left_dist <= right_dist:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        array = merge_sort(points)
        return array[:k]