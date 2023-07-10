#!/usr/bin/env python3

from app import app
from models import db, City, Continent, Food, Concities

with app.app_context():
    
    City.query.delete()
    Continent.query.delete()
    Food.query.delete()
    Concities.query.delete()

    foods = []
    

    # Istanbul
    foods.append(Food(name="Kebap", image="https://as2.ftcdn.net/v2/jpg/03/42/40/99/1000_F_342409940_Db8npTOsw59qJ3EGZrdmB87QypzZ1rY5.jpg", description="Authentic Turkish kebap", restaurant_recommendation="Eylemin Yeri", city_id=1))
    foods.append(Food(name="Baklava", image="https://as2.ftcdn.net/v2/jpg/03/35/90/57/1000_F_335905730_kB6jrKXxzHu1BMuYafDuNzs9ehRhzyGa.jpg", description="Sweet pastry with nuts and honey", restaurant_recommendation="Hafiz Mustafa", city_id=1))
    foods.append(Food(name="Lahmacun", image="https://i.pinimg.com/originals/f1/4d/da/f14dda97b5a227068cba7d7a57587700.jpg", description="Thin Turkish pizza with meat and vegetables", restaurant_recommendation="Halil Usta", city_id=1))

    # Paris
    foods.append(Food(name="Croissant", image="https://i.pinimg.com/564x/de/1e/a9/de1ea94c55c2cc01997c4ef1b42a5fac.jpg", description="Buttery and flaky French pastry", restaurant_recommendation="Pierre Hermé", city_id=2))
    foods.append(Food(name="Escargots", image="https://i.pinimg.com/564x/e4/3f/c3/e43fc3cfc76cb0d7e437c1ced98cb97c.jpg", description="Snails cooked in garlic and herb butter", restaurant_recommendation="L'Ambroisie", city_id=2))
    foods.append(Food(name="Crème Brûlée", image="https://i.pinimg.com/564x/e1/22/cc/e122cc913e66f95e281fda705382daa0.jpg", description="Rich custard dessert with caramelized sugar on top", restaurant_recommendation="Le Comptoir du Relais", city_id=2))

    # Rome
    foods.append(Food(name="Pasta Carbonara", image="https://i.pinimg.com/564x/ec/da/5b/ecda5bd39b966db612dc6fd5d122cc46.jpg", description="Creamy pasta with egg, cheese, and pancetta", restaurant_recommendation="Roscioli", city_id=3))
    foods.append(Food(name="Pizza Margherita", image="https://i.pinimg.com/564x/22/21/04/222104939ae5f28a74e075fa46c00b01.jpg", description="Classic pizza with tomato, mozzarella, and basil", restaurant_recommendation="Pizzarium", city_id=3))
    foods.append(Food(name="Gelato", image="https://i.pinimg.com/564x/a5/04/d7/a504d7f2e4857a87bfd22b0c9f3a0c98.jpg", description="Italian-style ice cream in various flavors", restaurant_recommendation="Giolitti", city_id=3))

    # Barcelona
    foods.append(Food(name="Paella", image="https://i.pinimg.com/564x/83/14/b6/8314b6a869003fd4ce2937025ee0e2ba.jpg", description="Traditional Spanish rice dish with saffron and seafood", restaurant_recommendation="Can Majó", city_id=4))
    foods.append(Food(name="Tapas", image="https://i.pinimg.com/564x/32/7b/11/327b11b0734d1db800096e7be6bf2b96.jpg", description="Assortment of small dishes, often served with drinks", restaurant_recommendation="El Xampanyet", city_id=4))
    foods.append(Food(name="Sangria", image="https://i.pinimg.com/564x/dd/72/7a/dd727a180433aa485e1f9fb63e4ea310.jpg", description="Fruity wine punch with added spirits and fruits", restaurant_recommendation="Bar Ramón", city_id=4))

    # Prague
    foods.append(Food(name="Trdelník", image="https://i.pinimg.com/564x/c8/da/f9/c8daf974ff58ec923d24152dab6c55fc.jpg", description="Sweet pastry cooked over an open flame", restaurant_recommendation="Good Food Coffee and Bakery", city_id=5))
    foods.append(Food(name="Goulash", image="https://i.pinimg.com/originals/c1/14/4a/c1144a34b307afba4812ba89d3234b9f.jpg", description="Hearty Czech stew with meat and vegetables", restaurant_recommendation="Lokál", city_id=5))
    foods.append(Food(name="Svíčková", image="https://i.pinimg.com/564x/d5/15/27/d515271a66c997dfc2cfecd2e7515713.jpg", description="Braised beef with creamy sauce, served with dumplings", restaurant_recommendation="U Kroka", city_id=5))

    # Amsterdam
    foods.append(Food(name="Stroopwafel", image="https://i.pinimg.com/564x/d5/42/fb/d542fbd38e22bedb63eef031d45d1420.jpg", description="Thin waffle filled with caramel syrup", restaurant_recommendation="Albert Cuypmarkt", city_id=6))
    foods.append(Food(name="Haring", image="https://i.pinimg.com/originals/1b/69/c5/1b69c59d88327680b836db3354de2294.jpg", description="Raw herring served with onions and pickles", restaurant_recommendation="Stubbe's Haring", city_id=6))
    foods.append(Food(name="Bitterballen", image="https://i.pinimg.com/564x/c0/ae/80/c0ae8041ac58643841abe496154d670e.jpg", description="Deep-fried meatballs with a crispy crust", restaurant_recommendation="Café De Doffer", city_id=6))

    # Vienna
    foods.append(Food(name="Wiener Schnitzel", image="https://i.pinimg.com/564x/65/6c/aa/656caa0cbf45fa100fa35b4edb6ca734.jpg", description="Breaded and fried veal cutlet", restaurant_recommendation="Figlmüller", city_id=7))
    foods.append(Food(name="Sachertorte", image="https://i.pinimg.com/564x/10/79/5e/10795e434f329c0b1404c51133eab8fc.jpg", description="Classic Viennese chocolate cake", restaurant_recommendation="Hotel Sacher", city_id=7))
    foods.append(Food(name="Apfelstrudel", image="https://i.pinimg.com/564x/5e/f2/4d/5ef24d05eac60d2a41f304b532fe805e.jpg", description="Apple strudel with flaky pastry and cinnamon", restaurant_recommendation="Café Landtmann", city_id=7))

    # Athens
    foods.append(Food(name="Moussaka", image="https://i.pinimg.com/564x/22/d5/61/22d561d69b5e142aeca8005f1e83e7b9.jpg", description="Layered dish with eggplant, minced meat, and béchamel sauce", restaurant_recommendation="Taverna To Trigono", city_id=8))
    foods.append(Food(name="Souvlaki", image="https://i.pinimg.com/564x/3c/ca/5b/3cca5b0027e7236a869662ede4948401.jpg", description="Grilled skewers of meat, usually served with pita bread", restaurant_recommendation="Bairaktaris", city_id=8))
    foods.append(Food(name="Greek Salad", image="https://i.pinimg.com/564x/9d/04/0b/9d040b5ac81dd6029e8dcbcc2f4dfa6a.jpg", description="Refreshing salad with tomatoes, cucumbers, feta cheese, and olives", restaurant_recommendation="Ta Karamanlidika Tou Fani", city_id=8))

    # Dublin
    foods.append(Food(name="Irish Stew", image="https://i.pinimg.com/564x/c4/47/b5/c447b5a5e68d2dfcabd4dfc77246d7a2.jpg", description="Hearty lamb and vegetable stew", restaurant_recommendation="The Brazen Head", city_id=9))
    foods.append(Food(name="Fish and Chips", image="https://i.pinimg.com/564x/96/d9/cb/96d9cbfb721e6aef044ce4b2eb9b1b61.jpg", description="Classic Irish dish with battered fish and fries", restaurant_recommendation="Leo Burdock", city_id=9))
    foods.append(Food(name="Guinness Pie", image="https://static01.nyt.com/images/2019/03/05/dining/ss-guinness-pie/merlin_150673182_afa6f84f-5993-4f0c-b53c-2ac0b44d01f6-master768.jpg?w=1280&q=75", description="Meat pie made with Guinness stout", restaurant_recommendation="The Pie Shop", city_id=9))

    # Stockholm
    foods.append(Food(name="Swedish Meatballs", image="https://i.pinimg.com/564x/f5/9c/a7/f59ca71a9baba6f0d0b8c56c31890c0f.jpg", description="Small seasoned meatballs served with lingonberry sauce", restaurant_recommendation="Pelikan", city_id=10))
    foods.append(Food(name="Gravlax", image="https://i.pinimg.com/564x/2f/0b/ed/2f0bed53799df0b4b5334290643caf71.jpg", description="Cured salmon with dill and spices", restaurant_recommendation="Södra Teatern", city_id=10))
    foods.append(Food(name="Princess Cake", image="https://i.pinimg.com/564x/0d/bf/7d/0dbf7d0d250a3d11bc02ca45fd69f25f.jpg", description="Layered cake with sponge, cream, and marzipan", restaurant_recommendation="Vete-Katten", city_id=10))

    # Budapest
    foods.append(Food(name="Goulash", image="https://www.fromachefskitchen.com/wp-content/uploads/2022/10/Traditional-Hungarian-Goulash-Recipe-16.jpeg", description="Hearty Hungarian stew with meat and vegetables", restaurant_recommendation="Kádár Étkezde", city_id=11))
    foods.append(Food(name="Langos", image="https://i.pinimg.com/564x/d3/4a/61/d34a61bf2889dbf0bf59368fc9f9bba2.jpg", description="Deep-fried dough topped with various savory or sweet toppings", restaurant_recommendation="Retro Büfé", city_id=11))
    foods.append(Food(name="Dobos Torte", image="https://i.pinimg.com/564x/75/df/89/75df8943632cc48e5c22d2d02d94f5a4.jpg", description="Layered sponge cake with chocolate buttercream and caramel", restaurant_recommendation="Gerbeaud", city_id=11))

    # Tokyo
    foods.append(Food(name="Sushi", image="https://i.pinimg.com/564x/61/76/c0/6176c0bd4c443e8534c9a219b0b4404d.jpg", description="Fresh and delicious sushi rolls", restaurant_recommendation="Sukiyabashi Jiro", city_id=12))
    foods.append(Food(name="Ramen", image="https://i.pinimg.com/564x/81/d3/f2/81d3f2565fdde1e5185e4193c9622290.jpg", description="Hearty and flavorful noodle soup", restaurant_recommendation="Ichiran", city_id=12))
    foods.append(Food(name="Tempura", image="https://i.pinimg.com/564x/39/76/75/397675e2d50c1f71d729c9e60091e34c.jpg", description="Lightly battered and deep-fried seafood and vegetables", restaurant_recommendation="Tenya", city_id=12))

    # Seoul
    foods.append(Food(name="Bibimbap", image="https://i.pinimg.com/564x/62/c2/77/62c27779283b93cecc33722bed632d7f.jpg", description="Mixed rice bowl with assorted vegetables and meat", restaurant_recommendation="Gogung", city_id=13))
    foods.append(Food(name="Kimchi", image="https://i.pinimg.com/564x/ff/f7/26/fff726eeb28d8f00f7759a994fb298ad.jpg", description="Fermented cabbage with spicy and tangy flavors", restaurant_recommendation="Gwangjang Market", city_id=13))
    foods.append(Food(name="Korean BBQ", image="https://i.pinimg.com/564x/70/9e/43/709e43d24978438610df8b1a35db066f.jpg", description="Grilled meat, often served with lettuce wraps and side dishes", restaurant_recommendation="Mapo Galmaegi", city_id=13))

    # Shanghai
    foods.append(Food(name="Xiaolongbao", image="https://i.pinimg.com/564x/45/36/fe/4536fec74c44dbf146a6567aaab244b8.jpg", description="Steamed soup-filled dumplings", restaurant_recommendation="Jia Jia Tang Bao", city_id=14))
    foods.append(Food(name="Shengjianbao", image="https://i.pinimg.com/564x/bd/1e/56/bd1e569333ea36063e350abbde4d17e5.jpg", description="Pan-fried pork dumplings with juicy filling", restaurant_recommendation="Yang's Fry-Dumpling", city_id=14))
    foods.append(Food(name="Braised Pork Belly", image="https://i.pinimg.com/564x/62/06/7f/62067fa0b6a4437f0c780a2511dd1f82.jpg", description="Tender and flavorful braised pork belly slices", restaurant_recommendation="Lao Zhengxing", city_id=14))

    # Singapore
    foods.append(Food(name="Hainanese Chicken Rice", image="https://i.pinimg.com/564x/b2/71/63/b27163361ba2d3982fb78d6610ddb4b5.jpg", description="Poached chicken served with fragrant rice and dipping sauces", restaurant_recommendation="Tian Tian Hainanese Chicken Rice", city_id=15))
    foods.append(Food(name="Chili Crab", image="https://i.pinimg.com/564x/a0/15/77/a015779da0d5cb06ffb519be9d181307.jpg", description="Crab cooked in spicy and tangy tomato-based sauce", restaurant_recommendation="Long Beach Seafood", city_id=15))
    foods.append(Food(name="Laksa", image="https://i.pinimg.com/564x/7c/96/8e/7c968e5490bb96ca4f833dd17138b6ce.jpg", description="Spicy noodle soup with coconut milk and seafood", restaurant_recommendation="328 Katong Laksa", city_id=15))

    # Dubai
    foods.append(Food(name="Shawarma", image="https://i.pinimg.com/564x/97/9c/e5/979ce5b2b5d72053234285d83b05daa8.jpg", description="Grilled meat, usually served in a wrap with vegetables and sauces", restaurant_recommendation="Al Mallah", city_id=16))
    foods.append(Food(name="Mandi", image="https://i.pinimg.com/564x/a4/dc/fc/a4dcfc087eec68cd67c46e5689df33a5.jpg", description="Fragrant rice and tender meat cooked in a traditional oven", restaurant_recommendation="Arabian Tea House", city_id=16))
    foods.append(Food(name="Kunafa", image="https://i.pinimg.com/564x/d0/98/fe/d098fea707fb1ef5d88c0b45c1a082ff.jpg", description="Sweet pastry made with cheese, syrup, and crunchy vermicelli", restaurant_recommendation="Feras Aldiyafa Sweets", city_id=16))

    # Mumbai
    foods.append(Food(name="Vada Pav", image="https://i.pinimg.com/564x/5a/b7/f5/5ab7f5406953dbc82ccdb68d8c0feea5.jpg", description="Spicy potato fritters served in a bun", restaurant_recommendation="Ashok Vada Pav", city_id=17))
    foods.append(Food(name="Butter Chicken", image="hhttps://i.pinimg.com/564x/d1/ac/a5/d1aca5bb93bb89190cd30a8d3146d46f.jpg", description="Creamy and flavorful chicken curry", restaurant_recommendation="Punjab Grill", city_id=17))
    foods.append(Food(name="Pav Bhaji", image="https://i.pinimg.com/564x/77/ee/f4/77eef452e03beecbe21be39f2d2b28a9.jpg", description="Mixed vegetable curry served with buttered buns", restaurant_recommendation="Sardar Refreshments", city_id=17))


    # Hong Kong
    foods.append(Food(name="Dim Sum", image="https://i.pinimg.com/564x/a9/c1/d6/a9c1d6796a6c28d1a0b83107247e2350.jpg", description="Assortment of bite-sized steamed or fried dumplings", restaurant_recommendation="Tim Ho Wan", city_id=18))
    foods.append(Food(name="Roast Goose", image="https://i.pinimg.com/564x/59/61/04/59610493bed83c561429557d049ffb50.jpg", description="Crispy and succulent roasted goose", restaurant_recommendation="Yat Lok Restaurant", city_id=18))
    foods.append(Food(name="Egg Waffles", image="https://i.pinimg.com/564x/1a/6a/32/1a6a326a246b38d6e60c8e763a572999.jpg", description="Sweet and fluffy waffles with a unique egg-shaped pattern", restaurant_recommendation="Lee Keung Kee North Point Egg Waffles", city_id=18))

    # Bangkok
    foods.append(Food(name="Pad Thai", image="https://i.pinimg.com/564x/d2/cf/44/d2cf444a620fc4fa65de2b504787fffb.jpg", description="Thai stir-fried noodles with peanuts and lime", restaurant_recommendation="Thip Samai", city_id=19))
    foods.append(Food(name="Green Curry", image="https://i.pinimg.com/564x/0f/bb/77/0fbb772dcabe3595686ec2fc6e18241d.jpg", description="Spicy and aromatic Thai curry with green chilies and coconut milk", restaurant_recommendation="Krua Apsorn", city_id=19))
    foods.append(Food(name="Mango Sticky Rice", image="https://i.pinimg.com/564x/e0/cb/55/e0cb5517ea75b9ead82b68d8287e197c.jpg", description="Sweet and creamy dessert made with ripe mangoes and sticky rice", restaurant_recommendation="Mae Varee Fruit Shop", city_id=19))

    # Tel Aviv
    foods.append(Food(name="Falafel", image="https://media.timeout.com/images/105106289/1920/1080/image.jpg", description="Deep-fried chickpea patties served in a pita with salad and tahini", restaurant_recommendation="Hakosem", city_id=20))
    foods.append(Food(name="Shakshuka", image="https://i.pinimg.com/564x/f4/85/5b/f4855b0160cdab3a1eb4562a434b0df5.jpg", description="Eggs poached in a spiced tomato sauce, often with peppers and onions", restaurant_recommendation="Dr. Shakshuka", city_id=20))
    foods.append(Food(name="Sabich", image="https://i.pinimg.com/564x/33/e6/7e/33e67e43b849feab4494aa149ce44205.jpg", description="Pita sandwich with fried eggplant, hard-boiled eggs, and various toppings", restaurant_recommendation="Oved Sabich", city_id=20))

    # Cape Town
    foods.append(Food(name="Biltong", image="https://example.com/biltong.jpg", description="Dried and cured South African meat snack", restaurant_recommendation="Carnivore", city_id=21))
    foods.append(Food(name="Bobotie", image="https://example.com/bobotie.jpg", description="Traditional South African dish with spiced minced meat and baked egg-based topping", restaurant_recommendation="Gold Restaurant", city_id=21))
    foods.append(Food(name="Malva Pudding", image="https://example.com/malvapudding.jpg", description="Sweet and sticky baked sponge pudding with apricot jam", restaurant_recommendation="Die Kombuis", city_id=21))

    # Marrakech
    foods.append(Food(name="Tagine", image="https://example.com/tagine.jpg", description="Slow-cooked savory stew with meat and vegetables", restaurant_recommendation="Al Fassia", city_id=22))
    foods.append(Food(name="Couscous", image="https://example.com/couscous.jpg", description="Traditional Moroccan dish with steamed semolina and vegetables", restaurant_recommendation="Nomad", city_id=22))
    foods.append(Food(name="Mint Tea", image="https://example.com/minttea.jpg", description="Refreshing and aromatic Moroccan tea", restaurant_recommendation="Café des Épices", city_id=22))

    # Nairobi
    foods.append(Food(name="Ugali and Sukuma Wiki", image="https://example.com/ugali.jpg", description="Kenyan staple made with maize flour served with collard greens", restaurant_recommendation="Mama Oliech", city_id=23))
    foods.append(Food(name="Nyama Choma", image="https://example.com/nyamachoma.jpg", description="Grilled meat, often goat or beef, served with side dishes", restaurant_recommendation="Carnivore", city_id=23))
    foods.append(Food(name="Mandazi", image="https://example.com/mandazi.jpg", description="Sweet fried dough similar to donuts or beignets", restaurant_recommendation="Junction Mall Mandazi Stand", city_id=23))

    # Cairo
    foods.append(Food(name="Koshari", image="https://example.com/koshari.jpg", description="Egyptian comfort food with rice, lentils, pasta, and a spiced tomato sauce", restaurant_recommendation="Abou Tarek", city_id=27))
    foods.append(Food(name="Ful Medames", image="https://example.com/fulmedames.jpg", description="Stewed fava beans served with toppings and bread", restaurant_recommendation="Felfela", city_id=27))
    foods.append(Food(name="Kofta", image="https://example.com/kofta.jpg", description="Grilled or baked ground meat skewers, often served with rice or bread", restaurant_recommendation="Kebdet El Prince", city_id=27))

    # Victoria Falls
    foods.append(Food(name="Bream Fish", image="https://example.com/breamfish.jpg", description="Freshwater fish commonly found in the Zambezi River, usually grilled or fried", restaurant_recommendation="The Boma - Dinner & Drum Show", city_id=28))
    foods.append(Food(name="Sadza", image="https://example.com/sadza.jpg", description="Staple food made from finely ground cornmeal, similar to polenta", restaurant_recommendation="Mama Africa Eating House", city_id=28))
    foods.append(Food(name="Game Meat", image="https://example.com/gamemeat.jpg", description="Various types of wild game meat, such as kudu or warthog, often prepared as steaks or stews", restaurant_recommendation="The Smoke that Thunders", city_id=28))

    # Zanzibar City
    foods.append(Food(name="Zanzibar Pizza", image="https://example.com/zanzibarpizza.jpg", description="Thin and crispy stuffed pancakes with various fillings like seafood, meat, or vegetables", restaurant_recommendation="Forodhani Night Market", city_id=29))
    foods.append(Food(name="Octopus Curry", image="https://example.com/octopuscurry.jpg", description="Spicy curry dish made with tender octopus and flavorful spices", restaurant_recommendation="Café Miwa", city_id=29))
    foods.append(Food(name="Urojo Soup", image="https://example.com/urojosoup.jpg", description="Tangy and savory soup with a mix of ingredients like potatoes, lentils, and fried snacks", restaurant_recommendation="Zanzibar Delights", city_id=29))

    # Cape Coast
    foods.append(Food(name="Fante Kenkey", image="https://example.com/fantekenkey.jpg", description="Fermented corn dumplings wrapped in banana leaves, served with fish or meat", restaurant_recommendation="Hansa Kenkey House", city_id=30))
    foods.append(Food(name="Grilled Lobster", image="https://example.com/grilledlobster.jpg", description="Freshly caught lobster grilled to perfection, often served with spicy sauces", restaurant_recommendation="Biriwa Beach Hotel", city_id=30))
    foods.append(Food(name="Cape Coast Soup", image="https://example.com/capecoastsoup.jpg", description="Hearty soup with a mix of seafood, vegetables, and spices", restaurant_recommendation="Brenu Beach Lodge", city_id=30))

    # Dakar
    foods.append(Food(name="Thieboudienne", image="https://example.com/thieboudienne.jpg", description="National dish of Senegal, a flavorful rice and fish stew with vegetables", restaurant_recommendation="Chez Loutcha", city_id=31))
    foods.append(Food(name="Yassa Poulet", image="https://example.com/yassapoulet.jpg", description="Chicken marinated in tangy onion and lemon sauce, often served with rice", restaurant_recommendation="La Calebasse", city_id=31))
    foods.append(Food(name="Mafe", image="https://example.com/mafe.jpg", description="Peanut butter stew with meat or vegetables, served with couscous or rice", restaurant_recommendation="Chez Fatou", city_id=31))

    # Johannesburg
    foods.append(Food(name="Braai", image="https://example.com/braai.jpg", description="South African barbecue featuring grilled meat, sausages, and vegetables", restaurant_recommendation="Mzoli's", city_id=32))
    foods.append(Food(name="Bunny Chow", image="https://example.com/bunnychow.jpg", description="Hollowed-out loaf of bread filled with curry, a popular street food", restaurant_recommendation="House of Nsangu", city_id=32))
    foods.append(Food(name="Malva Pudding", image="https://example.com/malvapudding.jpg", description="Sweet and sticky baked sponge pudding with apricot jam, often served with custard", restaurant_recommendation="Sophiatown Bar Lounge", city_id=32))

    # Luxor
    foods.append(Food(name="Koshari", image="https://example.com/koshari.jpg", description="Egyptian comfort food with rice, lentils, pasta, and a spiced tomato sauce", restaurant_recommendation="Abou Shakra", city_id=33))
    foods.append(Food(name="Ful Medames", image="https://example.com/fulmedames.jpg", description="Stewed fava beans served with toppings and bread", restaurant_recommendation="Hoda Restaurant", city_id=33))
    foods.append(Food(name="Taameya", image="https://example.com/taameya.jpg", description="Egyptian falafel made from mashed fava beans or chickpeas", restaurant_recommendation="El Hussein", city_id=33))

    # Sydney
    foods.append(Food(name="Fish and Chips", image="https://example.com/fishandchips.jpg", description="Classic dish of battered fish and crispy fries", restaurant_recommendation="Sydney Fish Market", city_id=34))
    foods.append(Food(name="Meat Pie", image="https://example.com/meatpie.jpg", description="Savory pie filled with minced meat and gravy", restaurant_recommendation="Harry's Cafe de Wheels", city_id=34))
    foods.append(Food(name="Pavlova", image="https://example.com/pavlova.jpg", description="Dessert made of meringue, whipped cream, and fresh fruits", restaurant_recommendation="Black Star Pastry", city_id=34))

    # Auckland
    foods.append(Food(name="Hangi", image="https://example.com/hangi.jpg", description="Traditional Maori dish of meat and vegetables cooked in an earth oven", restaurant_recommendation="Hangi Master", city_id=35))
    foods.append(Food(name="Pork Belly", image="https://example.com/porkbelly.jpg", description="Slow-cooked pork belly with crispy crackling, often served with roasted vegetables", restaurant_recommendation="The Grove", city_id=35))
    foods.append(Food(name="Pavlova", image="https://example.com/pavlova.jpg", description="Dessert made of meringue, whipped cream, and fresh fruits", restaurant_recommendation="Moustache Milk & Cookie Bar", city_id=35))

    # Melbourne
    foods.append(Food(name="Chicken Parmigiana", image="https://example.com/chickenparmigiana.jpg", description="Breaded chicken cutlet topped with tomato sauce and melted cheese, served with fries or salad", restaurant_recommendation="The Pub", city_id=36))
    foods.append(Food(name="Lamb Roast", image="https://example.com/lambroast.jpg", description="Slow-roasted lamb with herbs and spices, often served with roasted vegetables and gravy", restaurant_recommendation="The Meat & Wine Co", city_id=36))
    foods.append(Food(name="Vanilla Slice", image="https://example.com/vanillaslice.jpg", description="Pastry dessert with layers of custard and puff pastry, topped with icing", restaurant_recommendation="Bourke Street Bakery", city_id=36))

    # Queenstown
    foods.append(Food(name="Fergburger", image="https://example.com/fergburger.jpg", description="Iconic burger filled with a variety of toppings and sauces", restaurant_recommendation="Fergburger", city_id=37))
    foods.append(Food(name="Venison", image="https://example.com/venison.jpg", description="Tender and flavorful deer meat, often served as steaks or in stews", restaurant_recommendation="Rata Dining", city_id=37))
    foods.append(Food(name="Hokey Pokey Ice Cream", image="https://example.com/hokeypokey.jpg", description="New Zealand's classic ice cream flavor with caramelized honeycomb toffee pieces", restaurant_recommendation="Patagonia Chocolates", city_id=37))

    # Brisbane
    foods.append(Food(name="Barramundi", image="https://example.com/barramundi.jpg", description="Popular Australian fish known for its sweet and buttery flavor, often grilled or fried", restaurant_recommendation="The Fish House", city_id=38))
    foods.append(Food(name="Prawn Cocktail", image="https://example.com/prawncocktail.jpg", description="Chilled prawns served with a tangy cocktail sauce and lettuce", restaurant_recommendation="Cha Cha Char Wine Bar & Grill", city_id=38))
    foods.append(Food(name="Tim Tam", image="https://example.com/timtam.jpg", description="Chocolate-coated biscuit with a creamy filling, a beloved Australian treat", restaurant_recommendation="Woolworths", city_id=38))

    # Honolulu
    foods.append(Food(name="Poke Bowl", image="https://example.com/pokebowl.jpg", description="Hawaiian dish with diced raw fish, rice, and various toppings", restaurant_recommendation="Ono Seafood", city_id=39))
    foods.append(Food(name="Kalua Pig", image="https://example.com/kaluapig.jpg", description="Slow-roasted pig cooked in an underground oven, a traditional Hawaiian luau dish", restaurant_recommendation="Kono's North Shore", city_id=39))
    foods.append(Food(name="Shave Ice", image="https://example.com/shaveice.jpg", description="Flavored shaved ice topped with syrup and various toppings, a refreshing treat", restaurant_recommendation="Matsumoto Shave Ice", city_id=39))

    # Fiji
    foods.append(Food(name="Lovo", image="https://example.com/lovo.jpg", description="Traditional Fijian feast cooked in an underground oven, featuring meats, fish, and vegetables", restaurant_recommendation="Namosi Highland Picnic", city_id=40))
    foods.append(Food(name="Kokoda", image="https://example.com/kokoda.jpg", description="Fijian ceviche made with raw fish marinated in coconut milk and citrus juices", restaurant_recommendation="Indigo Indian Asian Restaurant", city_id=40))
    foods.append(Food(name="Cassava Cake", image="https://example.com/cassavacake.jpg", description="Dessert made from grated cassava, coconut milk, and sugar, often served with coconut cream", restaurant_recommendation="Nadina Authentic Fijian Restaurant", city_id=40))

    # Suva
    foods.append(Food(name="Palusami", image="https://example.com/palusami.jpg", description="Taro leaves filled with coconut cream and onions, cooked in an underground oven", restaurant_recommendation="Daikoku Fiji", city_id=41))
    foods.append(Food(name="Kokoda", image="https://example.com/kokoda.jpg", description="Fijian ceviche made with raw fish marinated in coconut milk and citrus juices", restaurant_recommendation="Rewa Café", city_id=41))
    foods.append(Food(name="Fried Rice", image="https://example.com/friedrice.jpg", description="Stir-fried rice with vegetables, meat, and/or seafood, a popular Chinese-inspired dish", restaurant_recommendation="Tai's Place", city_id=41))

    # Wellington
    foods.append(Food(name="Hangi Pie", image="https://example.com/hangipie.jpg", description="Meat and vegetable pie with flavors inspired by traditional Maori hangi", restaurant_recommendation="The British Pie Shop", city_id=43))
    foods.append(Food(name="Whitebait Fritter", image="https://example.com/whitebaitfritter.jpg", description="Egg-battered fritter filled with tiny whitebait fish, a classic New Zealand delicacy", restaurant_recommendation="Maranui Café", city_id=43))
    foods.append(Food(name="Kiwifruit Pavlova", image="https://example.com/kiwifruitpavlova.jpg", description="Pavlova dessert topped with slices of kiwifruit, a popular New Zealand fruit", restaurant_recommendation="Sweet Bakery and Cakery", city_id=43))

    # Canberra
    foods.append(Food(name="Barramundi", image="https://example.com/barramundi.jpg", description="Popular Australian fish known for its sweet and buttery flavor, often grilled or fried", restaurant_recommendation="Pialligo Estate", city_id=44))
    foods.append(Food(name="Australian Meat Pie", image="https://example.com/meatpie.jpg", description="Individual-sized savory pie filled with minced meat and gravy, a classic Australian snack", restaurant_recommendation="Gus' Cafe", city_id=44))
    foods.append(Food(name="Lamington", image="https://example.com/lamington.jpg", description="Sponge cake coated in chocolate icing and desiccated coconut, a beloved Australian treat", restaurant_recommendation="Dobinsons Bakery Cafe", city_id=44))

    # New York City
    foods.append(Food(name="New York-style Pizza", image="https://example.com/pizza.jpg", description="Large, thin-crust pizza with classic toppings like cheese, pepperoni, and tomato sauce", restaurant_recommendation="Joe's Pizza", city_id=45))
    foods.append(Food(name="Pastrami Sandwich", image="https://example.com/pastramisandwich.jpg", description="Hearty sandwich filled with thinly sliced, smoky pastrami, usually served on rye bread with mustard", restaurant_recommendation="Katz's Delicatessen", city_id=45))
    foods.append(Food(name="Cheesecake", image="https://example.com/cheesecake.jpg", description="Rich and creamy dessert made with cream cheese, eggs, and a graham cracker crust", restaurant_recommendation="Junior's", city_id=45))

    # Los Angeles
    foods.append(Food(name="Taco", image="https://example.com/taco.jpg", description="Mexican street food staple consisting of a tortilla filled with various ingredients like grilled meat, salsa, and guacamole", restaurant_recommendation="Guisados", city_id=46))
    foods.append(Food(name="Korean BBQ", image="https://example.com/koreanbbq.jpg", description="Grilled marinated meats, typically beef, served with rice, kimchi, and other side dishes", restaurant_recommendation="Park's BBQ", city_id=46))
    foods.append(Food(name="Acai Bowl", image="https://example.com/acai.jpg", description="Healthy breakfast bowl made with acai berries, topped with granola, fruits, and honey", restaurant_recommendation="Backyard Bowls", city_id=46))

    # Toronto
    foods.append(Food(name="Peameal Bacon Sandwich", image="https://example.com/peamealbacon.jpg", description="Sandwich made with peameal bacon, a type of Canadian bacon, often served on a bun with mustard", restaurant_recommendation="Carousel Bakery", city_id=47))
    foods.append(Food(name="Poutine", image="https://example.com/poutine.jpg", description="Classic Canadian dish of french fries topped with cheese curds and smothered in gravy", restaurant_recommendation="Smoke's Poutinerie", city_id=47))
    foods.append(Food(name="Butter Tart", image="https://example.com/buttertart.jpg", description="Sweet pastry tart filled with a gooey mixture of butter, sugar, and eggs", restaurant_recommendation="Le Gourmand", city_id=47))

    # Mexico City
    foods.append(Food(name="Tacos al Pastor", image="https://example.com/tacosalpastor.jpg", description="Marinated pork tacos topped with pineapple, onion, and cilantro", restaurant_recommendation="El Huequito", city_id=48))
    foods.append(Food(name="Chiles en Nogada", image="https://example.com/chilesennogada.jpg", description="Stuffed poblano peppers topped with walnut sauce and pomegranate seeds, a traditional Mexican dish", restaurant_recommendation="El Cardenal", city_id=48))
    foods.append(Food(name="Mexican Street Corn (Elote)", image="https://example.com/elote.jpg", description="Grilled corn on the cob coated with mayo, cheese, chili powder, and lime juice", restaurant_recommendation="Elote Man", city_id=48))

    # Vancouver
    foods.append(Food(name="Salmon Sushi", image="https://example.com/salmonsushi.jpg", description="Fresh salmon sashimi or nigiri sushi, a popular seafood delicacy in Vancouver", restaurant_recommendation="Miku", city_id=49))
    foods.append(Food(name="Japadog", image="https://example.com/japadog.jpg", description="Japanese-style hot dog topped with unique toppings like teriyaki sauce, seaweed, and Japanese mayo", restaurant_recommendation="Japadog", city_id=49))
    foods.append(Food(name="Nanaimo Bar", image="https://example.com/nanaimobar.jpg", description="Layered dessert bar with a chocolate-coconut base, custard filling, and chocolate ganache on top", restaurant_recommendation="Butter Baked Goods", city_id=49))

    # San Francisco
    foods.append(Food(name="Cioppino", image="https://example.com/cioppino.jpg", description="Seafood stew made with a variety of fish and shellfish, usually served with crusty bread", restaurant_recommendation="Tadich Grill", city_id=50))
    foods.append(Food(name="Mission Burrito", image="https://example.com/burrito.jpg", description="Large, overstuffed burrito filled with ingredients like rice, beans, meat, salsa, and guacamole", restaurant_recommendation="La Taqueria", city_id=50))
    foods.append(Food(name="Sourdough Bread", image="https://example.com/sourdoughbread.jpg", description="Tangy and crusty bread made from naturally fermented dough, a San Francisco specialty", restaurant_recommendation="Boudin Bakery", city_id=50))

    # Chicago
    foods.append(Food(name="Deep Dish Pizza", image="https://example.com/deepdishpizza.jpg", description="Thick, deep-dish pizza with a buttery crust, gooey cheese, and chunky tomato sauce", restaurant_recommendation="Lou Malnati's Pizzeria", city_id=51))
    foods.append(Food(name="Chicago-style Hot Dog", image="https://example.com/chicagohotdog.jpg", description="All-beef hot dog topped with mustard, onions, relish, tomato slices, pickle spear, sport peppers, and celery salt, served on a poppy seed bun", restaurant_recommendation="Portillo's", city_id=51))
    foods.append(Food(name="Italian Beef Sandwich", image="https://example.com/italianbeef.jpg", description="Thinly sliced roast beef piled on a crusty roll and dipped in flavorful gravy, a Chicago classic", restaurant_recommendation="Al's Beef", city_id=51))

    # Miami
    foods.append(Food(name="Cuban Sandwich", image="https://example.com/cubansandwich.jpg", description="Grilled sandwich with ham, roasted pork, Swiss cheese, pickles, and mustard, pressed on Cuban bread", restaurant_recommendation="Versailles Restaurant", city_id=52))
    foods.append(Food(name="Key Lime Pie", image="https://example.com/keylimepie.jpg", description="Tangy and creamy pie made with key lime juice and a graham cracker crust", restaurant_recommendation="Joe's Stone Crab", city_id=52))
    foods.append(Food(name="Stone Crab", image="https://example.com/stonecrab.jpg", description="Freshly caught stone crab claws served chilled with mustard sauce, a popular seafood delicacy in Miami", restaurant_recommendation="Joe's Stone Crab", city_id=52))

    # Montreal
    foods.append(Food(name="Poutine", image="https://example.com/poutine.jpg", description="Classic Canadian dish of french fries topped with cheese curds and smothered in gravy", restaurant_recommendation="La Banquise", city_id=53))
    foods.append(Food(name="Smoked Meat Sandwich", image="https://example.com/smokedmeat.jpg", description="Sandwich made with flavorful smoked meat, typically served on rye bread with mustard", restaurant_recommendation="Schwartz's Deli", city_id=53))
    foods.append(Food(name="Bagels", image="https://example.com/montrealbagels.jpg", description="Chewy and slightly sweet bagels, often topped with sesame seeds and served with cream cheese and smoked salmon", restaurant_recommendation="Fairmount Bagel", city_id=53))

    # Seattle
    foods.append(Food(name="Seattle-style Hot Dog", image="https://example.com/seattlehotdog.jpg", description="Hot dog topped with cream cheese, grilled onions, and sautéed onions, a unique Seattle twist", restaurant_recommendation="Monster Dogs", city_id=54))
    foods.append(Food(name="Salmon Chowder", image="https://example.com/salmonchowder.jpg", description="Creamy chowder made with fresh salmon, potatoes, and vegetables, a Pacific Northwest specialty", restaurant_recommendation="Pike Place Chowder", city_id=54))
    foods.append(Food(name="Dungeness Crab", image="https://example.com/dungenesscrab.jpg", description="Sweet and flavorful crab, often served steamed or in various seafood dishes, a local delicacy in Seattle", restaurant_recommendation="The Crab Pot", city_id=54))

    # Rio de Janeiro
    foods.append(Food(name="Feijoada", image="https://example.com/feijoada.jpg", description="Rich and hearty black bean stew with various cuts of pork and served with rice, collard greens, and farofa", restaurant_recommendation="Casa da Feijoada", city_id=55))
    foods.append(Food(name="Coxinha", image="https://example.com/coxinha.jpg", description="Deep-fried dough filled with shredded chicken and cream cheese, a popular Brazilian snack", restaurant_recommendation="Bar do Mineiro", city_id=55))
    foods.append(Food(name="Caipirinha", image="https://example.com/caipirinha.jpg", description="Refreshing cocktail made with cachaça, sugar, and lime, Brazil's national drink", restaurant_recommendation="Jobi", city_id=55))

    # Buenos Aires
    foods.append(Food(name="Asado", image="https://example.com/asado.jpg", description="Argentine-style barbecue with various cuts of grilled meat, often served with chimichurri sauce", restaurant_recommendation="La Brigada", city_id=56))
    foods.append(Food(name="Empanadas", image="https://example.com/empanadas.jpg", description="Savory pastries filled with meat, cheese, or vegetables, a popular street food in Argentina", restaurant_recommendation="El Sanjuanino", city_id=56))
    foods.append(Food(name="Milanesa", image="https://example.com/milanesa.jpg", description="Breaded and fried meat cutlets, typically made with beef or chicken, served with mashed potatoes or salad", restaurant_recommendation="El Preferido de Palermo", city_id=56))

    # Sao Paulo
    foods.append(Food(name="Pastel", image="https://example.com/pastel.jpg", description="Deep-fried pastry filled with various savory fillings, such as cheese, meat, or heart of palm", restaurant_recommendation="Feira da Liberdade", city_id=57))
    foods.append(Food(name="Virado à Paulista", image="https://example.com/virado.jpg", description="Traditional dish consisting of beans, rice, pork chops, sausage, collard greens, and a fried egg, a classic meal in Sao Paulo", restaurant_recommendation="Bar do Biu", city_id=57))
    foods.append(Food(name="Coxinha de Frango", image="https://example.com/coxinhadefrango.jpg", description="Chicken croquette with a dough filled with shredded chicken, shaped like a drumstick", restaurant_recommendation="Veloso", city_id=57))

    # Lima
    foods.append(Food(name="Ceviche", image="https://example.com/ceviche.jpg", description="Fresh raw fish marinated in citrus juice, typically seasoned with onions, chili peppers, and cilantro", restaurant_recommendation="La Mar", city_id=58))
    foods.append(Food(name="Lomo Saltado", image="https://example.com/lomosaltado.jpg", description="Stir-fried beef with onions, tomatoes, and french fries, often served with rice", restaurant_recommendation="Tanta", city_id=58))
    foods.append(Food(name="Anticuchos", image="https://example.com/anticuchos.jpg", description="Grilled skewers of marinated meat, usually beef heart, served with potatoes and corn", restaurant_recommendation="Panchita", city_id=58))

    # Bogota
    foods.append(Food(name="Ajiaco", image="https://example.com/ajiaco.jpg", description="Hearty soup made with chicken, potatoes, corn, and guascas herb, often served with avocado and capers", restaurant_recommendation="La Puerta Falsa", city_id=59))
    foods.append(Food(name="Bandeja Paisa", image="https://example.com/bandejapaisa.jpg", description="Traditional platter consisting of rice, beans, grilled steak, chorizo, fried pork belly, plantains, arepa, avocado, and a fried egg", restaurant_recommendation="Andres Carne de Res", city_id=59))
    foods.append(Food(name="Arepa", image="https://example.com/arepa.jpg", description="Cornmeal patty served with various fillings, such as cheese, meat, or eggs, a staple food in Colombia", restaurant_recommendation="La Puerta Falsa", city_id=59))

    # Santiago
    foods.append(Food(name="Completo", image="https://example.com/completo.jpg", description="Chilean-style hot dog topped with avocado, mayonnaise, sauerkraut, and tomato", restaurant_recommendation="Fuente Alemana", city_id=60))
    foods.append(Food(name="Pastel de Choclo", image="https://example.com/pasteldechoclo.jpg", description="Corn and meat pie topped with sugar, a traditional dish in Chile", restaurant_recommendation="Las Delicias de Quirihue", city_id=60))
    foods.append(Food(name="Cazuela", image="https://example.com/cazuela.jpg", description="Hearty soup made with meat, potatoes, corn, pumpkin, and various vegetables, a popular Chilean comfort food", restaurant_recommendation="El Hoyo", city_id=60))

    # Cartagena
    foods.append(Food(name="Arepas de Huevo", image="https://example.com/arepasdehuevo.jpg", description="Fried cornmeal patties filled with scrambled eggs, a popular snack in Cartagena", restaurant_recommendation="La Cocina de Pepina", city_id=61))
    foods.append(Food(name="Sancocho de Pescado", image="https://example.com/sancocho.jpg", description="Fish stew made with coconut milk, yuca, plantains, and various spices, a traditional dish in Cartagena", restaurant_recommendation="La Mulata", city_id=61))
    foods.append(Food(name="Camarones al Ajillo", image="https://example.com/camaronesalajillo.jpg", description="Garlic shrimp sautéed in olive oil, often served with rice or bread, a popular seafood dish in Cartagena", restaurant_recommendation="La Cevicheria", city_id=61))

    # Quito
    foods.append(Food(name="Locro de Papa", image="https://example.com/locrodepapa.jpg", description="Creamy potato soup with cheese, avocado, and crispy pork skin, a traditional dish in Ecuador", restaurant_recommendation="Cafe Dios No Muere", city_id=63))
    foods.append(Food(name="Cuy", image="https://example.com/cuy.jpg", description="Roasted guinea pig, a unique delicacy in Ecuador", restaurant_recommendation="El Crater", city_id=63))
    foods.append(Food(name="Encebollado", image="https://example.com/encebollado.jpg", description="Fish soup made with albacore tuna, yuca, onions, and spices, often served with pickled onions and avocado slices", restaurant_recommendation="Lo de Carlitos", city_id=63))

    # Salvador
    foods.append(Food(name="Acarajé", image="https://example.com/acaraje.jpg", description="Deep-fried black-eyed pea fritters filled with shrimp, vatapá, and caruru, a popular street food in Bahia", restaurant_recommendation="Dinha Acarajé", city_id=64))
    foods.append(Food(name="Moqueca de Camarão", image="https://example.com/moquecadecamarao.jpg", description="Creamy shrimp stew cooked with coconut milk, palm oil, peppers, onions, and tomatoes, a traditional dish in Bahia", restaurant_recommendation="Restaurante Yemanjá", city_id=64))
    foods.append(Food(name="Acaí na Tigela", image="https://example.com/acai.jpg", description="Frozen acai berry puree topped with granola, banana, and other fruits, a popular Brazilian snack", restaurant_recommendation="Açaí Concept", city_id=64))

    # Lisbon
    foods.append(Food(name="Pastel de Nata", image="https://example.com/pasteldenata.jpg", description="Creamy custard tart with a caramelized top, a famous Portuguese pastry", restaurant_recommendation="Pasteis de Belém", city_id=65))
    foods.append(Food(name="Bacalhau à Brás", image="https://example.com/bacalhauabras.jpg", description="Shredded codfish sautéed with onions, potatoes, eggs, and olives, a classic Portuguese dish", restaurant_recommendation="A Brasileira", city_id=65))
    foods.append(Food(name="Francesinha", image="https://example.com/francesinha.jpg", description="Hearty sandwich with layers of cured meats, melted cheese, and a spicy tomato-based sauce, a specialty of Porto but popular in Lisbon too", restaurant_recommendation="Cervejaria Gazela", city_id=65))


    cities = []
    cities.append(City(name="Istanbul", image="https://www.travelandleisure.com/thmb/UXNrwYTm3z1CAEBl8z_sTxnyGEw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/istanbul-turkey-ISTANBULTG0721-a987bb021e5e4b42b069ba2518cde276.jpg",language="Turkish",description="amazing"))
    cities.append(City(name="Paris", image="https://example.com/paris.jpg", language="French", description="The City of Love"))
    cities.append(City(name="Rome", image="https://example.com/rome.jpg", language="Italian", description="Eternal City"))
    cities.append(City(name="Barcelona", image="https://example.com/barcelona.jpg", language="Spanish", description="Vibrant and Cultural"))
    cities.append(City(name="Prague", image="https://example.com/prague.jpg", language="Czech", description="Fairytale City"))
    cities.append(City(name="Amsterdam", image="https://example.com/amsterdam.jpg", language="Dutch", description="Canals and Bicycles"))
    cities.append(City(name="Vienna", image="https://example.com/vienna.jpg", language="German", description="City of Music"))
    cities.append(City(name="Athens", image="https://example.com/athens.jpg", language="Greek", description="Ancient Capital"))
    cities.append(City(name="Dublin", image="https://example.com/dublin.jpg", language="English", description="Friendly and Lively"))
    cities.append(City(name="Stockholm", image="https://example.com/stockholm.jpg", language="Swedish", description="Scandinavian Gem"))
    cities.append(City(name="Budapest", image="https://example.com/budapest.jpg", language="Hungarian", description="City of Baths"))
    
    
    cities.append(City(name="Tokyo", image="https://example.com/tokyo.jpg", language="Japanese", description="Bustling Metropolis"))
    cities.append(City(name="Seoul", image="https://example.com/seoul.jpg", language="Korean", description="Dynamic and Modern"))
    cities.append(City(name="Shanghai", image="https://example.com/shanghai.jpg", language="Mandarin", description="Global Financial Hub"))
    cities.append(City(name="Singapore", image="https://example.com/singapore.jpg", language="English", description="Clean and Efficient"))
    cities.append(City(name="Dubai", image="https://example.com/dubai.jpg", language="Arabic", description="City of Superlatives"))
    cities.append(City(name="Mumbai", image="https://example.com/mumbai.jpg", language="Hindi", description="Bollywood and Business"))
    cities.append(City(name="Hong Kong", image="https://example.com/hongkong.jpg", language="Cantonese", description="Urban Jungle"))
    cities.append(City(name="Bangkok", image="https://example.com/bangkok.jpg", language="Thai", description="City of Temples"))
    cities.append(City(name="Tel Aviv", image="https://example.com/jerusalem.jpg", language="Hebrew", description="Holy City"))

   
    cities.append(City(name="Cape Town", image="https://example.com/capetown.jpg", language="English", description="Stunning Natural Beauty"))
    cities.append(City(name="Marrakech", image="https://example.com/marrakech.jpg", language="Arabic", description="Exotic and Colorful"))
    cities.append(City(name="Nairobi", image="https://example.com/nairobi.jpg", language="Swahili", description="Gateway to Safari"))
    cities.append(City(name="Cairo", image="https://example.com/cairo.jpg", language="Arabic", description="Pharaonic Wonders"))
    cities.append(City(name="Victoria Falls", image="https://example.com/victoriafalls.jpg", language="English", description="Spectacular Waterfalls"))
    cities.append(City(name="Zanzibar City", image="https://example.com/zanzibar.jpg", language="Swahili", description="Paradise Island"))
    cities.append(City(name="Cape Coast", image="https://example.com/capecoast.jpg", language="English", description="Rich History"))
    cities.append(City(name="Dakar", image="https://example.com/dakar.jpg", language="French", description="Vibrant West African Culture"))
    cities.append(City(name="Johannesburg", image="https://example.com/johannesburg.jpg", language="English", description="Economic Powerhouse"))
    cities.append(City(name="Luxor", image="https://example.com/luxor.jpg", language="Arabic", description="Ancient Egyptian Treasures"))

   
    cities.append(City(name="Sydney", image="https://example.com/sydney.jpg", language="English", description="Iconic Landmarks"))
    cities.append(City(name="Auckland", image="https://example.com/auckland.jpg", language="English", description="City of Sails"))
    cities.append(City(name="Melbourne", image="https://example.com/melbourne.jpg", language="English", description="Cultural Melting Pot"))
    cities.append(City(name="Queenstown", image="https://example.com/queenstown.jpg", language="English", description="Adventure Capital"))
    cities.append(City(name="Brisbane", image="https://example.com/brisbane.jpg", language="English", description="Sunshine City"))
    cities.append(City(name="Honolulu", image="https://example.com/honolulu.jpg", language="English", description="Tropical Paradise"))
    cities.append(City(name="Fiji", image="https://example.com/fiji.jpg", language="English", description="Idyllic Islands"))
    cities.append(City(name="Suva", image="https://example.com/suva.jpg", language="English", description="Cultural Hub"))
    cities.append(City(name="Wellington", image="https://example.com/wellington.jpg", language="English", description="Coolest Little Capital"))
    cities.append(City(name="Canberra", image="https://example.com/canberra.jpg", language="English", description="Seat of Government"))
   

    #north america
    cities.append(City(name="New York City", image="https://example.com/newyork.jpg", language="English", description="The Big Apple"))
    cities.append(City(name="Los Angeles", image="https://example.com/losangeles.jpg", language="English", description="City of Stars"))
    cities.append(City(name="Toronto", image="https://example.com/toronto.jpg", language="English", description="Cultural Diversity"))
    cities.append(City(name="Mexico City", image="https://example.com/mexicocity.jpg", language="Spanish", description="Historic Capital"))
    cities.append(City(name="Vancouver", image="https://example.com/vancouver.jpg", language="English", description="Outdoor Paradise"))
    cities.append(City(name="San Francisco", image="https://example.com/sanfrancisco.jpg", language="English", description="Tech Hub"))
    cities.append(City(name="Chicago", image="https://example.com/chicago.jpg", language="English", description="Windy City"))
    cities.append(City(name="Miami", image="https://example.com/miami.jpg", language="English", description="Sunshine Paradise"))
    cities.append(City(name="Montreal", image="https://example.com/montreal.jpg", language="French", description="European Charm"))
    cities.append(City(name="Seattle", image="https://example.com/seattle.jpg", language="English", description="Emerald City"))

    #south america
    cities.append(City(name="Rio de Janeiro", image="https://example.com/riodejaneiro.jpg", language="Portuguese", description="Carnival City"))
    cities.append(City(name="Buenos Aires", image="https://example.com/buenosaires.jpg", language="Spanish", description="Cosmopolitan Capital"))
    cities.append(City(name="Sao Paulo", image="https://example.com/saopaulo.jpg", language="Portuguese", description="Largest City in South America"))
    cities.append(City(name="Lima", image="https://example.com/lima.jpg", language="Spanish", description="Historic and Culinary Hub"))
    cities.append(City(name="Bogota", image="https://example.com/bogota.jpg", language="Spanish", description="Andean Capital"))
    cities.append(City(name="Santiago", image="https://example.com/santiago.jpg", language="Spanish", description="Modern and Progressive"))
    cities.append(City(name="Cartagena", image="https://example.com/cartagena.jpg", language="Spanish", description="Colonial Gem"))
    cities.append(City(name="Quito", image="https://example.com/quito.jpg", language="Spanish", description="High in the Andes"))
    cities.append(City(name="Salvador", image="https://example.com/salvador.jpg", language="Portuguese", description="Cultural Center"))
    cities.append(City(name="Lisbon", image="https://example.com/lisbon.jpg", language="Portuguese", description="Capital of Portugal, but located in South America"))




    continents = []
    continents.append(Continent(name="Europe",image="https://thumbs.dreamstime.com/z/vector-illustration-political-map-europe-european-continent-four-colors-country-name-labels-vector-illustration-cool-158754686.jpg",belongs="where"))
    continents.append(Continent(name="Asia",image="https://p4.wallpaperbetter.com/wallpaper/108/393/213/high-resolution-images-of-nature-3840x2160-wallpaper-preview.jpg",belongs="where"))
    continents.append(Continent(name="Africa",image="https://www.wallpapers13.com/wp-content/uploads/2019/09/Giraffe-Family-Giraffidae-the-tallest-living-land-animal-and-largest-survivor-Wild-Animals-from-Africa-4K-Ultra-HD-Wallpaper-for-Desktop-Laptop-840x525.jpg",belongs="where"))
    continents.append(Continent(name="Australia and Ocenia", image="https://cdn.britannica.com/66/194766-050-5908DD25/canyon-swell-reef-sunlight-water-surface-Pacific.jpg",belongs="where"))
    continents.append(Continent(name="North America", image="https://wallpapercave.com/dwp2x/wp10946351.jpg",belongs="where"))
    continents.append(Continent(name="South America", image="https://img.theculturetrip.com/1440x807/smart/wp-content/uploads/2021/04/kerkmt-e1618321977695.jpg",belongs="where"))
    


    

    concities = []
    concities.append(Concities(city_id=1, continent_id=1))  # Istanbul - Europe
    concities.append(Concities(city_id=2, continent_id=1))  # Paris - Europe
    concities.append(Concities(city_id=3, continent_id=1))  # Rome - Europe
    concities.append(Concities(city_id=4, continent_id=1))  # Barcelona - Europe
    concities.append(Concities(city_id=5, continent_id=1))  # Prague - Europe
    concities.append(Concities(city_id=6, continent_id=1))  # Amsterdam - Europe
    concities.append(Concities(city_id=7, continent_id=1))  # Vienna - Europe
    concities.append(Concities(city_id=8, continent_id=1))  # Athens - Europe
    concities.append(Concities(city_id=9, continent_id=1))  # Dublin - Europe
    concities.append(Concities(city_id=10, continent_id=1))  # Stockholm - Europe
    concities.append(Concities(city_id=11, continent_id=1))  # Budapest - Europe

    concities.append(Concities(city_id=12, continent_id=2))  # Tokyo - Asia
    concities.append(Concities(city_id=13, continent_id=2))  # Seoul - Asia
    concities.append(Concities(city_id=14, continent_id=2))  # Shanghai - Asia
    concities.append(Concities(city_id=15, continent_id=2))  # Singapore - Asia
    concities.append(Concities(city_id=16, continent_id=2))  # Dubai - Asia
    concities.append(Concities(city_id=17, continent_id=2))  # Mumbai - Asia
    concities.append(Concities(city_id=18, continent_id=2))  # Hong Kong - Asia
    concities.append(Concities(city_id=19, continent_id=2))  # Bangkok - Asia
    concities.append(Concities(city_id=20, continent_id=2))  # Tel Aviv - Asia

    concities.append(Concities(city_id=21, continent_id=3))  # Cape Town - Africa
    concities.append(Concities(city_id=22, continent_id=3))  # Marrakech - Africa
    concities.append(Concities(city_id=23, continent_id=3))  # Nairobi - Africa
    concities.append(Concities(city_id=24, continent_id=3))  # Cairo - Africa
    concities.append(Concities(city_id=25, continent_id=3))  # Victoria Falls - Africa
    concities.append(Concities(city_id=26, continent_id=3))  # Zanzibar City - Africa
    concities.append(Concities(city_id=27, continent_id=3))  # Cape Coast - Africa
    concities.append(Concities(city_id=28, continent_id=3))  # Dakar - Africa
    concities.append(Concities(city_id=29, continent_id=3))  # Johannesburg - Africa
    concities.append(Concities(city_id=30, continent_id=3))  # Luxor - Africa

    concities.append(Concities(city_id=31, continent_id=4))  # Sydney - Australia and Oceania
    concities.append(Concities(city_id=32, continent_id=4))  # Auckland - Australia and Oceania
    concities.append(Concities(city_id=33, continent_id=4))  # Melbourne - Australia and Oceania
    concities.append(Concities(city_id=34, continent_id=4))  # Queenstown - Australia and Oceania
    concities.append(Concities(city_id=35, continent_id=4))  # Brisbane - Australia and Oceania
    concities.append(Concities(city_id=36, continent_id=4))  # Honolulu - Australia and Oceania
    concities.append(Concities(city_id=37, continent_id=4))  # Fiji - Australia and Oceania
    concities.append(Concities(city_id=38, continent_id=4))  # Suva - Australia and Oceania
    concities.append(Concities(city_id=39, continent_id=4))  # Wellington - Australia and Oceania
    concities.append(Concities(city_id=40, continent_id=4))  # Canberra - Australia and Oceania

    concities.append(Concities(city_id=41, continent_id=5))  # New York City - North America
    concities.append(Concities(city_id=42, continent_id=5))  # Los Angeles - North America
    concities.append(Concities(city_id=43, continent_id=5))  # Toronto - North America
    concities.append(Concities(city_id=44, continent_id=5))  # Mexico City - North America
    concities.append(Concities(city_id=45, continent_id=5))  # Vancouver - North America
    concities.append(Concities(city_id=46, continent_id=5))  # San Francisco - North America
    concities.append(Concities(city_id=47, continent_id=5))  # Chicago - North America
    concities.append(Concities(city_id=48, continent_id=5))  # Miami - North America
    concities.append(Concities(city_id=49, continent_id=5))  # Montreal - North America
    concities.append(Concities(city_id=50, continent_id=5))  # Seattle - North America

    concities.append(Concities(city_id=51, continent_id=6))  # Rio de Janeiro - South America
    concities.append(Concities(city_id=52, continent_id=6))  # Buenos Aires - South America
    concities.append(Concities(city_id=53, continent_id=6))  # Sao Paulo - South America
    concities.append(Concities(city_id=54, continent_id=6))  # Lima - South America
    concities.append(Concities(city_id=55, continent_id=6))  # Bogota - South America
    concities.append(Concities(city_id=56, continent_id=6))  # Santiago - South America
    concities.append(Concities(city_id=57, continent_id=6))  # Cartagena - South America
    concities.append(Concities(city_id=58, continent_id=6))  # Quito - South America
    concities.append(Concities(city_id=59, continent_id=6))  # Salvador - South America
    concities.append(Concities(city_id=60, continent_id=6))  # Lisbon - South America


    

    db.session.add_all(foods)
    db.session.add_all(cities)
    db.session.add_all(continents)
    db.session.add_all(concities)
    db.session.commit()
    print("🌱 Successfully seeded! 🌱")