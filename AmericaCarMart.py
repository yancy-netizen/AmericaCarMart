import requests
import re
import json

cookies = {
    '__cf_bm': 'GS0eWbLsYb0ZX2I3Adk6HsmReu_RRKTQPmbK4hqpKkQ-1763243280-1.0.1.1-Xm2XbG3d06E1OEI7fsxbWUwssfChfLARDCt4g5UBV99DZgNw0um4D9JUbRXYSaKlic.6vEjrXBMrYfnCdJ32L8b0l4ISYsO60ZDSRtOjY.ZRcnGd3nH73I7yErV4L4nB',
    'nabSegmentation': '%7B%22activeSegments%22%3A%7B%7D%2C%22geo%22%3A%7B%22location%22%3A%22%22%2C%22ipAddress%22%3A%22%22%2C%22lastUpdate%22%3A%22%22%7D%2C%22firstVisit%22%3A1763243280845%7D',
    '_omappvp': 'IoLW39E6T0886YLMBBD8QlBNNgRqm83bH5l080DOl8XebQG757ZMeGv4Eevj6DiLwP4952EnQ4L9zvYA69D8CH9SvQ2XTIcE',
    '_ga': 'GA1.1.1643212430.1763243281',
    '_gcl_au': '1.1.1724016733.1763243281',
    'cf_clearance': 'zCI2I1LdtLQ1t4RUiUSrGaiOe8bWvw8j8Sj5h3KQUsY-1763243281-1.2.1.1-hN4tzKYC1tRGgbWRj3zn.FZmlsafG_bXhvKnrWzwrKDRDHZzTLD6HV4Rpxs1CzbDpGUj9VGi3IPRDTo7SUSgHLquomy5XRc_LaA93gpQLwTQwizn_DQJqKdS1RYtwiTHeWzi0QyqaMAGVZEOZMgf5k2A60TSoZBUuAapLlOv7mNCQNXOQffntD48G_1qARhIH5ReGQY4S.Q.xUMtzvU_si0yNMvkGVcPh_WQRDsu5Fc',
    '_fbp': 'fb.1.1763243281507.57014976411554461',
    '_clck': '17h4nf7%5E2%5Eg11%5E0%5E2145',
    'fullthrottlelims_t2': '4538233057',
    'r': '1',
    'acs': '1',
    'lat': '41.636776',
    'lon': '-74.3235539',
    'acc': '87425.05058087864',
    'src': 'g',
    'omSeen-tqcxkk0a1a6nrmzhk9t1': '1763243317280',
    'om-tqcxkk0a1a6nrmzhk9t1': '1763243317965',
    'UserTracking': '{%22TrackedVins%22:%22%22%2C%22TrackedLotIds%22:%22163%22%2C%22EventCode%22:%22%22%2C%22SourceType%22:%22%22}',
    'NearbyLotIds': '[%22163%22%2C%22112%22%2C%22012%22%2C%22053%22%2C%22089%22%2C%22010%22%2C%22170%22%2C%22002%22]',
    'NearbyLotsInfo': '[{%22Id%22:%22112%22%2C%22Name%22:%22CAR-MART%20of%20Rogers-North%22%2C%22State%22:%22AR%22%2C%22City%22:%22Rogers%22%2C%22Street%22:%222620%20W%20Hudson%20Rd%22%2C%22Zip%22:%2272756%22}%2C{%22Id%22:%22012%22%2C%22Name%22:%22CAR-MART%20of%20Rogers%22%2C%22State%22:%22AR%22%2C%22City%22:%22Rogers%22%2C%22Street%22:%222007%20S%208th%20St%22%2C%22Zip%22:%2272758%22}%2C{%22Id%22:%22053%22%2C%22Name%22:%22CAR-MART%20of%20Springdale%22%2C%22State%22:%22AR%22%2C%22City%22:%22Springdale%22%2C%22Street%22:%223733%20W%20Sunset%20Ave%22%2C%22Zip%22:%2272762%22}]',
    'omSeen-tlqfizrqpne6kjuqtkzt': '1763243333013',
    'InventorySearchFilters': '',
    'LotInformation': '{%22LotId%22:%22163%22%2C%22Name%22:%22CAR-MART%20of%20Centerton%22%2C%22Phone%22:%22479-224-7010%22%2C%22Hours%22:%229%20AM%20-%206%20PM%22%2C%22Street%22:%22350%20W%20Centerton%20Blvd%20%22%2C%22City%22:%22Centerton%22%2C%22State%22:%22AR%22%2C%22Zip%22:%2272719%22%2C%22Latitude%22:%22%22%2C%22Longitude%22:%22%22%2C%22PodiumWebchatToken%22:%220315184b-6df4-4d6b-af9d-4d5096200c0c%22%2C%22PodiumWebchatStart%22:%229:00%20AM%22%2C%22PodiumWebchatEnd%22:%225:00%20PM%22}',
    '_omappvs': '1763243333548',
    '_uetsid': 'c1fb1eb0c26c11f0981a4598ae765ef7',
    '_uetvid': 'c1fb1e10c26c11f0937737a1b33894fb',
    '_clsk': '3fr8qi%5E1763243333859%5E4%5E1%5Eq.clarity.ms%2Fcollect',
    'omSeen-wzow1a5ajqnki77uhtqm': '1763243339384',
    'om-wzow1a5ajqnki77uhtqm': '1763243341660',
    '_ga_70GJ0W1ZCN': 'GS2.1.s1763243281$o1$g1$t1763243366$j60$l0$h0',
    '_ga_BNJR9YWZHD': 'GS2.1.s1763243281$o1$g1$t1763243366$j60$l0$h0',
    'InventoryScrollPosition': '3255.199951171875',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.car-mart.com/locations/163/centerton-arkansas/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

response = requests.get('https://www.car-mart.com/cars/163/centerton-arkansas/', cookies=cookies, headers=headers)

# Extract all car listing links using regex
pattern = r'href="(/for-sale/[^"]+)"'
matches = re.findall(pattern, response.text)

# Create full URLs and remove duplicates
base_url = 'https://www.car-mart.com'
full_urls = sorted(set(base_url + url for url in matches))

# Parse links and extract make, model, VIN
cars = []
for url in full_urls:
    # Pattern: /for-sale/{lot}/{make}/{model}/{vin}/
    match = re.search(r'/for-sale/\d+/([^/]+)/([^/]+)/([^/]+)/?$', url)
    if match:
        make = match.group(1).title()
        model = match.group(2).replace('-', ' ').title()  # Replace hyphens with spaces
        vin = match.group(3)
        
        cars.append({
            'link': url,
            'make': make,
            'model': model,
            'vin': vin
        })

# Write to JSON file
with open('acm_direct_links.json', 'w') as f:
    json.dump(cars, f, indent=2)

print(f"Found {len(cars)} unique car listings")
print(f"Links saved to acm_direct_links.json")
print("\nFirst 5 entries:")
for car in cars[:5]:
    print(f"  Make: {car['make']}, Model: {car['model']}, VIN: {car['vin']}")
    print(f"  Link: {car['link']}\n")