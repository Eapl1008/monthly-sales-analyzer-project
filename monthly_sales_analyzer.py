# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total = 0
    for day_data in data:
        if product_key in day_data:
            total += day_data[product_key]
    return f'{total:,}'


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total_ventas = 0
    dias_con_venta = 0
    for dia in data:
        if product_key in dia:
            total_ventas += dia[product_key]
            dias_con_venta += 1
    if dias_con_venta > 0:
        return total_ventas/dias_con_venta
    else: 
        return 0


def best_selling_day(data):
    """Finds the day with the highest total sales."""
    total = 0
    dias = 0
    for ventas in data:
        ventas_totales = sum(v for k, v in ventas.items() if k != 'day')
        if ventas_totales > total:
            total = ventas_totales
            dias = ventas['day']
    return dia


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    total = 0
    for ventas in data:
        if product_key in ventas and ventas[product_key] > threshold:
            total += 1
    return total


def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    maximo_producto_vendidos = {}
    for ventas in data:
        for producto, cantidad in ventas.items():
            if producto != 'day':
                maximo_producto_vendidos[producto] = maximo_producto_vendidos.get(producto, 0) + cantidad
    max_producto = max(maximo_producto_vendidos, key = maximo_producto_vendidos.get)
    return max_producto

def worst_day_sales(data):
  """Finds the day with the worst day of sales"""
  if not data: 
      return None

  min_total_sales = sum(v for k, v in data[0].items() if k != "day")
  worst_day = data[0]["day"]

  for ventas in data[1:]:
        sum_day = sum(v for k, v in ventas.items() if k != "day")
        if sum_day < min_total_sales:
            min_total_sales = sum_day
            worst_day = ventas["day"]
  return worst_day

def ventas_top3(data):
  """Top 3 days of selling"""
  venta_por_dia = []
  for ventas in data:
    suma_por_dia = sum(value for key, value in ventas.items() if key != 'day')
    venta_por_dia.append({'day': ventas['day'],
                          'venta_total': suma_por_dia})

  venta_diaria = sorted(venta_por_dia, key=lambda x: x['venta_total'], reverse=True)

  return venta_diaria[:3]

def max_and_min(data, product_key):
  """Calculates the maximum and minimum sales for a specific product."""
  ventas_diarias = []
  for dia in data:
    if product_key in dia:
      ventas_diarias.append(dia[product_key])

  if not ventas_diarias:
    return {'Producto': product_key, 'Máximo': None, 'Mínimo': None}
  
  return {'Producto': product_key, 'Máximo': max(ventas_diarias), 'Mínimo': min(ventas_diarias)}

# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
print("The day with the worst sales:", worst_day_sales(sales_data))
print("The Top3 in sales:", ventas_top3(sales_data))
print("Max and Min in sales of a specific product:", max_and_min(sales_data, "product_a"))


