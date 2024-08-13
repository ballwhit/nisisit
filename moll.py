class Tag:
    def __init__(self, y0, y1):
        self.y0 = y0
        self.y1 = y1

# Create a Tag object with specific y-coordinates
tag = Tag(10, 50)

# Calculate the height of the element
h = tag.y1 - tag.y0

print(f"The height of the element is: {h}")
