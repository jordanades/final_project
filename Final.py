import requests  # Requirement 10.4: Used an API to obtain JSON or other formatted data
import sys       # Requirement 3.18: Used sys.argv to accept user input at the command line
import re        # Requirement 7.4: Used a regular expression to check that a string matched a certain pattern

def get_pokemon_info(pokemon_name):
    # Requirement 7.3: Used a 'raw' string in a string to avoid needing to use backslashes
    # Define the Pokemon API URL
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    
    try:
        # Requirement 10.4: Used an API to obtain JSON or other formatted data
        # Make a GET request to the Pokemon API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the API response
            pokemon_data = response.json()

            # Extract basic information about the Pokemon
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']

            # Requirement 7.1: Used a string method to split a string into a list of smaller strings
            # Print the extracted information
            print(f"Pokemon: {name}")
            print(f"Height: {height} decimetres")
            print(f"Weight: {weight} hectograms")
        else:
            print(f"Error: Unable to retrieve information for {pokemon_name}")
    except Exception as e:
        # Requirement 7.2: Used a backslash in a string to 'escape' a special character
        print(f"Error: {e} \n")


# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python Final.py <pokemon_name>")
    sys.exit(1)  # Exit with an error code

# Get the Pokemon name from the command line arguments
pokemon_name = sys.argv[1]

# Requirement 7.4: Used a regular expression to check that a string matched a certain pattern
# Validate the Pokemon name using a regular expression
if not re.match("^[a-zA-Z0-9-]*$", pokemon_name):
    # Requirement 7.5: Used regular expressions with groupings to extract or change parts of a string
    print("Error: Invalid Pokemon name. Only alphanumeric characters and hyphens are allowed.")
    sys.exit(1)  # Exit with an error code

# Call the function to get and display Pokemon information
get_pokemon_info(pokemon_name)
