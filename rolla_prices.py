import numpy as np
import matplotlib.pyplot as plt

# loading in the samples I collected from Zillow
data = [
    (185000, 1920),
    (259000, 1440),
    (184900, 910),
    (247900, 1648),
    (165000, 1344),
    (287500, 2856),
    (192500, 1145),
    (174900, 1726),
    (249900, 2968),
    (299900, 2712),
    (249000, 1200),
    (195000, 1740),
    (159000, 1403),
    (625000, 3600),
    (185000, 1248),
    (200000, 1000),
    (375000, 2647),
    (420000, 3882),
    (270000, 2588),
    (194500, 1728)
]

data = np.array(data)
prices = data[:, 0]
sqft = data[:, 1]

# quick calculation of price per sq ft for each listing
price_per_sqft = prices / sqft

# median of my scraped data
median_scraped = np.median(price_per_sqft)
print("Median scraped price per sq ft:", median_scraped)

# simple scatter plot to show how price relates to square footage
plt.figure(figsize=(8, 6))
plt.scatter(sqft, prices, alpha=0.7)
plt.xlabel("Square Feet")
plt.ylabel("Listing Price ($)")
plt.title("Listing Price vs Square Feet (Rolla, MO)")
plt.grid(True)
plt.show()

# comparing my median to the official FRED number
official_fred_value = 150  # Jan 2026 value from FRED
difference = median_scraped - official_fred_value

print("Official FRED value:", official_fred_value)
print("Difference (scraped - official):", difference)
