from lxml import etree

# Load and parse the XML file
tree = etree.parse(r'C:\Users\chand\Downloads\IV SEM\WP-1\EXP-4\perfume.xml')
root = tree.getroot()

# Queries remain the same
# 1. Find all perfume names and their prices.
perfume_names_prices = [(perfume.find("name").text, float(perfume.find("price").text)) for perfume in root.findall("perfume")]
print("Perfume names and their prices:", perfume_names_prices)

# 2. Get the details of the perfume with the highest price.
highest_price_perfume = max(root.findall("perfume"), key=lambda x: float(x.find("price").text))
highest_price_details = {
    "name": highest_price_perfume.find("name").text,
    "brand": highest_price_perfume.find("brand").text,
    "price": float(highest_price_perfume.find("price").text),
    "quantity": int(highest_price_perfume.find("quantity").text)
}
print("Details of the perfume with the highest price:", highest_price_details)

# 3. List perfumes with a quantity greater than 20.
perfumes_quantity_gt_20 = [(perfume.find("name").text, int(perfume.find("quantity").text)) for perfume in root.findall("perfume") if int(perfume.find("quantity").text) > 20]
print("Perfumes with a quantity greater than 20:", perfumes_quantity_gt_20)

# 4. Calculate the total quantity of all perfumes.
total_quantity = sum(int(perfume.find("quantity").text) for perfume in root.findall("perfume"))
print("Total quantity of all perfumes:", total_quantity)
