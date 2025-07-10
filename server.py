# server.py:
# this file is for hosting the FastMCP server
# contains tools we define.
from fastmcp import FastMCP
from typing import List
import os
from dotenv import load_dotenv

import colorama
import json

load_dotenv()

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

mcp = FastMCP(name="Local MCP Server", host=HOST, port=PORT)

# Tools:
@mcp.tool
def choose_pdx_park(location: str) -> str:
    '''
        choose a park based on the incoming location provided by the user. 
        if nothing is matchable for the `location` provided, returns the suggestion to search for a park at the PDX parks 
        website.
        
        Args:
            location (str): corresponds to the location where the user is to search against
        Returns:
            park_recommendation (str): the chosen park closest to the specified user location
    '''
    
    # Open and parse the options for user recommendation
    try:
        with open("./db/parks.json", "r") as parks_file:
            
            pdx_parks = json.load(parks_file)
            
    except FileNotFoundError:
        print(colorama.Fore.YELLOW + "Error: \n Parks Database File not found")
    except json.JSONDecodeError:
        print(colorama.Fore.YELLOW + "Error: \n `parks.json` is not properly formatted please check the source file for this tool.")
    except Exception as err:
        print(colorama.Fore.RED + f"Error: something went wrong... \n {err}")
    
    # attempt to access the provided location
    search_loc = location.strip().lower()
    
    if search_loc in pdx_parks:
        park_options = pdx_parks.get(search_loc)
        
        park_suggestions = f"it appears you are looking for parks in the: {search_loc} \n here are some suggestions \n "
        for park in park_options:
            park_suggestions += f" * {park} \n"
        
        return park_suggestions
    else:
        return """
                invalid location request provide one of the following: \n
                
                * 'north' \n
                * 'northeast' \n
                * 'southeast' \n
                * 'southwest' \n
                * 'northwest' \n
                """
    

if __name__ == "__main__":
    # enable stdio client support:
    # mcp.run(transport="stdio")
    # enable streamable-http support:
    mcp.run(transport="streamable-http")
    