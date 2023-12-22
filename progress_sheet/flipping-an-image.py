class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image=[m[::-1] for m in image]
        for i in range(len(image)):
            for j in range(len(image)):
                image[i][j]=int(not(image[i][j]))
        return image
