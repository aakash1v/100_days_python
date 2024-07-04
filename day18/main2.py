import colorgram

rgb_colors = []

# Extract 12 colors from picture
colors = colorgram.extract('image.jpg',12)

for _ in range(12):
    color = colors[0]
    rgb_colors.append(color.rgb)

print(*rgb_colors)
