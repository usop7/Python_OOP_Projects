import aiohttp
import asyncio


async def get_starwars_people_data(id: int, session: aiohttp.ClientSession, url: str) -> dict:
    target_url = url.format(id)
    response = await session.request(method="GET", url=target_url)
    print(response)
    print(type(response))
    json_dict = await response.json()
    print(json_dict)


async def get_data(requests: list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for request in requests:
            task = asyncio.create_task(get_starwars_people_data(request.get('id'), session, request.get('url')))
            tasks.append(task)
        await asyncio.gather(*tasks)


def main():
    data = []
    request = {'url': 'https://swapi.co/api/people/{}/', 'id': 4}
    data.append(request)
    asyncio.run(get_data(data))


if __name__ == '__main__':
    main()