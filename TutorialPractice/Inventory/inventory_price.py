import csv

def csv_file_process(csv_file):
  
  total_inventory_cost=0
  
  with open(csv_file,'r') as file:
    
    reader=csv.DictReader(file)
    
    for i in reader:
      
      total_inventory_cost=total_inventory_cost+(int(i['quantity_in_stock']))*(float(i['unit_price']))
  
  return total_inventory_cost    

result=csv_file_process("C:\PythonPrograms\TutorialPractice\Inventory\data.csv")

print(f"Total cost of the inventory is $ {result}")