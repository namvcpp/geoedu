import sys, os, math, random
import geopy
import geoplot
import geoplot.crs as gcrs
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

'''
def city_coordinates_border(city):
    for i in vnmapjson['features']:
        if i['properties']['name'] == city:
            return i['geometry']['coordinates'][0]
'''

if __name__ == "__main__":
    '''
    fileMapJson = open('vn.json', mode="r", encoding="utf-8")
    vnmapjson = json.load(fileMapJson)
    '''
    data = gpd.read_file('vn.json')
    #data = gpd.read_file("https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/france.geojson")
    #print(data.crs)
    #print(type(data))
    geoplot.polyplot(data, projection=gcrs.AlbersEqualArea(), edgecolor='darkgrey', facecolor='lightgrey', linewidth=.3, figsize=(12, 8))
    '''
    #print(city_coordinates_border("An Giang"))
    pygame.init()

    # Create Screen
    x_screen = 1000
    y_screen = 600
    screen = pygame.display.set_mode((x_screen, y_screen))



    location_color = (255, 51, 153)
    background_color = (255, 255, 255)

    COLOR_INACTIVE = pygame.Color('grey')
    COLOR_ACTIVE = pygame.Color('pink')
    FONT = pygame.font.Font(None, 32)
    color = pygame.Color('pink')
    text_color = pygame.Color('black')

    true_color = (0, 204, 0)
    false_color = (255, 0, 0)

    hint_list = []

    # Title of screen
    pygame.display.set_caption("Wero - Wordle")

    # Text title
    title_size = 50
    body_size = 30
    end_game_size = 100
    font_title = pygame.font.SysFont("Times New Roman", title_size, bold=True)
    font_body = pygame.font.SysFont("Times New Roman", body_size, bold=True)
    font_end_game = pygame.font.SysFont("comicsans", end_game_size, bold=True)
    geolocator = Nominatim(user_agent="geoedu")

    x_namegame = (x_screen // 2)
    y_namegame = 0
    x_mid = x_screen // 2
    y_mid = y_screen // 2

    screen.fill("white")
    pygame.display.flip()

    cities = ['an giang', 'ba ria-vung tau', 'bac giang', 'bac kan', 'bac lieu', 'bac ninh', 'ben tre',
            'binh dinh', 'binh duong', 'binh phuoc', 'binh thuan', 'ca mau', 'can tho', 'cao bang',
            'da nang', 'dak lak', 'dak nong', 'dien bien', 'dong nai', 'dong thap', 'gia lai',
            'ha giang', 'ha nam', 'ha noi', 'hai duong', 'ha tinh', 'hai duong', 'hai phong',
            'hau giang', 'hoa binh', 'ho chi minh', 'hung yen', 'khanh hoa', 'kien giang', 'kon tum',
            'lai chau', 'lam dong', 'lang son', 'lao cai', 'long an', 'nam dinh', 'nghe an',
            'ninh binh', 'ninh thuan', 'phu tho', 'phu yen', 'quang binh', 'quang nam', 'quang ngai',
            'quang ninh', 'quang tri', 'soc trang', 'son la', 'tay ninh', 'thai binh', 'thai nguyen',
            'thanh hoa', 'thua thien hue', 'tien giang', 'tra vinh', 'tuyen quang', 'vinh long',
            'vinh phuc', 'yen bai', 'kien giang']
    
    #print(geopy.location.Location(cities[0]))

    #print(geolocator.geocode(cities[0], country_codes="vn", featuretype="city"))
    #sys.exit()
    Exit = False
    while not Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = 0
                pygame.quit()
                sys.exit()
        #citymap = pygame.draw.polygon(screen, "black", city_coordinates_border("An Giang"), 10)
        #citymap = pygame.draw.polygon(screen, "black", [[100, 100], [0, 200], [200, 200]], 5)
        citymap = pygame.draw.polygon(screen, "black", [[0, 0], [100, 0], [100, 100], [0, 100]], 5)
        pygame.display.update(citymap)

        #pygame.display.flip()

    '''
