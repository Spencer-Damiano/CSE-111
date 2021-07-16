import datetime 
from random import randint

def rocko_meals_main():
  weekly_order = {}
  master_customer_info = {}

  def customer_main(function_required=None):
    """
    Parameters: function_required = None - this is because it might be helpful to call a function without user input 
    Variables: 
      customer_csv_file - file name with customers in it
    Purpose: add a new customer (if needed), read the csv file, make it a dictionary
    Functions: 
      read_csv(customer_csv_file) - returns the csv as a usable vaiable
      add_new_customer(read_csv) - gets customer information and adds it to the csv file
        add_to_csv(read_csv)- adds the information to the csv_file
      get_all_customer_info(read_csv) - makes a dictionary of existing customers
      get_one_customer_info(read_csv) - gets just one customers informations based on a radnomly generated number
    return customer_info
    """
    def get_all_customer_info():
      """
      Paramiters: csv_customers - dictionary
      Purpose: to get a dictionary of existing customers
      Return: customer_info - (dict) existing customers
      """
    def break_down_recipe(customer_info):
      """
      Paramiters: customer_info (to be used in finding the cost to customer)
      Purpose: open csv files, find out cost to customer, get the recipe info, return this information
      Functions: 
        csv_open - returns a dictionary with the recipe info from a master recipie sheet
        cost_to_customer - uses customer information to figure out how much it would be for that customer as well as the portion
        get_get_recpie_info - gets the recipe we are using, possibly, all recipies in a loop 
      """
    
    def add_new_customer(read_csv):
      """
      Purpose: doesn't return anything, just adds the new customer info into the cvs file.
      """

  def recipe_main():
    """
    Paraminters: none
    Purpose: To figure out what we need to order and returns it in a dictionary
    Functions: 
      get_purpose
    """

def main():
