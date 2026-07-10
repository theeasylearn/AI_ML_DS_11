import matplotlib.pyplot as plt
years = list(range(2020, 2025))
it = [10000, 12000, 14000, 16000, 15000]
management = [5000, 6000, 7000, 8000, 7500]
arts = [2000, 4000, 5000, 6000, 4500]
# 'management_bottom' is the combined height of IT and Arts bars
management_bottom = [i_item + a_item for i_item, a_item in zip(it, arts)]
# 1. Plot Base Layer (IT)
plt.bar(years, it, label='IT', color='green')
# 2. Plot Middle Layer (Arts) - stacked on top of IT
plt.bar(years, arts, label='arts', color='red', bottom=it)
# 3. Plot Top Layer (Management) - stacked on top of IT + Arts
plt.bar(years, management, label='management', color='orange', bottom=management_bottom)
plt.xlabel("years")
plt.ylabel("No of admission")
plt.title("No admission in different branches each year")
plt.grid(which='both', zorder=0) # Keeps grid lines behind the bars
plt.legend()
plt.tight_layout()
plt.show()