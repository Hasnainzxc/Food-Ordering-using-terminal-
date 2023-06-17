import requests

# Talabat API base URL
base_url = 'https://api.talabat.com/api/v1'
# Make a GET request to fetch all restaurants in Dubai
base_url = 'https://api.talabat.com/api/v1'

# Function to get all restaurants and menus in Dubai
def get_dubai_restaurants():
    try:
        # Make GET request to Talabat API to fetch all restaurants in Dubai
        response = requests.get(f"{base_url}/restaurant", params={"city": "Dubai"})
        response.raise_for_status()

        # Extract restaurant names and menus from the response
        restaurants = response.json()
        return restaurants
    except requests.exceptions.RequestException as error:
        print(f"Error fetching Dubai restaurants: {error}")
        return []

# Function to place an order
# (same as before)

# Function to check order status
# (same as before)

# Get all restaurants and menus in Dubai
restaurants = get_dubai_restaurants()

# Display restaurant names and menus
if restaurants:
    print("Restaurants in Dubai:")
    for index, restaurant in enumerate(restaurants, start=1):
        print(f"{index}. {restaurant['name']}")
        print("Menu:")
        for item in restaurant['menu']:
            print(f"- {item['name']}")
else:
    print("No restaurants found in Dubai.")

# Function to place an order
def place_order(order_info):
    try:
        # Make POST request to Talabat API to place the order
        response = requests.post(f"{base_url}/orders", json=order_info)
        response.raise_for_status()

        # Check the response status and handle accordingly
        if response.status_code == 200:
            print("Order placed successfully!")
        else:
            print("Failed to place the order.")
    except requests.exceptions.RequestException as error:
        print(f"Error placing the order: {error}")

# Function to check order status
def check_order_status(order_id):
    try:
        # Make GET request to Talabat API to check the order status
        response = requests.get(f"{base_url}/orders/{order_id}")
        response.raise_for_status()

        # Extract the order status from the response
        order_status = response.json().get("orderStatus")
        print(f"Order Status: {order_status}")
    except requests.exceptions.RequestException as error:
        print(f"Error checking the order status: {error}")

# Get user's GPS coordinates
latitude = input("Enter your latitude: ")
longitude = input("Enter your longitude: ")

# Get nearby restaurants based on GPS coordinates
restaurants = get_nearby_restaurants(latitude, longitude)

# Display restaurant names and menus
if restaurants:
    print("Nearby Restaurants:")
    for index, restaurant in enumerate(restaurants, start=1):
        print(f"{index}. {restaurant['name']}")
        print("Menu:")
        for item in restaurant['menu']:
            print(f"- {item['name']}")
else:
    print("No nearby restaurants found.")

# Select an item to order
selected_item = input("Select an item to order (enter the number): ")

# Validate the selected item
if selected_item.isnumeric() and int(selected_item) <= len(restaurants):
    selected_restaurant = restaurants[int(selected_item) - 1]
    selected_menu_item = selected_restaurant['menu'][int(selected_item) - 1]

    # Confirm the order
    print(f"Confirming order: {selected_menu_item['name']} from {selected_restaurant['name']}")
    confirmation = input("Confirm the order (yes/no): ")

    if confirmation.lower() == "yes":
        # Create the order payload
        order_info = {
            "restaurant": selected_restaurant['name'],
            "orderID": selected_menu_item['id'],
            "orderPrice": selected_menu_item['price'],
            "orderStatus": "Preparing",
            "riderName": "",
            "riderNumber": ""
        }

        # Place the order
        place_order(order_info)

        # Check the order status
        check_order_status(selected_menu_item['id'])
    else:
        print("Order canceled.")
else:
    print("Invalid selection. Order canceled.")
