# LeetCode 11: Container With Most Water
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def maxArea(self, height):
        # Length of the height array
        le = len(height)

        # Initialize two pointers
        a = 0            # Left pointer
        b = le - 1       # Right pointer

        # Variable to store the maximum water area
        max_area = 0

        # Loop until the two pointers meet
        while a != b:
            # Width is the distance between the two pointers
            width = b - a

            # Height of the container is decided by the shorter line
            con_height = min(height[a], height[b])

            # Calculate the area formed by the current pair of lines
            area = width * con_height

            # Update maximum area if current area is greater
            max_area = max(area, max_area)

            # Move the pointer with smaller height
            # This gives a chance to find a taller line
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        # Return the maximum water that can be stored
        return max_area
