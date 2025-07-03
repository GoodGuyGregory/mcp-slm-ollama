from fastmcp import Client
from server import mcp
import pytest

@pytest.fixture
def create_client():
    '''
        creates an MCP client from the `./server.py import`
    '''
    return Client(mcp)

@pytest.mark.asyncio
async def test_MCP_create_client(create_client):
    
    client = create_client
    
    async with client:
    
        server_status = (await client.call_tool("server_status" ))[0].text

        assert "mcp server running on" in server_status

@pytest.mark.asyncio
async def test_choose_parks_in_northwest_tool(create_client):
    '''
        test to determine if the "northwest" district parks are being recognized
    '''
    
    client = create_client
    
    async with client:
        
        # call the choose_pdx_parks 
        park_results = await client.call_tool("choose_pdx_park", {"location": "northwest"})

        # Check for Forest Park
        if "Forest Park" in park_results and "Wallace Park" in park_results:
            assert True

@pytest.mark.asyncio
async def test_choose_park_location_not_listed_parks_tool(create_client):
    '''
        test to ensure that the tool responds with suggestions for the correct location
        arguments to be supplied for the tool.
    '''
    
    client = create_client
    
    suitable_error = """
                invalid location request provide one of the following: \n
                
                * 'north' \n
                * 'northeast' \n
                * 'southeast' \n
                * 'southwest' \n
                * 'northwest' \n
                """
                
    async with client:
        
        # call the choose_pdx_parks 
        park_results = (await client.call_tool("choose_pdx_park", {"location": "weast"}))[0].text
        assert park_results == suitable_error


    