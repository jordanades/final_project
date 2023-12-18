import requests  
import sys       
import re        

def get_pokemon_info(pokemon_name):
    # 7.3: Used a 'raw' string in a string to avoid needing to use backslashes
    # Defined the Pokemon API URL
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    
    try:
        # 10.4: Used an API to obtain JSON or other formatted data
        # Make a GET request to the Pokemon API
        response = requests.get(api_url)

        # Checked here if the request was successful (status code 200 means it was)
        if response.status_code == 200:
            # Took JSON data here from the API response
            pokemon_data = response.json()

            # Extracted basic height and weight information about the Pokemon
            # 10.5: Extracted or manipulated values from JSON formatted data.
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']

            # 7.1: Used a string method to split a string into a list of smaller strings
            # Converted the Pokemon name into a list of characters
            name_characters = list(name)

            # Print each character separately
            print("Pokemon Name Characters:")
            for char in name_characters:
                print(char)

            print(f"Height: {height} decimetres")
            print(f"Weight: {weight} hectograms")
        else:
            print(f"Error: Unable to retrieve information for {pokemon_name}")
    except Exception as e:
        # 7.2: Used a backslash in a string to 'escape' a special character
        print(f"Error: {e} \n")


# Check if the correct number of command line arguments is provided
# 3.18: Used sys.argv to accept user input at the command line
if len(sys.argv) != 2:
    print("Usage: python Final.py <pokemon_name>")
    sys.exit(1)  # Exit with an error code

# Get the Pokemon name from the command line arguments
pokemon_name = sys.argv[1]

# 7.4: Used a regular expression to check that a string matched a certain pattern
# Validate the Pokemon name using a regular expression
if not re.match("^[a-zA-Z0-9-]*$", pokemon_name):
    print("Error: Invalid Pokemon name. Only alphanumeric characters and hyphens are allowed.")
    sys.exit(1)  # Exit with an error code

# Call the function to get and display Pokemon information
get_pokemon_info(pokemon_name)
