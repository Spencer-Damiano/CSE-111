import csv

def main():
  product_dictionary = get_product_dict()
  print(product_dictionary)

def get_product_dict():
  
  product_dict = {}

  with open('products.csv') as products_csv:
    read_products = csv.reader(products_csv)
    next(read_products)

    for row in read_products:
      product_info = []
      product_num = row[0]
      product_name = row[1]
      product_info.append(product_name)
      product_price = row[2]
      product_info.append(product_price)

      product_dict[product_num] = product_info


  return product_dict

main()
