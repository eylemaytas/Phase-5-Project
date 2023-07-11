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
    foods.append(Food(name="Biltong", image="https://i.pinimg.com/564x/c5/3d/e0/c53de00357e1f515f5af5b0cd337a668.jpg", description="Dried and cured South African meat snack", restaurant_recommendation="Carnivore", city_id=21))
    foods.append(Food(name="Bobotie", image="https://i.pinimg.com/564x/70/35/e4/7035e4bfefc77244b7ccf8b2ca1cbbf5.jpg", description="Traditional South African dish with spiced minced meat and baked egg-based topping", restaurant_recommendation="Gold Restaurant", city_id=21))
    foods.append(Food(name="Malva Pudding", image="https://i.pinimg.com/564x/9f/65/9b/9f659b1050bfacbf5138748783504115.jpg", description="Sweet and sticky baked sponge pudding with apricot jam", restaurant_recommendation="Die Kombuis", city_id=21))

    # Marrakech
    foods.append(Food(name="Tagine", image="https://i.pinimg.com/564x/02/b8/f0/02b8f0cd17e65c85f7e370d89bab3054.jpg", description="Slow-cooked savory stew with meat and vegetables", restaurant_recommendation="Al Fassia", city_id=22))
    foods.append(Food(name="Couscous", image="https://i.pinimg.com/564x/f5/ce/dd/f5ceddbd20ce72087b12f7eaf0587c64.jpg", description="Traditional Moroccan dish with steamed semolina and vegetables", restaurant_recommendation="Nomad", city_id=22))
    foods.append(Food(name="Mint Tea", image="https://i.pinimg.com/564x/fc/b2/ad/fcb2adb1bc14da3b5c23a512ff853894.jpg", description="Refreshing and aromatic Moroccan tea", restaurant_recommendation="Café des Épices", city_id=22))

    # Nairobi
    foods.append(Food(name="Ugali and Sukuma Wiki", image="https://i.pinimg.com/564x/31/9d/dc/319ddc3649455e2b6927dc346631f33f.jpg", description="Kenyan staple made with maize flour served with collard greens", restaurant_recommendation="Mama Oliech", city_id=23))
    foods.append(Food(name="Nyama Choma", image="https://i.pinimg.com/564x/b6/c8/7a/b6c87a8ede3eefeb47d2f025af732b8b.jpg", description="Grilled meat, often goat or beef, served with side dishes", restaurant_recommendation="Carnivore", city_id=23))
    foods.append(Food(name="Mandazi", image="https://i.pinimg.com/564x/66/16/89/661689834b2faaa4352ddf909b6e3fc5.jpg", description="Sweet fried dough similar to donuts or beignets", restaurant_recommendation="Junction Mall Mandazi Stand", city_id=23))

    # Cairo
    foods.append(Food(name="Koshari", image="https://i.pinimg.com/564x/50/de/01/50de01f4f97ef0211920d957bc49fe19.jpg", description="Egyptian comfort food with rice, lentils, pasta, and a spiced tomato sauce", restaurant_recommendation="Abou Tarek", city_id=27))
    foods.append(Food(name="Ful Medames", image="https://i.pinimg.com/564x/be/d6/3e/bed63ea60cb81e62f3d8ec81e5596e25.jpg", description="Stewed fava beans served with toppings and bread", restaurant_recommendation="Felfela", city_id=27))
    foods.append(Food(name="Kofta", image="https://i.pinimg.com/564x/e6/d4/e2/e6d4e2c92086a94f8f37646bbd22b5ad.jpg", description="Grilled or baked ground meat skewers, often served with rice or bread", restaurant_recommendation="Kebdet El Prince", city_id=27))

    # Victoria Falls
    foods.append(Food(name="Bream Fish", image="https://i.pinimg.com/564x/fe/2f/40/fe2f40dc3401776ef93ecfe96bd80e7d.jpg", description="Freshwater fish commonly found in the Zambezi River, usually grilled or fried", restaurant_recommendation="The Boma - Dinner & Drum Show", city_id=28))
    foods.append(Food(name="Sadza", image="https://i.pinimg.com/564x/bb/a9/3d/bba93d6efdb2653e585f64f372e74c9f.jpg", description="Staple food made from finely ground cornmeal, similar to polenta", restaurant_recommendation="Mama Africa Eating House", city_id=28))
    foods.append(Food(name="Game Meat", image="https://harvestingnature.com/wp-content/uploads/2022/12/Photo-Dec-18-2022-22-02-08-scaled.jpg", description="Various types of wild game meat, such as kudu or warthog, often prepared as steaks or stews", restaurant_recommendation="The Smoke that Thunders", city_id=28))

    # Zanzibar City
    foods.append(Food(name="Zanzibar Pizza", image="https://swahilifood.com/wp-content/uploads/2019/04/IMG_0084-scaled-e1596965122470.jpg", description="Thin and crispy stuffed pancakes with various fillings like seafood, meat, or vegetables", restaurant_recommendation="Forodhani Night Market", city_id=29))
    foods.append(Food(name="Octopus Curry", image="https://i.pinimg.com/564x/41/4e/05/414e05635acba43a015c9704eca06c7f.jpg", description="Spicy curry dish made with tender octopus and flavorful spices", restaurant_recommendation="Café Miwa", city_id=29))
    foods.append(Food(name="Urojo Soup", image="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*wqN3OaZqV32PCNcgIucRqg.jpeg", description="Tangy and savory soup with a mix of ingredients like potatoes, lentils, and fried snacks", restaurant_recommendation="Zanzibar Delights", city_id=29))

    # Cape Coast
    foods.append(Food(name="Fante Kenkey", image="https://ocdn.eu/pulscms-transforms/1/HOsk9kqTURBXy8xZjRlOGIyY2NkNjZmYTBkNmIxY2Q0NzYzZDAxZTI4Ny5qcGVnkpUDAMyEzQQ4zQJgkwXNAxbNAa7eAAGhMAU", description="Fermented corn dumplings wrapped in banana leaves, served with fish or meat", restaurant_recommendation="Hansa Kenkey House", city_id=30))
    foods.append(Food(name="Grilled Lobster", image="https://i.pinimg.com/564x/0b/2f/c9/0b2fc9903ca68b5dbdfc64bb9e344d9c.jpg", description="Freshly caught lobster grilled to perfection, often served with spicy sauces", restaurant_recommendation="Biriwa Beach Hotel", city_id=30))
    foods.append(Food(name="Cape Coast Soup", image="https://i.redd.it/9pq8wx23mix41.jpg", description="Hearty soup with a mix of seafood, vegetables, and spices", restaurant_recommendation="Brenu Beach Lodge", city_id=30))

    # Dakar
    foods.append(Food(name="Thieboudienne", image="https://i.pinimg.com/564x/3b/e5/9f/3be59ff5fde097ad806a1b63b3cec813.jpg", description="National dish of Senegal, a flavorful rice and fish stew with vegetables", restaurant_recommendation="Chez Loutcha", city_id=31))
    foods.append(Food(name="Yassa Poulet", image="https://i.pinimg.com/564x/3a/8d/c2/3a8dc2c1b1d115d4528b3d7402ecdb40.jpg", description="Chicken marinated in tangy onion and lemon sauce, often served with rice", restaurant_recommendation="La Calebasse", city_id=31))
    foods.append(Food(name="Mafe", image="https://i.pinimg.com/564x/98/07/fc/9807fc7605598ceb066adf76c7ea9522.jpg", description="Peanut butter stew with meat or vegetables, served with couscous or rice", restaurant_recommendation="Chez Fatou", city_id=31))

    # Johannesburg
    foods.append(Food(name="Braai", image="https://i.pinimg.com/564x/73/a6/af/73a6afb290f0d6c905aa42381940b54b.jpg", description="South African barbecue featuring grilled meat, sausages, and vegetables", restaurant_recommendation="Mzoli's", city_id=32))
    foods.append(Food(name="Bunny Chow", image="https://i.pinimg.com/564x/a3/85/1f/a3851f62b5bad3a7f9a11c71dbbf77c6.jpg", description="Hollowed-out loaf of bread filled with curry, a popular street food", restaurant_recommendation="House of Nsangu", city_id=32))
    foods.append(Food(name="Malva Pudding", image="https://i.pinimg.com/564x/7c/36/5f/7c365f8866f67c783cac0c7f8db7674c.jpg", description="Sweet and sticky baked sponge pudding with apricot jam, often served with custard", restaurant_recommendation="Sophiatown Bar Lounge", city_id=32))

    # Luxor
    foods.append(Food(name="Koshari", image="https://i.pinimg.com/564x/e3/f2/c6/e3f2c600edee3c37d4434b563ea5aca1.jpg", description="Egyptian comfort food with rice, lentils, pasta, and a spiced tomato sauce", restaurant_recommendation="Abou Shakra", city_id=33))
    foods.append(Food(name="Ful Medames", image="https://i.pinimg.com/564x/46/12/b9/4612b9680751354f038a6981604969c9.jpg", description="Stewed fava beans served with toppings and bread", restaurant_recommendation="Hoda Restaurant", city_id=33))
    foods.append(Food(name="Taameya", image="https://i.pinimg.com/564x/a4/5d/16/a45d16e96b5093e9d245f2f00761c1f1.jpg", description="Egyptian falafel made from mashed fava beans or chickpeas", restaurant_recommendation="El Hussein", city_id=33))

    # Sydney
    foods.append(Food(name="Fish and Chips", image="https://media.timeout.com/images/105728822/1920/1080/image.jpg", description="Classic dish of battered fish and crispy fries", restaurant_recommendation="Sydney Fish Market", city_id=34))
    foods.append(Food(name="Meat Pie", image="https://imgix.theurbanlist.com/content/general/best-pies-sydney-2021.jpg?auto=format,compress&w=740&h=486&fit=crop", description="Savory pie filled with minced meat and gravy", restaurant_recommendation="Harry's Cafe de Wheels", city_id=34))
    foods.append(Food(name="Pavlova", image="https://i.pinimg.com/564x/c1/bd/6a/c1bd6a22284d59674e3ddf44061f2608.jpg", description="Dessert made of meringue, whipped cream, and fresh fruits", restaurant_recommendation="Black Star Pastry", city_id=34))

    # Auckland
    foods.append(Food(name="Hangi", image="https://supervalue.imgix.net/assets/recipes/iStock-516816688.jpg?&ch=Width,DPR&fit=crop&auto=format%2C%20compress&q=70", description="Traditional Maori dish of meat and vegetables cooked in an earth oven", restaurant_recommendation="Hangi Master", city_id=35))
    foods.append(Food(name="Pork Belly", image="https://i.pinimg.com/564x/82/06/43/8206436d0f2e7ecb9ad785366f993f11.jpg", description="Slow-cooked pork belly with crispy crackling, often served with roasted vegetables", restaurant_recommendation="The Grove", city_id=35))
    foods.append(Food(name="Pavlova", image="https://i.pinimg.com/564x/c1/bd/6a/c1bd6a22284d59674e3ddf44061f2608.jpg", description="Dessert made of meringue, whipped cream, and fresh fruits", restaurant_recommendation="Moustache Milk & Cookie Bar", city_id=35))

    # Melbourne
    foods.append(Food(name="Chicken Parmigiana", image="https://media.timeout.com/images/105725924/1920/1080/image.jpg", description="Breaded chicken cutlet topped with tomato sauce and melted cheese, served with fries or salad", restaurant_recommendation="The Pub", city_id=36))
    foods.append(Food(name="Lamb Roast", image="https://i.pinimg.com/564x/4c/6c/83/4c6c831162041b01afbdc8691849124d.jpg", description="Slow-roasted lamb with herbs and spices, often served with roasted vegetables and gravy", restaurant_recommendation="The Meat & Wine Co", city_id=36))
    foods.append(Food(name="Vanilla Slice", image="https://i.pinimg.com/564x/5b/46/54/5b465406d16042ab059259abda439600.jpg", description="Pastry dessert with layers of custard and puff pastry, topped with icing", restaurant_recommendation="Bourke Street Bakery", city_id=36))

    # Queenstown
    foods.append(Food(name="Fergburger", image="https://media-cdn.tripadvisor.com/media/photo-s/06/5d/25/90/fergburger.jpg", description="Iconic burger filled with a variety of toppings and sauces", restaurant_recommendation="Fergburger", city_id=37))
    foods.append(Food(name="Venison", image="https://www.saveur.com/uploads/2018/12/18/52L6W7ML34KL4YCAVTIILLVDYI.jpg?auto=webp&auto=webp&optimize=high&quality=70&width=1440", description="Tender and flavorful deer meat, often served as steaks or in stews", restaurant_recommendation="Rata Dining", city_id=37))
    foods.append(Food(name="Hokey Pokey Ice Cream", image="https://icecreamfromscratch.com/wp-content/uploads/2022/12/Hokey-Pokey-Ice-Cream-1.2.jpg", description="New Zealand's classic ice cream flavor with caramelized honeycomb toffee pieces", restaurant_recommendation="Patagonia Chocolates", city_id=37))

    # Brisbane
    foods.append(Food(name="Barramundi", image="https://media.blueapron.com/recipes/1944/square_newsletter_images/1478273125-4-4502/111418_2PF_Barramundi-RESHOOT-0144_SQ.jpg?quality=80&width=850&format=pjpg", description="Popular Australian fish known for its sweet and buttery flavor, often grilled or fried", restaurant_recommendation="The Fish House", city_id=38))
    foods.append(Food(name="Prawn Cocktail", image="https://i.pinimg.com/564x/b2/9b/0f/b29b0f26f8db14076002a6763f2fe6ca.jpg", description="Chilled prawns served with a tangy cocktail sauce and lettuce", restaurant_recommendation="Cha Cha Char Wine Bar & Grill", city_id=38))
    foods.append(Food(name="Tim Tam", image="https://assets.bonappetit.com/photos/5888f63dc60fe15a61297432/4:3/w_3699,h_2774,c_limit/chewy-caramel-tim-tam.jpg", description="Chocolate-coated biscuit with a creamy filling, a beloved Australian treat", restaurant_recommendation="Woolworths", city_id=38))

    # Honolulu
    foods.append(Food(name="Poke Bowl", image="https://www.hawaiimagazine.com/content/uploads/2020/12/5bestpoke-foodland.png", description="Hawaiian dish with diced raw fish, rice, and various toppings", restaurant_recommendation="Ono Seafood", city_id=39))
    foods.append(Food(name="Kalua Pig", image="https://www.cookingclassy.com/wp-content/uploads/2020/05/kalua-pork-1.jpg", description="Slow-roasted pig cooked in an underground oven, a traditional Hawaiian luau dish", restaurant_recommendation="Kono's North Shore", city_id=39))
    foods.append(Food(name="Shave Ice", image="https://i.pinimg.com/564x/2a/b0/bc/2ab0bcc8eb3ecacf4206265d3c389fcb.jpg", description="Flavored shaved ice topped with syrup and various toppings, a refreshing treat", restaurant_recommendation="Matsumoto Shave Ice", city_id=39))

    # Fiji
    foods.append(Food(name="Lovo", image="https://www.sbs.com.au/food/sites/sbs.com.au.food/files/styles/full/public/lovofijianfeastcookedintheearth_0.jpg?itok=9Ny6s6P3&mtime=1541553830", description="Traditional Fijian feast cooked in an underground oven, featuring meats, fish, and vegetables", restaurant_recommendation="Namosi Highland Picnic", city_id=40))
    foods.append(Food(name="Kokoda", image="https://www.saveur.com/uploads/2019/02/08/DUCNM4MDNXXYW7HUTIHWWKN5AM.jpg?auto=webp&auto=webp&optimize=high&quality=70&width=1440", description="Fijian ceviche made with raw fish marinated in coconut milk and citrus juices", restaurant_recommendation="Indigo Indian Asian Restaurant", city_id=40))
    foods.append(Food(name="Cassava Cake", image="https://i.pinimg.com/564x/49/c3/23/49c32380a73b2ee2989ec5e63d5660b4.jpg", description="Dessert made from grated cassava, coconut milk, and sugar, often served with coconut cream", restaurant_recommendation="Nadina Authentic Fijian Restaurant", city_id=40))

    # Suva
    foods.append(Food(name="Palusami", image="https://i.pinimg.com/564x/01/18/cc/0118ccf5c3530bcafa57dc7e6ce3d13f.jpg", description="Taro leaves filled with coconut cream and onions, cooked in an underground oven", restaurant_recommendation="Daikoku Fiji", city_id=41))
    foods.append(Food(name="Kokoda", image="https://i.pinimg.com/564x/ba/69/66/ba696672c37b9ecfdd3dd5c00d316e4e.jpg", description="Fijian ceviche made with raw fish marinated in coconut milk and citrus juices", restaurant_recommendation="Rewa Café", city_id=41))
    foods.append(Food(name="Fried Rice", image="https://i.pinimg.com/564x/a8/f1/93/a8f1935a5caf89b347ca11f9e791100c.jpg", description="Stir-fried rice with vegetables, meat, and/or seafood, a popular Chinese-inspired dish", restaurant_recommendation="Tai's Place", city_id=41))

    # Wellington
    foods.append(Food(name="Hangi Pie", image="https://iconiceats.co.nz/wp-content/uploads/2021/08/BlueRose01-2048x1365.jpg", description="Meat and vegetable pie with flavors inspired by traditional Maori hangi", restaurant_recommendation="The British Pie Shop", city_id=43))
    foods.append(Food(name="Whitebait Fritter", image="https://d3lp4xedbqa8a5.cloudfront.net/s3/digital-cougar-assets/food/2016/09/26/35319/whitebait-fritters.jpg?width=922&height=768&mode=crop&anchor=topcenter&quality=75", description="Egg-battered fritter filled with tiny whitebait fish, a classic New Zealand delicacy", restaurant_recommendation="Maranui Café", city_id=43))
    foods.append(Food(name="Kiwifruit Pavlova", image="https://img.taste.com.au/iGAw1TLs/w720-h480-cfill-q80/taste/2016/11/kiwi-passionfruit-pavlova-79408-1.jpeg", description="Pavlova dessert topped with slices of kiwifruit, a popular New Zealand fruit", restaurant_recommendation="Sweet Bakery and Cakery", city_id=43))

    # Canberra
    foods.append(Food(name="Barramundi", image="https://media.blueapron.com/recipes/1944/square_newsletter_images/1478273125-4-4502/111418_2PF_Barramundi-RESHOOT-0144_SQ.jpg?quality=80&width=850&format=pjpg", description="Popular Australian fish known for its sweet and buttery flavor, often grilled or fried", restaurant_recommendation="Pialligo Estate", city_id=44))
    foods.append(Food(name="Australian Meat Pie", image="https://www.wandercooks.com/wp-content/uploads/2020/10/australian-meat-party-pies-5.jpg", description="Individual-sized savory pie filled with minced meat and gravy, a classic Australian snack", restaurant_recommendation="Gus' Cafe", city_id=44))
    foods.append(Food(name="Lamington", image="https://www.thespruceeats.com/thmb/u_JVYFPo9KHEkYaRiKF8RLU-gJc=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/SES-lamington-cake-recipe-256086-b7ee6d18303c423db87bf0752419de02.jpg", description="Sponge cake coated in chocolate icing and desiccated coconut, a beloved Australian treat", restaurant_recommendation="Dobinsons Bakery Cafe", city_id=44))

    # New York City
    foods.append(Food(name="New York-style Pizza", image="https://i.pinimg.com/564x/fb/55/55/fb555527058ecad1797448c022780071.jpg", description="Large, thin-crust pizza with classic toppings like cheese, pepperoni, and tomato sauce", restaurant_recommendation="Joe's Pizza", city_id=45))
    foods.append(Food(name="Pastrami Sandwich", image="https://i.pinimg.com/564x/5a/5a/07/5a5a078c367bbde173594c491f21f7ea.jpg", description="Hearty sandwich filled with thinly sliced, smoky pastrami, usually served on rye bread with mustard", restaurant_recommendation="Katz's Delicatessen", city_id=45))
    foods.append(Food(name="Cheesecake", image="https://i.pinimg.com/564x/c4/57/97/c45797743e0f1d95b30a98e80cbbda19.jpg", description="Rich and creamy dessert made with cream cheese, eggs, and a graham cracker crust", restaurant_recommendation="Junior's", city_id=45))

    # Los Angeles
    foods.append(Food(name="Taco", image="https://i.pinimg.com/564x/5c/76/b9/5c76b97473ba7ae1ef9ba34df9ff15bb.jpg", description="Mexican street food staple consisting of a tortilla filled with various ingredients like grilled meat, salsa, and guacamole", restaurant_recommendation="Guisados", city_id=46))
    foods.append(Food(name="Korean BBQ", image="https://i.pinimg.com/564x/70/9e/43/709e43d24978438610df8b1a35db066f.jpg", description="Grilled marinated meats, typically beef, served with rice, kimchi, and other side dishes", restaurant_recommendation="Park's BBQ", city_id=46))
    foods.append(Food(name="Acai Bowl", image="https://i.pinimg.com/564x/72/9d/4a/729d4a7d3e97d781123af1ec06bc7905.jpg", description="Healthy breakfast bowl made with acai berries, topped with granola, fruits, and honey", restaurant_recommendation="Backyard Bowls", city_id=46))

    # Toronto
    foods.append(Food(name="Peameal Bacon Sandwich", image="https://www.cbc.ca/stevenandchris/content/images/roasted_peameal_bacon_sandwich.jpg", description="Sandwich made with peameal bacon, a type of Canadian bacon, often served on a bun with mustard", restaurant_recommendation="Carousel Bakery", city_id=47))
    foods.append(Food(name="Poutine", image="https://media.timeout.com/images/105451314/1920/1080/image.jpg", description="Classic Canadian dish of french fries topped with cheese curds and smothered in gravy", restaurant_recommendation="Smoke's Poutinerie", city_id=47))
    foods.append(Food(name="Butter Tart", image="https://www.biggerbolderbaking.com/wp-content/uploads/2021/03/Canadian-Butter-Tarts-scaled.jpg", description="Sweet pastry tart filled with a gooey mixture of butter, sugar, and eggs", restaurant_recommendation="Le Gourmand", city_id=47))

    # Mexico City
    foods.append(Food(name="Tacos al Pastor", image="https://www.jocooks.com/wp-content/uploads/2022/04/tacos-al-pastor-feature-1.jpg", description="Marinated pork tacos topped with pineapple, onion, and cilantro", restaurant_recommendation="El Huequito", city_id=48))
    foods.append(Food(name="Chiles en Nogada", image="https://assets.elgourmet.com/wp-content/uploads/2023/03/BO5RnJFRWk8aNcMETODOSXVNiGbXQVPX4Mp-1024x683.png.webp", description="Stuffed poblano peppers topped with walnut sauce and pomegranate seeds, a traditional Mexican dish", restaurant_recommendation="El Cardenal", city_id=48))
    foods.append(Food(name="Mexican Street Corn (Elote)", image="https://cookieandkate.com/images/2020/08/elote-recipe-2.jpg", description="Grilled corn on the cob coated with mayo, cheese, chili powder, and lime juice", restaurant_recommendation="Elote Man", city_id=48))

    # Vancouver
    foods.append(Food(name="Salmon Sushi", image="https://tryhiddengems.com/wp-content/uploads/VancouverAburiSushi6-1024x576.jpg", description="Fresh salmon sashimi or nigiri sushi, a popular seafood delicacy in Vancouver", restaurant_recommendation="Miku", city_id=49))
    foods.append(Food(name="Japadog", image="https://www.yvr.ca/-/media/yvr/blog/2022/japadog/88_yvr_japadog_march3_2022.jpg", description="Japanese-style hot dog topped with unique toppings like teriyaki sauce, seaweed, and Japanese mayo", restaurant_recommendation="Japadog", city_id=49))
    foods.append(Food(name="Nanaimo Bar", image="https://montecristomagazine.com/wp-content/uploads/2021/04/NanaimoRecipe-1.jpg", description="Layered dessert bar with a chocolate-coconut base, custard filling, and chocolate ganache on top", restaurant_recommendation="Butter Baked Goods", city_id=49))

    # San Francisco
    foods.append(Food(name="Cioppino", image="https://diethood.com/wp-content/uploads/2021/01/Cioppino-6.jpg", description="Seafood stew made with a variety of fish and shellfish, usually served with crusty bread", restaurant_recommendation="Tadich Grill", city_id=50))
    foods.append(Food(name="Mission Burrito", image="https://www.seriouseats.com/thmb/00BXhhQBN0wQN6-TajgPYXjd8n0=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/20191002-san-francisco-burritos-TaqueriaGuadalejara-lori-eanes-9762fdae2ecd47e6927d51805760b1b1.jpg", description="Large, overstuffed burrito filled with ingredients like rice, beans, meat, salsa, and guacamole", restaurant_recommendation="La Taqueria", city_id=50))
    foods.append(Food(name="Sourdough Bread", image="https://heartbeetkitchen.com/foodblog/wp-content/uploads/2020/04/basic-sourdough-bread-recipe4.jpg", description="Tangy and crusty bread made from naturally fermented dough, a San Francisco specialty", restaurant_recommendation="Boudin Bakery", city_id=50))

    # Chicago
    foods.append(Food(name="Deep Dish Pizza", image="https://www.thecookierookie.com/wp-content/uploads/2023/05/Chicago-Style-Deep-Dish-Pizza-4-edited.jpg", description="Thick, deep-dish pizza with a buttery crust, gooey cheese, and chunky tomato sauce", restaurant_recommendation="Lou Malnati's Pizzeria", city_id=51))
    foods.append(Food(name="Chicago-style Hot Dog", image="https://static01.nyt.com/images/2022/07/27/dining/27Chicagodogrex/05Chicagodogrex-articleLarge.jpg", description="All-beef hot dog topped with mustard, onions, relish, tomato slices, pickle spear, sport peppers, and celery salt, served on a poppy seed bun", restaurant_recommendation="Portillo's", city_id=51))
    foods.append(Food(name="Italian Beef Sandwich", image="https://www.wellplated.com/wp-content/uploads/2021/04/Italian-Beef-Recipe.jpg", description="Thinly sliced roast beef piled on a crusty roll and dipped in flavorful gravy, a Chicago classic", restaurant_recommendation="Al's Beef", city_id=51))

    # Miami
    foods.append(Food(name="Cuban Sandwich", image="https://www.seriouseats.com/thmb/DMduS_tw16ftsr8NJq7NHqUTfb4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/cuban-sandwich-recipe-Hero-5833ef16ac3f4ebe99fb3156c9fe2e0c.jpg", description="Grilled sandwich with ham, roasted pork, Swiss cheese, pickles, and mustard, pressed on Cuban bread", restaurant_recommendation="Versailles Restaurant", city_id=52))
    foods.append(Food(name="Key Lime Pie", image="https://i0.wp.com/www.livewellbakeoften.com/wp-content/uploads/2021/05/Key-Lime-Pie-NEW.jpg?w=1200&ssl=1", description="Tangy and creamy pie made with key lime juice and a graham cracker crust", restaurant_recommendation="Joe's Stone Crab", city_id=52))
    foods.append(Food(name="Stone Crab", image="https://media.timeout.com/images/104085872/1920/1080/image.jpg", description="Freshly caught stone crab claws served chilled with mustard sauce, a popular seafood delicacy in Miami", restaurant_recommendation="Joe's Stone Crab", city_id=52))

    # Montreal
    foods.append(Food(name="Poutine", image="https://indie88.com/wp-content/uploads/2018/09/poutine.jpg", description="Classic Canadian dish of french fries topped with cheese curds and smothered in gravy", restaurant_recommendation="La Banquise", city_id=53))
    foods.append(Food(name="Smoked Meat Sandwich", image="https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Schwartz_smoked_meat_montreal.JPG/2560px-Schwartz_smoked_meat_montreal.JPG", description="Sandwich made with flavorful smoked meat, typically served on rye bread with mustard", restaurant_recommendation="Schwartz's Deli", city_id=53))
    foods.append(Food(name="Bagels", image="https://i0.wp.com/www.onceuponachef.com/images/2022/05/MontrealBagels_0263-scaled.jpg?resize=1365%2C2048&ssl=1", description="Chewy and slightly sweet bagels, often topped with sesame seeds and served with cream cheese and smoked salmon", restaurant_recommendation="Fairmount Bagel", city_id=53))

    # Seattle
    foods.append(Food(name="Seattle-style Hot Dog", image="https://www.thespruceeats.com/thmb/R3ImDoIX7zI1vWMmcOA4Yg9cNUg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/seattle-hot-dogs-4773446-Hero-01-394711d96fc34b569634bd6497dbd796.jpg", description="Hot dog topped with cream cheese, grilled onions, and sautéed onions, a unique Seattle twist", restaurant_recommendation="Monster Dogs", city_id=54))
    foods.append(Food(name="Salmon Chowder", image="https://images.themodernproper.com/billowy-turkey/production/posts/2019/salmon-chowder-14.jpg?w=1200&q=82&fm=jpg&fit=crop&dm=1684213205&s=b920dd0a2afd7fda1a420d08309d29bf", description="Creamy chowder made with fresh salmon, potatoes, and vegetables, a Pacific Northwest specialty", restaurant_recommendation="Pike Place Chowder", city_id=54))
    foods.append(Food(name="Dungeness Crab", image="https://www.foodiecrush.com/wp-content/uploads/2016/11/The-Easiest-Dungeness-Crab-Recipe-foodiecrush.com-0011.jpg", description="Sweet and flavorful crab, often served steamed or in various seafood dishes, a local delicacy in Seattle", restaurant_recommendation="The Crab Pot", city_id=54))

    # Rio de Janeiro
    foods.append(Food(name="Feijoada", image="https://i.pinimg.com/564x/ab/14/59/ab14591fedcf4bf5632e489dbad68725.jpg", description="Rich and hearty black bean stew with various cuts of pork and served with rice, collard greens, and farofa", restaurant_recommendation="Casa da Feijoada", city_id=55))
    foods.append(Food(name="Coxinha", image="https://blog.amigofoods.com/wp-content/uploads/2019/09/brazilian-chicken-coxinha.jpg", description="Deep-fried dough filled with shredded chicken and cream cheese, a popular Brazilian snack", restaurant_recommendation="Bar do Mineiro", city_id=55))
    foods.append(Food(name="Caipirinha", image="https://www.liquor.com/thmb/W0TdVI7hFql6gfp8XazymQ8mqQs=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/caipirnha-720x720-primary-40900f56782b4c1d8c79494c9b413f9c.jpg", description="Refreshing cocktail made with cachaça, sugar, and lime, Brazil's national drink", restaurant_recommendation="Jobi", city_id=55))

    # Buenos Aires
    foods.append(Food(name="Asado", image="https://media.tacdn.com/media/attractions-splice-spp-674x446/0a/32/47/0f.jpg", description="Argentine-style barbecue with various cuts of grilled meat, often served with chimichurri sauce", restaurant_recommendation="La Brigada", city_id=56))
    foods.append(Food(name="Empanadas", image="https://assets.bonappetit.com/photos/58a34e1df12ac6e639bf24ae/1:1/w_2240,c_limit/argentinian-beef-empanadas.jpg", description="Savory pastries filled with meat, cheese, or vegetables, a popular street food in Argentina", restaurant_recommendation="El Sanjuanino", city_id=56))
    foods.append(Food(name="Milanesa", image="https://i.pinimg.com/564x/1f/15/d8/1f15d8e337068524aded38d6209070d8.jpg", description="Breaded and fried meat cutlets, typically made with beef or chicken, served with mashed potatoes or salad", restaurant_recommendation="El Preferido de Palermo", city_id=56))

    # Sao Paulo
    foods.append(Food(name="Pastel", image="https://i.pinimg.com/564x/76/bf/bc/76bfbc2424bcee6ddfb4b56f6d139568.jpg", description="Deep-fried pastry filled with various savory fillings, such as cheese, meat, or heart of palm", restaurant_recommendation="Feira da Liberdade", city_id=57))
    foods.append(Food(name="Virado à Paulista", image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Virado_a_paulista.jpg/1920px-Virado_a_paulista.jpg", description="Traditional dish consisting of beans, rice, pork chops, sausage, collard greens, and a fried egg, a classic meal in Sao Paulo", restaurant_recommendation="Bar do Biu", city_id=57))
    foods.append(Food(name="Coxinha de Frango", image="https://receitasimplesefacil.com.br/wp-content/uploads/2022/02/Coxinha-de-Frango-scaled.jpg", description="Chicken croquette with a dough filled with shredded chicken, shaped like a drumstick", restaurant_recommendation="Veloso", city_id=57))

    # Lima
    foods.append(Food(name="Ceviche", image="https://www.peruhop.com/wp-content/uploads/La-Mar-ceviche-Small-2.jpg", description="Fresh raw fish marinated in citrus juice, typically seasoned with onions, chili peppers, and cilantro", restaurant_recommendation="La Mar", city_id=58))
    foods.append(Food(name="Lomo Saltado", image="https://www.seriouseats.com/thmb/RCkiNb_SbnrgTdupIh7NsLvAvrg=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/__opt__aboutcom__coeus__resources__content_migration__serious_eats__seriouseats.com__2019__03__20190321-lomo-saltado-vicky-wasik-28-68ac118a03324091afed4205428ddf4e.jpg", description="Stir-fried beef with onions, tomatoes, and french fries, often served with rice", restaurant_recommendation="Tanta", city_id=58))
    foods.append(Food(name="Anticuchos", image="https://www.eatperu.com/wp-content/uploads/2022/01/peruvian-beed-heart-kebab-recipe.jpg", description="Grilled skewers of marinated meat, usually beef heart, served with potatoes and corn", restaurant_recommendation="Panchita", city_id=58))

    # Bogota
    foods.append(Food(name="Ajiaco", image="https://www.thespruceeats.com/thmb/LkZa7ts4OhNdo4n6vIQpiOcfasw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/colombian-chicken-and-potato-stew-4120146-hero-01-d6dcdf2fe44342d9893b25659ad041c7.jpg", description="Hearty soup made with chicken, potatoes, corn, and guascas herb, often served with avocado and capers", restaurant_recommendation="La Puerta Falsa", city_id=59))
    foods.append(Food(name="Bandeja Paisa", image="https://popmenucloud.com/cdn-cgi/image/width%3D3840%2Cheight%3D3840%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/sqbhvkor/e1a2dfb7-8dd1-4218-8a34-acfee78bed85.jpg", description="Traditional platter consisting of rice, beans, grilled steak, chorizo, fried pork belly, plantains, arepa, avocado, and a fried egg", restaurant_recommendation="Andres Carne de Res", city_id=59))
    foods.append(Food(name="Arepa", image="https://www.xtremefoodies.com/sites/default/files/Arepa.jpg", description="Cornmeal patty served with various fillings, such as cheese, meat, or eggs, a staple food in Colombia", restaurant_recommendation="La Puerta Falsa", city_id=59))

    # Santiago
    foods.append(Food(name="Completo", image="https://i0.wp.com/tarasmulticulturaltable.com/wp-content/uploads/2016/06/Completo-Italiano-Chilean-Italian-Style-Hot-Dog-2-of-3-1.jpg?w=1300&ssl=1", description="Chilean-style hot dog topped with avocado, mayonnaise, sauerkraut, and tomato", restaurant_recommendation="Fuente Alemana", city_id=60))
    foods.append(Food(name="Pastel de Choclo", image="https://www.comedera.com/wp-content/uploads/2022/12/Pastel-de-choclo-chileno.jpg", description="Corn and meat pie topped with sugar, a traditional dish in Chile", restaurant_recommendation="Las Delicias de Quirihue", city_id=60))
    foods.append(Food(name="Cazuela", image="https://www.tasteofhome.com/wp-content/uploads/2018/01/Cazuela_EXPS_MIOPBZ17_5633_B10_012_3b.jpg?fit=700,1024", description="Hearty soup made with meat, potatoes, corn, pumpkin, and various vegetables, a popular Chilean comfort food", restaurant_recommendation="El Hoyo", city_id=60))

    # Cartagena
    foods.append(Food(name="Arepas de Huevo", image="https://www.mycolombianrecipes.com/wp-content/uploads/2023/03/Arepa-de-Huevo-Recipe.jpg", description="Fried cornmeal patties filled with scrambled eggs, a popular snack in Cartagena", restaurant_recommendation="La Cocina de Pepina", city_id=61))
    foods.append(Food(name="Sancocho de Pescado", image="https://cdn.colombia.com/gastronomia/2011/07/28/sancocho-de-pescado-1642.webp", description="Fish stew made with coconut milk, yuca, plantains, and various spices, a traditional dish in Cartagena", restaurant_recommendation="La Mulata", city_id=61))
    foods.append(Food(name="Camarones al Ajillo", image="https://diethood.com/wp-content/uploads/2023/01/camarones-al-ajillo-garlic-shrimp-1.jpg", description="Garlic shrimp sautéed in olive oil, often served with rice or bread, a popular seafood dish in Cartagena", restaurant_recommendation="La Cevicheria", city_id=61))

    # Quito
    foods.append(Food(name="Locro de Papa", image="https://www.bonella.com.ec/-/media/Project/Upfield/Brands/Rama/Rama-EC/Assets/Recipes/sync-img/1e7b3493-d630-421a-9c3a-35156540d88d.jpg?rev=d860b5d4b7d444bdb24564d04a242a53&w=900", description="Creamy potato soup with cheese, avocado, and crispy pork skin, a traditional dish in Ecuador", restaurant_recommendation="Cafe Dios No Muere", city_id=63))
    foods.append(Food(name="Cuy", image="https://www.thedailymeal.com/img/gallery/what-is-cuy/crop%203285113200_d40e7500bb_o.jpg", description="Roasted guinea pig, a unique delicacy in Ecuador", restaurant_recommendation="El Crater", city_id=63))
    foods.append(Food(name="Encebollado", image="https://blog.amigofoods.com/wp-content/uploads/2020/09/encebollado-ecuadorian-stew.jpg", description="Fish soup made with albacore tuna, yuca, onions, and spices, often served with pickled onions and avocado slices", restaurant_recommendation="Lo de Carlitos", city_id=63))

    # Salvador
    foods.append(Food(name="Acarajé", image="https://www.thespruceeats.com/thmb/94QudT5WddjJgmk070IqIgnH1EU=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/SES-brazilian-black-eyed-pea-shrimp-fritters-3028859-f7183508846f43838ca7b713d3b887c0.jpg", description="Deep-fried black-eyed pea fritters filled with shrimp, vatapá, and caruru, a popular street food in Bahia", restaurant_recommendation="Dinha Acarajé", city_id=64))
    foods.append(Food(name="Moqueca de Camarão", image="https://skinnyspatula.com/wp-content/uploads/2021/06/Brazilian_Prawn_Stew3.jpg", description="Creamy shrimp stew cooked with coconut milk, palm oil, peppers, onions, and tomatoes, a traditional dish in Bahia", restaurant_recommendation="Restaurante Yemanjá", city_id=64))
    foods.append(Food(name="Acaí na Tigela", image="https://images.food52.com/j9NLFmC-c-Yi1UK7nlvZxON9Hww=/2016x1344/filters:format(webp)/a74f268b-0ef7-49be-9872-f857001d43ad--tumblr_n2wggbyc4Q1reeddko2_1280.jpg", description="Frozen acai berry puree topped with granola, banana, and other fruits, a popular Brazilian snack", restaurant_recommendation="Açaí Concept", city_id=64))

    # Lisbon
    foods.append(Food(name="Pastel de Nata", image="https://spanishsabores.com/wp-content/uploads/2019/06/Pasteis-de-nata-2397-Blog.jpg", description="Creamy custard tart with a caramelized top, a famous Portuguese pastry", restaurant_recommendation="Pasteis de Belém", city_id=65))
    foods.append(Food(name="Bacalhau à Brás", image="https://www.foodandwine.com/thmb/TdZP92mInzQmKFUWLfu1zW3RWB4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/201501-xl-bacalhau-a-bras-2ff72a7a6ae14518b2dcd7509a52b618.jpg", description="Shredded codfish sautéed with onions, potatoes, eggs, and olives, a classic Portuguese dish", restaurant_recommendation="A Brasileira", city_id=65))
    foods.append(Food(name="Francesinha", image="https://www.thetravelmentor.com/wp-content/uploads/2021/10/close_up_francesinha_cafe_santiago_porto_portugal.jpg", description="Hearty sandwich with layers of cured meats, melted cheese, and a spicy tomato-based sauce, a specialty of Porto but popular in Lisbon too", restaurant_recommendation="Cervejaria Gazela", city_id=65))


    cities = []
    cities.append(City(name="Istanbul", image="https://www.celebritycruises.com/blog/content/uploads/2022/12/best-time-to-visit-istanbul-hero-cta.jpg",language="Turkish",description="Istanbul is a city steeped in history and culture so there is much to see and do there. From its Byzantine churches adorned with mosaics and frescoes to its magnificent mosques decorated by sky-high minarets, Istanbul is a city that will mesmerize you at every turn."))
    cities.append(City(name="Paris", image="https://wallpapers.com/images/hd/romantic-eiffel-paris-babqqvmcylchhb6i.webp", language="French", description="Paris — the City of Light — has been a beacon of culture for centuries. As a world capital of art, fashion, food, literature, and ideas, it stands as a symbol of all the fine things human civilization can offer. Paris offers sweeping boulevards, chatty crêpe stands, chic boutiques, and world-class art galleries"))
    cities.append(City(name="Rome", image="https://images.pexels.com/photos/1797161/pexels-photo-1797161.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", language="Italian", description="Rome is often referred to as the City of Seven Hills due to its geographic location, and also as the 'Eternal City'. Rome is generally considered to be the 'cradle of Western civilization and Christian culture', and the centre of the Catholic Church."))
    cities.append(City(name="Barcelona", image="https://images.unsplash.com/photo-1583422409516-2895a77efded?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2940&q=80", language="Spanish", description="It is Spain's major Mediterranean port and commercial centre and is famed for its individuality, cultural interest, and physical beauty."))
    cities.append(City(name="Prague", image="https://a.cdn-hotels.com/gdcs/production131/d1659/aa53e340-f585-11e8-b8fa-0242ac11000d.jpg?impolicy=fcrop&w=1600&h=1066&q=medium", language="Czech", description="Situated in the northwest of the country on the Vltava River, Prague is the capital and the largest city of the Czech Republic. This magical city of bridges, cathedrals, gold-tipped towers and church spires is also the fourteenth largest city in the European Union."))
    cities.append(City(name="Amsterdam", image="https://www.travelandleisure.com/thmb/FVnQw8F6k79tsfS4TPAxQuICwic=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/amsterdam-nl-AMSTERDAMTG0521-6d2bfaac29704667a950bcf219680640.jpg", language="Dutch", description="Amsterdam is known for its beautiful canals, quirky architecture, and lively nightlife. It's also a great place to find Dutch art and culture, and the city has a rich history that dates back to the 13th century."))
    cities.append(City(name="Vienna", image="https://www.travelandleisure.com/thmb/LjkeMsDoZVX1eo5SdPK_uj5guoY=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/vienna-austria-VIENNATG0621-ecb0ee926c2d49c4bce610db594f7405.jpg", language="German", description="Austria's capital Vienna offers a blend of imperial traditions, music, and endearing charm. A city that inspires with the old and the new alike, and always has a cosy place available in a coffee house or wine tavern."))
    cities.append(City(name="Athens", image="https://c4.wallpaperflare.com/wallpaper/607/836/982/ancient-history-tourism-ruins-temple-wallpaper-preview.jpg", language="Greek", description="The capital of Greece is full of ancient monuments, temples, ruins and churches. For lovers of ancient Greece, this city is a paradise. You really have to see the Acropolis. This hill in the middle of Athens has some of the most important archaeological monuments."))
    cities.append(City(name="Dublin", image="https://i.pinimg.com/564x/b4/ff/d8/b4ffd89bd41e17b082ab64d32d8f9289.jpg", language="English", description="Dublin is Ireland's capital city and its most historically significant, having been the second city of the British Empire until Ireland's independence in 1922. Dublin today is teeming with enough art, culture, and monuments to fill multiple itineraries."))
    cities.append(City(name="Stockholm", image="https://media.timeout.com/images/105171709/1920/1080/image.jpg", language="Swedish", description="Stockholm is known as one of the most inclusive and welcoming cities in the world. Its contemporary, urban appeal is balanced with centuries-old history and closeness to nature. As for the things to do in Stockholm, the list is endless."))
    cities.append(City(name="Budapest", image="https://i.pinimg.com/564x/2e/45/67/2e456776951f1ecad05cb48e157d17e4.jpg", language="Hungarian", description="Budapest, with its stunning landscape and rich architectural and historical heritage, offers a unique combination of diverse cultural backgrounds, fine cuisine and wide array of leisurely activities."))
    
    
    cities.append(City(name="Tokyo", image="https://i.pinimg.com/564x/c8/c6/70/c8c67058a55b856c5d3e8754c0efcc61.jpg", language="Japanese", description="Tokyo is the administrative, cultural, financial, commercial, and educational centre of Japan and the focus of an extensive urban complex that includes Kawasaki and Yokohama. Attractions include the Imperial Palace, encircled by stone-walled moats and broad gardens, and numerous temples and shrines."))
    cities.append(City(name="Seoul", image="https://koreankulture.com/wp-content/uploads/Gyeongbokgung-Palace-in-Seoul-South-Korea.jpg", language="Korean", description="Seoul is a vibrant and dynamic city that is truly worth visiting. Known for its delicious fusion cuisine, art galleries, and bustling bars, there is no shortage of activities to enjoy."))
    cities.append(City(name="Shanghai", image="https://i.natgeofe.com/n/302104d1-7616-4ba2-8fa4-316a96b9d718/shanghai_travel_2x3.jpg", language="Mandarin", description="With its innovative architecture, rich history and lush nature, it's no surprise that Shanghai is one of the world's most visited cities. As China's biggest and most developed city, Shanghai is worth visiting whether you're a dedicated shopper, Disney fan, keen historian, or anything in between."))
    cities.append(City(name="Singapore", image="https://subsites-newsroom.imgix.net/sites/pinnews/files/post_main_content_image/2019-07/Singapore%20Image%20Final_0.jpg?ixlib=php-3.3.1&s=599c327224d6caba6391a4fcc057ecd2", language="English", description="Singapore is famous for being a global financial center, being among the most densely populated places in the world, having a world-class city airport with a waterfall, and a Botanic Garden that is a World Heritage Site."))
    cities.append(City(name="Dubai", image="https://lp-cms-production.imgix.net/features/2017/09/dubai-marina-skyline-2c8f1708f2a1.jpg?auto=format&w=1440&h=810&fit=crop&q=75", language="Arabic", description="With stunning architecture, fancy hotels, shopping festivals, majestic skyscrapers, glittering skylines, and giant shopping malls, Dubai is truly a paradise for scores of tourists from around the world. Known to be one of the most progressive regions in the Middle East region, Dubai has undergone a huge transformation."))
    cities.append(City(name="Mumbai", image="https://www.micato.com/wp-content/uploads/2018/09/mumbai-5.jpg.webp", language="Hindi", description="Mumbai is known for its lively and cosmopolitan atmosphere, as well as its rich history and culture. The city has long been associated with the film industry and is often referred to as the “Bollywood capital.” Mumbai is famous for its bustling markets, street food, and iconic landmarks such as the Gateway of India."))
    cities.append(City(name="Hong Kong", image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Hong_Kong_Harbour_Night_2019-06-11.jpg/2880px-Hong_Kong_Harbour_Night_2019-06-11.jpg", language="Cantonese", description="Hong Kong is one of the major tourist destinations in the world because of its gastronomic affair, vibrant nightlife, beautiful temples, and spell-binding natural beauty. Also, Hong Kong is known for being a paradise for shopaholics."))
    cities.append(City(name="Bangkok", image="https://content.r9cdn.net/rimg/dimg/26/5b/01e97574-city-26166-1592813274a.jpg?width=1366&height=768&xhint=1038&yhint=725&crop=true", language="Thai", description="City of Temples"))
    cities.append(City(name="Tel Aviv", image="https://media.timeout.com/images/105434111/1920/1080/image.jpg", language="Hebrew", description="Tel Aviv is an international, modern city that has a vibrant, multicultural atmosphere with the perfect beach/city mix! It's young and full of amazing nightlife, food and culture. There's no other place quite like it!"))

   
    cities.append(City(name="Cape Town", image="https://upload.wikimedia.org/wikipedia/commons/e/ec/Aerial_View_of_Sea_Point%2C_Cape_Town_South_Africa.jpg", language="English", description="Cape Town, South Africa's second-largest city, ranks among the most beautiful in the world. With its larger-than-life mountain overlooking the City Bowl, harbour, white beaches and Robben Island beyond, this is a tourists' playground."))
    cities.append(City(name="Marrakech", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Marokko0112_%28retouched%29.jpg/1024px-Marokko0112_%28retouched%29.jpg", language="Arabic", description="Marrakech, also spelt Marrakesh, is an intoxicating city known for its souks, spices and snake charmers, though these days it is also prized as much for its trendy art galleries, classy boutique hotels and luxurious hammams."))
    cities.append(City(name="Nairobi", image="https://www.andbeyond.com/wp-content/uploads/sites/5/giraffe-and-sky-line-nairobi.jpg", language="Swahili", description="Nairobi is famous for being the only capital city that contains a national park. The city's proximity to Nairobi National Park has given it the name of 'the safari capital of Kenya'."))
    cities.append(City(name="Cairo", image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Flickr_-_HuTect_ShOts_-_Citadel_of_Salah_El.Din_and_Masjid_Muhammad_Ali_%D9%82%D9%84%D8%B9%D8%A9_%D8%B5%D9%84%D8%A7%D8%AD_%D8%A7%D9%84%D8%AF%D9%8A%D9%86_%D8%A7%D9%84%D8%A3%D9%8A%D9%88%D8%A8%D9%8A_%D9%88%D9%85%D8%B3%D8%AC%D8%AF_%D9%85%D8%AD%D9%85%D8%AF_%D8%B9%D9%84%D9%8A_-_Cairo_-_Egypt_-_17_04_2010_%284%29.jpg/2560px-thumbnail.jpg", language="Arabic", description="Cairo, the bustling capital of Egypt, is a city of contrasts, where ancient wonders coexist with modern skyscrapers and vibrant markets. With its rich history, diverse culture, and stunning architecture, Cairo offers visitors an unforgettable travel experience that is both captivating and enlightening."))
    cities.append(City(name="Victoria Falls", image="https://lp-cms-production.imgix.net/image_browser/victoria-falls-aerial-shot.jpg?auto=format&w=1440&h=810&fit=crop&q=75", language="English", description="As well as being a natural wonder, Victoria Falls is a hub of activity. There is something for everyone. For the adrenaline junkies, there is white rafting, kayaking, the 111-metre high bungee jump, river surfing, gorge swings and zip wires."))
    cities.append(City(name="Zanzibar City", image="https://planetofhotels.com/guide/sites/default/files/styles/big_gallery_image/public/text_gallery/zanzibar-1.jpg", language="Swahili", description="Zanzibar is an escape from the everyday and the ordinary, with world-class beaches, and a rich history, culture, and geography like no other in the world. It's a true tropical paradise, but with so much more to offer than just surface beauty."))
    cities.append(City(name="Cape Coast", image="https://upload.wikimedia.org/wikipedia/commons/a/a0/Cape_Coast_Castle%2C_Cape_Coast%2C_Ghana.JPG", language="English", description="Cape Coast is one of the most historical cities in Ghana. Portuguese colonists built a trading fort in the area. In 1650, the Swedes built a lodge that would later become the better known Cape Coast Castle, which is now a World Heritage Site. Most of the modern town expanded around it."))
    cities.append(City(name="Dakar", image="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Ngor_Beach.jpg/1920px-Ngor_Beach.jpg", language="French", description="Dakar is the political, economic and cultural capital of Senegal since April 4, 1960. It includes the historic district of the Medina and the famous Theodore Monod museum, which exhibit African works of art. It is also famous for its nightlife centered on Mbalax music."))
    cities.append(City(name="Johannesburg", image="https://media.timeout.com/images/105237782/image.jpg", language="English", description="The city boasts vibrant nightlife world-class cuisine, and a rich cultural history to explore. Johannesburg offers something for everyone with its cutting-edge art galleries, live music venues, and exciting shopping districts."))
    cities.append(City(name="Luxor", image="https://cdn.britannica.com/08/178108-050-F19D0A38/statues-entrance-Ramses-II-Luxor-temple-complex.jpg", language="Arabic", description="Luxor is often referred to today as the 'world's largest open-air museum'. This name comes from the fact that the modern city is located at the same site as ancient Thebes. It has literally been built upon and around the treasures of the Old Kingdom, which are still being unearthed to this day."))

   
    cities.append(City(name="Sydney", image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Sydney_Opera_House_and_Harbour_Bridge_Dusk_%282%29_2019-06-21.jpg/2880px-Sydney_Opera_House_and_Harbour_Bridge_Dusk_%282%29_2019-06-21.jpg", language="English", description="A city of iconic attractions and brilliant beaches, Sydney is a destination you'll never forget. Sydney is home to must-visit icons like the Sydney Harbour Bridge and Opera House, but this Harbour City is constantly evolving."))
    cities.append(City(name="Auckland", image="https://a.cdn-hotels.com/gdcs/production133/d294/4e4195aa-b9ca-42cd-923f-e8a65c8c5c7b.jpg?impolicy=fcrop&w=800&h=533&q=medium", language="English", description="Some of the best things to do in Auckland highlight its vibrant Maori community, waterfront seafood restaurants and bars, as well as a dazzling skyline. Nestled in a bay on the North Island, the city faces the Pacific Ocean on one side and the Tasman Sea."))
    cities.append(City(name="Melbourne", image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Melbourne_CBD_and_Princes_Bridge_at_night_%282013%29.jpg/2880px-Melbourne_CBD_and_Princes_Bridge_at_night_%282013%29.jpg", language="English", description="Nestled right to the bottom of Australia lies Melbourne, known as the place-to-be for sport, food and culture. Characterised by its heritage buildings, stunning gardens, and magical city laneways, Melbourne is loved by all."))
    cities.append(City(name="Queenstown", image="https://upload.wikimedia.org/wikipedia/commons/c/c9/Queenstown_1_%288168013172%29.jpg", language="English", description="World-renowned for its adventure, Queenstown is home to a huge choice of adrenaline activities including jet boating. When the cooler months arrive Queenstown transforms into a world class winter resort, with four ski areas and a range of activities, bars, restaurants and ways to relax and unwind."))
    cities.append(City(name="Brisbane", image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Sunsets_of_Brisbane%2C_Queensland%2C_September_2021%2C_01.jpg/1920px-Sunsets_of_Brisbane%2C_Queensland%2C_September_2021%2C_01.jpg", language="English", description="The country's best beaches are only a short drive away. The job market is great and continues to grow. It is much more affordable than some of Australia's other big cities. There is a large population of young people, so there are plenty of people to meet!"))
    cities.append(City(name="Honolulu", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/King_Kamehameha_I_Statue_-_Honolulu_%284_by_3%29.jpg/1920px-King_Kamehameha_I_Statue_-_Honolulu_%284_by_3%29.jpg", language="English", description="Honolulu is the largest city in the state of Hawaii and also home to the State Capitol. Rich in Hawaiian cultural and geographical history, this island houses 3 active volcanoes, gorgeous waterfalls, black sand beaches, and coffee farms."))
    cities.append(City(name="Fiji", image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Lautoka_Streets_20.jpg/2560px-Lautoka_Streets_20.jpg", language="English", description="Fiji is popularly known for its attractive pacific islands, such as the larger Vanua Levu and Viti Levu islands. Moreover, the people of Fiji are among the warmest, friendliest, and most welcoming in the world. This is because the Fijian culture emphasises friendship in various aspects."))
    cities.append(City(name="Suva", image="https://static01.nyt.com/images/2023/05/06/travel/oakImage-1663853463601/oakImage-1663853463601-superJumbo.jpg?quality=75&auto=webp", language="English", description="A tropical metropolis, Suva offers a mix of historical sites, museums, parks, and local markets along with a vibrant nightlife. Bula and welcome to Fiji's capital and largest city! Here you will find yourself in one of the most cosmopolitan centres in the South Pacific, home to around a third of Fiji's population."))
    cities.append(City(name="Wellington", image="https://static01.nyt.com/images/2022/12/05/multimedia/05-36hours-wellington-1-0bfb/05-36hours-wellington-1-0bfb-superJumbo.jpg", language="English", description="From the world's best coffee, to scenic views which will blow your mind, a unique and cozy bar scene, and accessibility to both the North and South Islands, Wellington is one of those city's you really shouldn't miss."))
    cities.append(City(name="Canberra", image="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Canberra_viewed_from_Mount_Ainslie.jpg/2560px-Canberra_viewed_from_Mount_Ainslie.jpg", language="English", description="Canberra is a planned city, with national monuments, museums and galleries built around a large artificial lake. As a bush capital, Canberra is also a great place to enjoy the outdoors, with excellent cycling, gardens, parks, bushwalking and nature reserves."))
   

    #north america
    cities.append(City(name="New York City", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/2560px-New_york_times_square-terabass.jpg", language="English", description="New York is well known for many things, but one of them is easily its artistic prowess and the talent it homes. It's also a great spot for some huge, fascinating museums, and if you're always up for some peaceful contemplation and beautiful sights, this is a top spot."))
    cities.append(City(name="Los Angeles", image="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Hollywood_Sign_%28Zuschnitt%29_%28cropped%29.jpg/1920px-Hollywood_Sign_%28Zuschnitt%29_%28cropped%29.jpg", language="English", description="Los Angeles, or LA, is one of the most well-known cities in the world. But why is Los Angeles so famous? Hollywood stars, the TV & movie industries, and gorgeous beaches all make LA a famous city and a popular vacation spot."))
    cities.append(City(name="Toronto", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Toronto_-_ON_-_Skyline_bei_Nacht.jpg/1920px-Toronto_-_ON_-_Skyline_bei_Nacht.jpg", language="English", description="With its highly iconic landmark of the CN Tower gracing its skyline, Toronto is also famous for its beautiful lake scenery with much of the city straddling and rising up against the gorgeous Lake Ontario."))
    cities.append(City(name="Mexico City", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Chapultepec_castle_in_Mexico_city.jpg/2560px-Chapultepec_castle_in_Mexico_city.jpg", language="Spanish", description="As one of the most populous cities in the world, Mexico City teems with rich history that you can uncover at area museums, monuments and archeological sites. But Mexico's capital has evolved into the center of its modern political and economic and cultural spheres."))
    cities.append(City(name="Vancouver", image="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/A_look_downtown_%28759827996%29.jpg/2560px-A_look_downtown_%28759827996%29.jpg", language="English", description="With its scenic views, mild climate, and friendly people, Vancouver is known around the world as both a popular tourist attraction and one of the best places to live."))
    cities.append(City(name="San Francisco", image="https://cdn.britannica.com/13/77413-050-95217C0B/Golden-Gate-Bridge-San-Francisco.jpg", language="English", description="San Francisco, city and port, coextensive with San Francisco county, northern California, U.S., located on a peninsula between the Pacific Ocean and San Francisco Bay. It is a cultural and financial centre of the western United States and one of the country's most cosmopolitan cities."))
    cities.append(City(name="Chicago", image="https://www.travelandleisure.com/thmb/L2dnLH86xwCJfZ8fIVBT2Sp9D9s=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/chicago-illinois-CHITG0221-e448062fc5164da0bba639f9857987f6.jpg", language="English", description="Dotted along the diverse tourist area are world-famous landmarks like The Wrigley Building, the John Hancock Center, and Tribune Tower, as well a sleuth of high-end boutiques, speakeasy pubs, and revered underground eateries."))
    cities.append(City(name="Miami", image="https://a.travel-assets.com/findyours-php/viewfinder/images/res70/471000/471674-Miami.jpg", language="English", description="Miami is home to miles of the most beautiful white and golden sand beaches. The turquoise waters in front of you, and the palm trees swaying behind; you'll feel like you are in a tropical paradise. Not only that, many of the beaches have gym apparatus so you can work out whilst enjoying the spectacular weather."))
    cities.append(City(name="Montreal", image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Vieux-Montr%C3%A9al_%28525744602%29.jpg/2560px-Vieux-Montr%C3%A9al_%28525744602%29.jpg", language="French", description="Montreal is one of the most festive cities in Canada, and that's one of the reasons why that people love to visit. There's a wide range of fun and exciting events happening year-round, and especially during the warmer months (June–September); it can feel like there's one long city-wide festival going on."))
    cities.append(City(name="Seattle", image="https://upload.wikimedia.org/wikipedia/commons/5/58/Seattle_Center_as_night_falls.jpg", language="English", description="Seattle is a vibrant city with exciting things to do and see that will make any visit worthwhile. For those looking for an outdoor escape, Seattle offers lush green spaces, majestic mountain views, and plenty of opportunities for activities like hiking, kayaking, and camping."))

    #south america
    cities.append(City(name="Rio de Janeiro", image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Cidade_Maravilhosa.jpg/2560px-Cidade_Maravilhosa.jpg", language="Portuguese", description="Rio's natural beauty is the most distinguishing reason to visit. You can explore the tropical rainforest of Floresta da Tijuca, appreciate the white-sand and turquoise water of Ipanema beach, or relax at the city's many epic lookout points like Pedra do Telégrafo."))
    cities.append(City(name="Buenos Aires", image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Puerto_Madero%2C_Buenos_Aires_%2840689219792%29_%28cropped%29.jpg/2880px-Puerto_Madero%2C_Buenos_Aires_%2840689219792%29_%28cropped%29.jpg", language="Spanish", description="Known as the “Paris of the south”, Buenos Aires boasts renowned architecture, world-class cuisine, vibrant entertainment, world-class shopping, rich historical sites, and more."))
    cities.append(City(name="Sao Paulo", image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Ponte_Estaiada_e_CENU.jpg/1920px-Ponte_Estaiada_e_CENU.jpg", language="Portuguese", description="The world of arts and theatrical plays stands out in São Paulo. Latin America's cultural center, São Paulo has 101 museums, 282 movie theaters, 146 libraries and around 40 cultural centers; besides several popular festivities and fair that take place in its streets."))
    cities.append(City(name="Lima", image="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Plaza_de_Armas%2C_Lima.jpg/2560px-Plaza_de_Armas%2C_Lima.jpg", language="Spanish", description="Lima is known for its award-winning Peruvian gastronomy, two miles of parks along the Pacific coast, museums and gorgeous colonial Plaza de Armas. Being the capital, it is the home to the government buildings and palaces as well."))
    cities.append(City(name="Bogota", image="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Colegio_Mayor_de_San_Bartolom%C3%A9%2C_Plaza_de_Bol%C3%ADvar.jpg/1920px-Colegio_Mayor_de_San_Bartolom%C3%A9%2C_Plaza_de_Bol%C3%ADvar.jpg", language="Spanish", description="The city where the past and present meet. Bogotá is the capital of and largest city in Colombia. It is a place of convergence for people from all around the country and is therefore diverse and multicultural. Within this city, the past and present come together."))
    cities.append(City(name="Santiago", image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/2019-04-06-12h10m43.jpg/1920px-2019-04-06-12h10m43.jpg", language="Spanish", description="Santiago is best known for its street dancing, nightlife, and amazing tourist attractions like the Central Market, Plaza de Armas, Cerro Santa Lucia, La Moneda Palace, La Chascona, San Cristobal Hill, and Museo de la Memoria Chilena."))
    cities.append(City(name="Cartagena", image="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Amarillo_Latente.jpg/2560px-Amarillo_Latente.jpg", language="Spanish", description="Cartagena is an unmissable place to visit and Colombia's most popular city for tourists, thanks not only to the colonial buildings but also to the sandy beaches, mouth-watering cuisine, and raucous nightlife."))
    cities.append(City(name="Quito", image="https://upload.wikimedia.org/wikipedia/commons/5/58/Iglesia_de_San_Francisco%2C_Quito%2C_Ecuador%2C_2015-07-22%2C_DD_171-173_HDR.JPG", language="Spanish", description="Quito is a place rich in culture and architectural beauty. As the capital of Ecuador, it boasts the largest and best preserved historic center in the Americas."))
    cities.append(City(name="El Salvador", image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Vulkan_Chaparrastique%2C_El_Salvador_2013_01.JPG/2560px-Vulkan_Chaparrastique%2C_El_Salvador_2013_01.JPG", language="Portuguese", description="El Salvador may be the smallest country in Central America, but it's certainly one of its most charming. Less touristy than its neighbours, El Salvador is rich in natural beauty, pristine beaches, countless volcanoes, many Maya ruins and a great culture and rich history."))
    cities.append(City(name="Lisbon", image="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Lisbon_%2836831596786%29_%28cropped%29.jpg/2560px-Lisbon_%2836831596786%29_%28cropped%29.jpg", language="Portuguese", description="Lisbon is probably best known for its colonial history, ornate architecture and tradition of Fado music. But some of its best features are in the everyday – spectacular hilltop vistas in Alfama or at St. George's Castle, blue-and-white tile-covered facades, pleasant year-round weather and friendly locals"))




    continents = []
    continents.append(Continent(name="Europe",image="https://www.visa.co.uk/dam/VCOM/regional/ve/unitedkingdom/in-page-images/visa-in-europe/visa-eu-header-france-1600x900.jpg",belongs="where"))
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