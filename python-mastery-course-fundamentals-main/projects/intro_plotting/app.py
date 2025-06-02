import matplotlib.pyplot as plt
from random import choice

data = [23, 1, 34, 2, 12, 89]
style_list = [
    "Solarize_Light2",
    "_classic_test_patch",
    "_mpl-gallery",
    "_mpl-gallery-nogrid",
    "bmh",
    "classic",
    "dark_background",
    "fast",
    "fivethirtyeight",
    "ggplot",
    "grayscale",
    "seaborn-v0_8",
    "seaborn-v0_8-bright",
    "seaborn-v0_8-colorblind",
    "seaborn-v0_8-dark",
    "seaborn-v0_8-dark-palette",
    "seaborn-v0_8-darkgrid",
    "seaborn-v0_8-deep",
    "seaborn-v0_8-muted",
    "seaborn-v0_8-notebook",
    "seaborn-v0_8-paper",
    "seaborn-v0_8-pastel",
    "seaborn-v0_8-poster",
    "seaborn-v0_8-talk",
    "seaborn-v0_8-ticks",
    "seaborn-v0_8-white",
    "seaborn-v0_8-whitegrid",
    "tableau-colorblind10",
]

style = choice(style_list)
print(style)
plt.style.use(str(style))
fig, ax = plt.subplots()
ax.plot(data, linewidth=3)

ax.set_title("Simple Plot of Randomness")

# adding labels
ax.set_xlabel("x")
ax.set_ylabel("y")


# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
plt.show()
