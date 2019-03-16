import scrapy


class HillSpider(scrapy.Spider):   

 #identity
    name = "allbeachdes"

    #Request
    start_urls= [
        
        'https://www.holidayiq.com/Baga-Beach-Calangute-Sightseeing-319-9090.html',
        'https://www.holidayiq.com/Calangute-Beach-Calangute-Sightseeing-319-9209.html',
        'https://www.holidayiq.com/Baga-River-Calangute-Sightseeing-319-9094.html',
        'https://www.holidayiq.com/Juhu-Beach-Mumbai-Sightseeing-468-8292.html',
        'https://www.holidayiq.com/Elephanta-Island-Mumbai-Sightseeing-468-8281.html',
        'https://www.holidayiq.com/Cherai-Beach-Kochi-Cochin-Sightseeing-335-1273.html',
        'https://www.holidayiq.com/Fort-Kochi-Beach-Kochi-Cochin-Sightseeing-335-244.html',
        'https://www.holidayiq.com/Udaipur-Beach-Digha-Sightseeing-601-18774.html',
        'https://www.holidayiq.com/Talasari-Digha-Sightseeing-601-1049.html',
        'https://www.holidayiq.com/New-Digha-Digha-Sightseeing-601-9258.html',
        'https://www.holidayiq.com/Digha-Beach-Digha-Sightseeing-601-9256.html',
        'https://www.holidayiq.com/Subarnarekha-River-Digha-Sightseeing-601-9259.html',
        'https://www.holidayiq.com/Ramakrishna-Beach-Visakhapatnam-Sightseeing-592-1495.html',
        'https://www.holidayiq.com/Rishikonda-Beach-Visakhapatnam-Sightseeing-592-171.html',
        'https://www.holidayiq.com/Yarada-Beach-Visakhapatnam-Sightseeing-592-11091.html',
        'https://www.holidayiq.com/Bheemunipatnam-Beach-Visakhapatnam-Sightseeing-592-31971.html',
        'https://www.holidayiq.com/Kanyakumari-Beach-Kanyakumari-Sightseeing-401-614.html',
        'https://www.holidayiq.com/Sothavilai-Beach-Kanyakumari-Sightseeing-401-9285.html',
        'https://www.holidayiq.com/Mandarmani-Beach-Mandarmani-Sightseeing-1208-9640.html',
        'https://www.holidayiq.com/The-Delta-Mandarmani-Sightseeing-1208-9641.html',
        'https://www.holidayiq.com/Digha-Beach-Mandarmani-Sightseeing-1208-9643.html',
        'https://www.holidayiq.com/Jolly-Buoy-Island-Port-Blair-Sightseeing-516-18508.html',
        'https://www.holidayiq.com/Ross-Island-Port-Blair-Sightseeing-516-12811.html',
        'https://www.holidayiq.com/Little-Andaman-Island-Port-Blair-Sightseeing-516-12813.html',
        'https://www.holidayiq.com/North-Bay-Island-Andaman-Port-Blair-Sightseeing-516-18513.html',
        'https://www.holidayiq.com/Wandoor-Beach-Port-Blair-Sightseeing-516-21032.html',
        'https://www.holidayiq.com/Red-Skin-Island-Port-Blair-Sightseeing-516-18511.html',
        'https://www.holidayiq.com/Lime-Stone-Cave-And-Mud-Volcano-At-Baratang-Port-Blair-Sightseeing-516-32302.html',
        'https://www.holidayiq.com/Corbyns-Cove-Port-Blair-Sightseeing-516-12814.html',
        'https://www.holidayiq.com/Long-Island-Port-Blair-Sightseeing-516-1572.html',
        'https://www.holidayiq.com/Vembanad-Lake-Alappuzha-Alleppey-Sightseeing-262-233.html',
        'https://www.holidayiq.com/Mararikulam-Beach-Alappuzha-Alleppey-Sightseeing-262-13859.html',
        'https://www.holidayiq.com/Kayamkulam-Lake-Alappuzha-Alleppey-Sightseeing-262-528.html',
        'https://www.holidayiq.com/Alleppey-Beach-Alappuzha-Alleppey-Sightseeing-262-1108.html',
        'https://www.holidayiq.com/Pathiramannal-Alappuzha-Alleppey-Sightseeing-262-1109.html',
        'https://www.holidayiq.com/Alappuzha-Lighthouse-Alappuzha-Alleppey-Sightseeing-262-36781.html',
        'https://www.holidayiq.com/The-Lighthouse-Kovalam-Sightseeing-425-8690.html',
        'https://www.holidayiq.com/Lighthouse-Beach-Kovalam-Sightseeing-425-245.html',
        'https://www.holidayiq.com/Samudra-Beach-Kovalam-Sightseeing-425-8066.html',
        'https://www.holidayiq.com/Hawa-Beach-Kovalam-Sightseeing-425-631.html',
        'https://www.holidayiq.com/Shangumukam-Beach-Kovalam-Sightseeing-425-20465.html',
        'https://www.holidayiq.com/Karamana-River-Kovalam-Sightseeing-425-8691.html',
        'https://www.holidayiq.com/Vizhinjam-Fishing-Harbour-Kovalam-Sightseeing-425-1307.html',
        'https://www.holidayiq.com/Akkulam-Lake-Kovalam-Sightseeing-425-8693.html',
        'https://www.holidayiq.com/Vellayani-Lake-Kovalam-Sightseeing-425-1310.html',
        'https://www.holidayiq.com/Alibag-Beach-Alibaug-Sightseeing-602-2351.html',
        'https://www.holidayiq.com/Varsoli-Beach-Alibaug-Sightseeing-602-2358.html',
        'https://www.holidayiq.com/Kihim-Beach-Alibaug-Sightseeing-602-10129.html',
        'https://www.holidayiq.com/Nagaon-Beach-Alibaug-Sightseeing-602-2347.html',
        'https://www.holidayiq.com/Mandwa-Beach-Alibaug-Sightseeing-602-10130.html',
        'https://www.holidayiq.com/Akshi-Beach-Alibaug-Sightseeing-602-2349.html',
        'https://www.holidayiq.com/Thal-Beach-Alibaug-Sightseeing-602-10131.html',
        'https://www.holidayiq.com/Rewas-Jetty-Alibaug-Sightseeing-602-10136.html',
        'https://www.holidayiq.com/Karli-Backwaters-Tarkarli-Sightseeing-698-11083.html',
        'https://www.holidayiq.com/Achra-Beach-Tarkarli-Sightseeing-698-11081.html',
        'https://www.holidayiq.com/Dhamapur-Lake-Tarkarli-Sightseeing-698-11079.html',
        'https://www.holidayiq.com/Kolamb-Beach-Tarkarli-Sightseeing-698-11082.html',
        'https://www.holidayiq.com/Poovar-Island-Trivandrum-Thiruvananthapuram-Sightseeing-572-18640.html',
        'https://www.holidayiq.com/Light-House-Beach-Trivandrum-Thiruvananthapuram-Sightseeing-572-12956.html',
        'https://www.holidayiq.com/Samudra-Beach-Trivandrum-Thiruvananthapuram-Sightseeing-572-12958.html',
        'https://www.holidayiq.com/Shanghumukham-Beach-Trivandrum-Thiruvananthapuram-Sightseeing-572-1465.html',
        'https://www.holidayiq.com/Hawa-Beach-Trivandrum-Thiruvananthapuram-Sightseeing-572-12957.html',
        'https://www.holidayiq.com/Radhanagar-Beach-Havelock-Island-Sightseeing-616-8234.html',
        'https://www.holidayiq.com/Elephant-Beach-Havelock-Island-Sightseeing-616-8235.html',
        'https://www.holidayiq.com/Kaala-Pathar-Beach-Havelock-Island-Sightseeing-616-18945.html',
        'https://www.holidayiq.com/Neil-Island-Havelock-Island-Sightseeing-616-8241.html',
        'https://www.holidayiq.com/Vijaynagar-Beach-Havelock-Island-Sightseeing-616-8236.html',
        'https://www.holidayiq.com/Inglis-Island-Havelock-Island-Sightseeing-616-18947.html',
        'https://www.holidayiq.com/Panambur-Beach-Mangalore-Sightseeing-456-10570.html',
        'https://www.holidayiq.com/Tannirubhavi-Beach-Mangalore-Sightseeing-456-28955.html',
        'https://www.holidayiq.com/St-MaryS-Islands-Mangalore-Sightseeing-456-28953.html',
        'https://www.holidayiq.com/Mangalore-Beach-Mangalore-Sightseeing-456-10560.html',
        'https://www.holidayiq.com/Someshwar-Beach-Mangalore-Sightseeing-456-10569.html',
        'https://www.holidayiq.com/Benaulim-Village-And-Beach-Colva-Sightseeing-337-8895.html',
        'https://www.holidayiq.com/Nagoa-Beach-Diu-Sightseeing-14848-9404.html',
        'https://www.holidayiq.com/Jallandhar-Beach-Diu-Sightseeing-14848-9406.html',
        'https://www.holidayiq.com/Ghoghla-Beach-Diu-Sightseeing-14848-9409.html',
        'https://www.holidayiq.com/Sunset-Point-Diu-Sightseeing-14848-9415.html',
        'https://www.holidayiq.com/Gomatimata-Beach-Diu-Sightseeing-14848-9408.html',
        'https://www.holidayiq.com/Chakratirath-Beach-Diu-Sightseeing-14848-9407.html',
        'https://www.holidayiq.com/Chowpatty-Beach-Mumbai-Sightseeing-468-8280.html',
        'https://www.holidayiq.com/Powai-Lake-Mumbai-Sightseeing-468-20307.html',
        'https://www.holidayiq.com/Worli-Sea-Face-Mumbai-Sightseeing-468-33849.html',
        'https://www.holidayiq.com/Marve-Beach-Mumbai-Sightseeing-468-18419.html',
        'https://www.holidayiq.com/Wellingdon-Island-Kochi-Cochin-Sightseeing-335-1271.html',
        'https://www.holidayiq.com/Jaigad-Lighthouse-Ganpatipule-Sightseeing-356-12484.html',
        'https://www.holidayiq.com/Mangamaripeta-Visakhapatnam-Sightseeing-592-1502.html',
        'https://www.holidayiq.com/Gangavaram-Beach-Visakhapatnam-Sightseeing-592-11088.html',
        'https://www.holidayiq.com/Muttom-Beach-Kanyakumari-Sightseeing-401-9287.html',
        'https://www.holidayiq.com/Visakhapatnam-Visakhapatnam-Sightseeing-592-34250.html',
        'https://www.holidayiq.com/Thengapattinam-Beach-Kanyakumari-Sightseeing-401-9294.html',
        'https://www.holidayiq.com/Bhimli-Visakhapatnam-Sightseeing-592-174.html',
        'https://www.holidayiq.com/Kappad-Beach-Kozhikode-Calicut-Sightseeing-426-10323.html',
        'https://www.holidayiq.com/Kozhikode-Beach-Kozhikode-Calicut-Sightseeing-426-635.html',
        'https://www.holidayiq.com/Beypore-Beach-Kozhikode-Calicut-Sightseeing-426-636.html',
        'https://www.holidayiq.com/Kalipoyika-Kozhikode-Calicut-Sightseeing-426-10319.html',
        'https://www.holidayiq.com/Canolly-Canal-Kozhikode-Calicut-Sightseeing-426-1633.html',
        'https://www.holidayiq.com/Smith-Island-Port-Blair-Sightseeing-516-1574.html',
        'https://www.holidayiq.com/Collinpur-Port-Blair-Sightseeing-516-12808.html',
        'https://www.holidayiq.com/Viper-Island-Port-Blair-Sightseeing-516-21031.html',
        'https://www.holidayiq.com/Mahabalipuram-Beach-Mahabalipuram-Sightseeing-446-9995.html',
        'https://www.holidayiq.com/Mamallapuram-Lighthouse-Mahabalipuram-Sightseeing-446-18657.html',
        'https://www.holidayiq.com/Kudle-Beach-Gokarna-Sightseeing-615-730.html',
        'https://www.holidayiq.com/Om-Beach-Gokarna-Sightseeing-615-8939.html',
        'https://www.holidayiq.com/Half-Moon-Beach-Gokarna-Sightseeing-615-8940.html',
        'https://www.holidayiq.com/Paradise-Beach-Gokarna-Sightseeing-615-8941.html',
        'https://www.holidayiq.com/Apsarakonda-Gokarna-Sightseeing-615-32215.html',
        'https://www.holidayiq.com/Gokarna-Beach-Gokarna-Sightseeing-615-8937.html',
        'https://www.holidayiq.com/Jampore-Beach-Daman-Sightseeing-14847-9384.html',
        'https://www.holidayiq.com/Devka-Beach-Daman-Sightseeing-14847-9383.html',
        'https://www.holidayiq.com/Chowara-Beach-Trivandrum-Thiruvananthapuram-Sightseeing-572-18644.html',
        'https://www.holidayiq.com/Vizhinjam-Lighthouse-Trivandrum-Thiruvananthapuram-Sightseeing-572-18641.html',
        'https://www.holidayiq.com/Murudeshwar-Beach-Murudeshwara-Sightseeing-746-8710.html',
        'https://www.holidayiq.com/Netrani-Island-Murudeshwara-Sightseeing-746-10660.html',
        'https://www.holidayiq.com/Bhatkal-Beach-Murudeshwara-Sightseeing-746-10669.html',
        'https://www.holidayiq.com/Bhatkal-Light-House-Murudeshwara-Sightseeing-746-10667.html',
        'https://www.holidayiq.com/New-Mangalore-Port-Mangalore-Sightseeing-456-10539.html',
        'https://www.holidayiq.com/Nandini-River-Mangalore-Sightseeing-456-10553.html',
        'https://www.holidayiq.com/Coco-Beach-Bardez-Sightseeing-906-11284.html',
        'https://www.holidayiq.com/Henrys-Island-Bakkhali-Sightseeing-813-8115.html',
        'https://www.holidayiq.com/Jambu-Dwip-Bakkhali-Sightseeing-813-8114.html',
        'https://www.holidayiq.com/Bakkhali-Sea-Beach-Bakkhali-Sightseeing-813-8112.html',
        'https://www.holidayiq.com/Sagar-Island-Bakkhali-Sightseeing-813-8117.html',
        'https://www.holidayiq.com/Vihar-Lake-Mumbai-Sightseeing-468-8288.html',
        'https://www.holidayiq.com/Munambam-Beach-Kochi-Cochin-Sightseeing-335-34633.html',
        'https://www.holidayiq.com/Gorai-Beach-Gorai-Sightseeing-679-16460.html',
        'https://www.holidayiq.com/Manori-And-Marve-Beaches-Gorai-Sightseeing-679-16461.html',
        'https://www.holidayiq.com/St-Anthonys-Island-Gorai-Sightseeing-679-16463.html',
        'https://www.holidayiq.com/Lawsons-Bay-Visakhapatnam-Sightseeing-592-173.html',
        'https://www.holidayiq.com/Kondakarla-Ava-Beach-Visakhapatnam-Sightseeing-592-11089.html',
        'https://www.holidayiq.com/Uppada-Beach-Kakinada-Sightseeing-658-32547.html',
        'https://www.holidayiq.com/Bhogamdani-Cheruvu-Kakinada-Sightseeing-658-27335.html',
        'https://www.holidayiq.com/Sutta-Point-Port-Blair-Sightseeing-516-21029.html',
        'https://www.holidayiq.com/Gorai-Beach-Manori-Sightseeing-688-14153.html',
        'https://www.holidayiq.com/Manori-Beach-Manori-Sightseeing-688-14151.html',
        'https://www.holidayiq.com/Marve-Beach-Manori-Sightseeing-688-14152.html',
        'https://www.holidayiq.com/Ozran-Beach-Anjuna-Beach-Sightseeing-276-10155.html',
        'https://www.holidayiq.com/Colva-Beach-Varca-Sightseeing-589-12973.html',
        'https://www.holidayiq.com/Varca-Beach-Varca-Sightseeing-589-12972.html',
        'https://www.holidayiq.com/Betalbatim-Beach-Varca-Sightseeing-589-12978.html',
        'https://www.holidayiq.com/Cavelossim-And-Mobor-Beaches-Varca-Sightseeing-589-12975.html',
        'https://www.holidayiq.com/Betul-Beach-Varca-Sightseeing-589-12984.html',
        'https://www.holidayiq.com/Arossim-Beach-Varca-Sightseeing-589-12980.html',
        'https://www.holidayiq.com/Sunset-Beach-Varca-Sightseeing-589-12979.html',
        'https://www.holidayiq.com/Harihareshwar-Beach-Diveagar-Sightseeing-1780-11940.html',
        'https://www.holidayiq.com/Kondivili-Beach-Diveagar-Sightseeing-1780-11937.html',
        'https://www.holidayiq.com/Karaikal-Sandy-Beach-Karaikal-Sightseeing-1092-12289.html',
        'https://www.holidayiq.com/Majorda-Margao-Sightseeing-708-16390.html',
        'https://www.holidayiq.com/Velsao-Beach-Margao-Sightseeing-708-16394.html',
        'https://www.holidayiq.com/Zalor-Beach-Margao-Sightseeing-708-37219.html',
        'https://www.holidayiq.com/Mahatma-Gandhi-Beach-And-Park-Kollam-Quilon-Sightseeing-419-16770.html',
        'https://www.holidayiq.com/Ashtamudi-Lake-Kollam-Quilon-Sightseeing-419-16769.html',
        'https://www.holidayiq.com/Thirumullavaram-Beach-Kollam-Quilon-Sightseeing-419-623.html',
        'https://www.holidayiq.com/Neendakara-Port-Kollam-Quilon-Sightseeing-419-16782.html',
        'https://www.holidayiq.com/Dhavaleshwar-Island-Gopalpur-Sightseeing-363-9268.html',
        'https://www.holidayiq.com/Bordi-Beach-Bordi-Sightseeing-317-9511.html',
        'https://www.holidayiq.com/Hooghly-River-Raichak-Sightseeing-524-10046.html',
        'https://www.holidayiq.com/Diamond-Harbour-Raichak-Sightseeing-524-1061.html',
        'https://www.holidayiq.com/Kukrahati-Raichak-Sightseeing-524-10045.html',
        'https://www.holidayiq.com/Mobor-Beach-Cavelossim-Mobor-Sightseeing-707-11403.html',
        'https://www.holidayiq.com/Cavelossim-Beach-Cavelossim-Mobor-Sightseeing-707-11402.html',
        'https://www.holidayiq.com/Ganapatipule-Beach-Ratnagiri-Sightseeing-692-12893.html',
        'https://www.holidayiq.com/Anjarle-Beach-Ratnagiri-Sightseeing-692-18567.html',
        'https://www.holidayiq.com/Velas-Beach-Ratnagiri-Sightseeing-692-36258.html',
        'https://www.holidayiq.com/Guhagar-Beach-Ratnagiri-Sightseeing-692-18564.html',
        'https://www.holidayiq.com/Aare-Beach-Ratnagiri-Sightseeing-692-12881.html',
        'https://www.holidayiq.com/Mandavi-Beach-Ratnagiri-Sightseeing-692-12889.html',
        'https://www.holidayiq.com/Bhatye-Beach-Ratnagiri-Sightseeing-692-12892.html',
        'https://www.holidayiq.com/Ratnagiri-Lighthouse-Ratnagiri-Sightseeing-692-18566.html',
        'https://www.holidayiq.com/Kovalam-Beach-Poovar-Sightseeing-515-15028.html',
        'https://www.holidayiq.com/Poovar-Beach-Poovar-Sightseeing-515-15027.html',
        'https://www.holidayiq.com/Ravindranath-Tagore-Beach-Karwar-Sightseeing-403-18798.html',
        'https://www.holidayiq.com/Karwar-Beach-Karwar-Sightseeing-403-10296.html',
        'https://www.holidayiq.com/Devbagh-Beach-Karwar-Sightseeing-403-10297.html',
        'https://www.holidayiq.com/Majali-Beach-Karwar-Sightseeing-403-10299.html',
        'https://www.holidayiq.com/Tilmati-Beach-Karwar-Sightseeing-403-27615.html',
        'https://www.holidayiq.com/Binaga-Beach-Karwar-Sightseeing-403-10298.html',
        'https://www.holidayiq.com/Koodi-Bagh-Beach-Karwar-Sightseeing-403-10300.html',
        'https://www.holidayiq.com/Oyster-Rock-Lighthouse-Karwar-Sightseeing-403-10308.html',
        'https://www.holidayiq.com/Bharatpur-Beach-Neil-Island-Sightseeing-836-14607.html',
        'https://www.holidayiq.com/Sitapur-Beach-Neil-Island-Sightseeing-836-14605.html',
        'https://www.holidayiq.com/Kalapathar-Beach-Neil-Island-Sightseeing-836-14613.html',
        'https://www.holidayiq.com/Laxmanpur-Beach-Neil-Island-Sightseeing-836-14606.html',
        'https://www.holidayiq.com/Ramnagar-Beach-Neil-Island-Sightseeing-836-35911.html',
        'https://www.holidayiq.com/Vijaynagar-Beach-Neil-Island-Sightseeing-836-14611.html',
        'https://www.holidayiq.com/Mahim-Beach-Palghar-Sightseeing-1296-15219.html',
        'https://www.holidayiq.com/Kelva-Beach-Palghar-Sightseeing-1296-15221.html',
        'https://www.holidayiq.com/Chinchani-Beach-Palghar-Sightseeing-1296-32735.html',
        'https://www.holidayiq.com/Satpati-Beach-Palghar-Sightseeing-1296-15214.html',
        'https://www.holidayiq.com/Shirgaon-Beach-Palghar-Sightseeing-1296-15216.html',
        'https://www.holidayiq.com/Mypadu-Beach-Nellore-Sightseeing-661-29999.html',
        'https://www.holidayiq.com/Pulicat-Lake-Nellore-Sightseeing-661-30002.html',
        'https://www.holidayiq.com/Koduru-Beach-Nellore-Sightseeing-661-33347.html',
        'https://www.holidayiq.com/Bujabuja-Nellore-Lake-Nellore-Sightseeing-661-29977.html',
        'https://www.holidayiq.com/Varkala-Beach-Varkala-Sightseeing-590-246.html',
        'https://www.holidayiq.com/Kappil-Beach-kappil-Varkala-Varkala-Sightseeing-590-34265.html',
        'https://www.holidayiq.com/Papanasam-Beach-Varkala-Sightseeing-590-712.html',
        'https://www.holidayiq.com/Varkala-Lighthouse-Varkala-Sightseeing-590-12990.html',
        'https://www.holidayiq.com/Ponnumthuruthu-Island-Varkala-Sightseeing-590-12991.html',
        'https://www.holidayiq.com/Thiruvambadi-Beach-Varkala-Sightseeing-590-21651.html',
        'https://www.holidayiq.com/Tarkarli-Beach-Malvan-Sightseeing-686-15399.html',
        'https://www.holidayiq.com/Malvan-Beach-Malvan-Sightseeing-686-15398.html',
        'https://www.holidayiq.com/Devbaug-Beach-Malvan-Sightseeing-686-15410.html',
        'https://www.holidayiq.com/Tsunami-Island-Malvan-Sightseeing-686-33712.html',
        'https://www.holidayiq.com/Kolamb-Beach-Malvan-Sightseeing-686-15401.html',
        'https://www.holidayiq.com/Achara-Beach-Malvan-Sightseeing-686-15406.html',
        'https://www.holidayiq.com/Arse-Mahal-Beach-Malvan-Sightseeing-686-15407.html',
        'https://www.holidayiq.com/Tondavali-Beach-Malvan-Sightseeing-686-15408.html',
        'https://www.holidayiq.com/Shiroda-Velagar-Beach-Malvan-Sightseeing-686-15413.html',
        'https://www.holidayiq.com/Uttorda-Margao-Sightseeing-708-16392.html',
        'https://www.holidayiq.com/Gogal-Lake-Margao-Sightseeing-708-28996.html',
        'https://www.holidayiq.com/Masunda-Lake-Mumbai-Sightseeing-468-20268.html',
        'https://www.holidayiq.com/Sasthamcotta-Lake-Kollam-Quilon-Sightseeing-419-16787.html',
        'https://www.holidayiq.com/Ozran-Beach-Mapusa-Sightseeing-706-16365.html',
        'https://www.holidayiq.com/Harmal-Beach-Mapusa-Sightseeing-706-16373.html',
        'https://www.holidayiq.com/Agonda-Beach-Palolem-Sightseeing-498-15010.html',
        'https://www.holidayiq.com/Harihareshwar-Beach-Harihareshwar-Sightseeing-1779-11427.html',
        'https://www.holidayiq.com/Kondivli-Beach-Harihareshwar-Sightseeing-1779-11431.html',
        'https://www.holidayiq.com/Pandre-Samudra-Ratnagiri-Sightseeing-692-12890.html',
        'https://www.holidayiq.com/Ganeshghule-Beach-Ratnagiri-Sightseeing-692-12891.html',
        'https://www.holidayiq.com/Shastri-River-Ratnagiri-Sightseeing-692-18571.html',
        'https://www.holidayiq.com/Dhamapur-Lake-Ratnagiri-Sightseeing-692-18572.html',
        'https://www.holidayiq.com/Kunkeshwar-Beach-Ratnagiri-Sightseeing-692-18573.html',
        'https://www.holidayiq.com/Devgad-Beach-Ratnagiri-Sightseeing-692-18575.html',
        'https://www.holidayiq.com/Miramar-Beach-Miramar-Sightseeing-610-16698.html',
        'https://www.holidayiq.com/Sinquerim-Beach-Miramar-Sightseeing-610-16705.html',
        'https://www.holidayiq.com/Baga-River-Miramar-Sightseeing-610-16710.html',
        'https://www.holidayiq.com/Coco-Beach-Miramar-Sightseeing-610-16715.html',
        'https://www.holidayiq.com/Vainguinim-Miramar-Sightseeing-610-16701.html',
        'https://www.holidayiq.com/Siridao-Beach-Miramar-Sightseeing-610-16718.html',
        'https://www.holidayiq.com/Kaju-Bagh-Beach-Karwar-Sightseeing-403-18799.html',
        'https://www.holidayiq.com/Harihareshwar-Beach-Shriwardhan-Sightseeing-694-14414.html',
        'https://www.holidayiq.com/Kondivali-Beach-Shriwardhan-Sightseeing-694-14419.html',
        'https://www.holidayiq.com/Shankarpur-Beach-Shankarpur-Sightseeing-812-13844.html',
        'https://www.holidayiq.com/Digha-Beach-Shankarpur-Sightseeing-812-13845.html',
        'https://www.holidayiq.com/Vagator-Beach-Vagator-Sightseeing-584-14759.html',
        'https://www.holidayiq.com/Ashvem-Beach-Vagator-Sightseeing-584-14764.html',
        'https://www.holidayiq.com/Chivia-Beach-Malvan-Sightseeing-686-28872.html',
        'https://www.holidayiq.com/Kodi-Beach-Kundapur-Sightseeing-718-15096.html',
        'https://www.holidayiq.com/Uppinakudru-Kundapur-Sightseeing-718-15098.html',
        'https://www.holidayiq.com/Trasi-Kundapur-Sightseeing-718-15108.html',
        'https://www.holidayiq.com/Coco-Beach-Aguada-Beach-Sightseeing-608-12425.html',
        'https://www.holidayiq.com/Kalacha-Beach-Mapusa-Sightseeing-706-28970.html',
        'https://www.holidayiq.com/Coco-Beach-Mapusa-Sightseeing-706-16356.html',
        'https://www.holidayiq.com/Arpora-Mapusa-Sightseeing-706-16363.html',
        'https://www.holidayiq.com/Baga-River-Mapusa-Sightseeing-706-16339.html',
        'https://www.holidayiq.com/Siridao-Beach-Mapusa-Sightseeing-706-16359.html',
        'https://www.holidayiq.com/Mandrem-Beach-Mapusa-Sightseeing-706-16362.html',
        'https://www.holidayiq.com/Sunset-Beach-Majorda-Beach-Sightseeing-448-12371.html',
        'https://www.holidayiq.com/Vainguinim-Majorda-Beach-Sightseeing-448-837.html',
        'https://www.holidayiq.com/Cavelossim-Beach-Majorda-Beach-Sightseeing-448-12372.html',
        'https://www.holidayiq.com/Dahanu-Beach-Dahanu-Sightseeing-676-11475.html',
        'https://www.holidayiq.com/Bordi-Beach-Dahanu-Sightseeing-676-11478.html',
        'https://www.holidayiq.com/Guhagar-Beach-Guhagar-Sightseeing-1243-16261.html',
        'https://www.holidayiq.com/Palolem-Beach-Canacona-Sightseeing-705-9218.html',
        'https://www.holidayiq.com/Patnem-Beach-Canacona-Sightseeing-705-9219.html',
        'https://www.holidayiq.com/Cola-Beach-Canacona-Sightseeing-705-24261.html',
        'https://www.holidayiq.com/Rajbag-Beach-Canacona-Sightseeing-705-9222.html',
        'https://www.holidayiq.com/Bambolim-Beach-Bambolim-Sightseeing-831-11230.html',
        'https://www.holidayiq.com/Siridao-Beach-Bambolim-Sightseeing-831-11231.html',
        'https://www.holidayiq.com/Vainguinim-Beach-Bambolim-Sightseeing-831-11232.html',
        'https://www.holidayiq.com/Marivel-Beach-Bambolim-Sightseeing-831-11236.html',
        'https://www.holidayiq.com/Velsao-Beach-Bambolim-Sightseeing-831-11248.html',
        'https://www.holidayiq.com/Arossim-Beach-Bambolim-Sightseeing-831-11249.html',
        'https://www.holidayiq.com/Bonda-Lake-Bambolim-Sightseeing-831-23913.html',
        'https://www.holidayiq.com/Vengurlas-Lighthouse-Vengurla-Sightseeing-701-12052.html',
        'https://www.holidayiq.com/Old-Vengurla-Port-Vengurla-Sightseeing-701-981.html',
        'https://www.holidayiq.com/Nivati-Beach-Vengurla-Sightseeing-701-12042.html',
        'https://www.holidayiq.com/Shiroda-Beach-Vengurla-Sightseeing-701-12049.html',
        'https://www.holidayiq.com/Mochemad-Beach-Vengurla-Sightseeing-701-12053.html',
        'https://www.holidayiq.com/Vayangani-Beach-Vengurla-Sightseeing-701-12056.html',
        'https://www.holidayiq.com/Khavane-Beach-Vengurla-Sightseeing-701-31943.html',
        'https://www.holidayiq.com/Madha-Beach-Vengurla-Sightseeing-701-31946.html',
        'https://www.holidayiq.com/Chandipur-Beach-Balasore-Sightseeing-1079-19029.html',
        'https://www.holidayiq.com/Chandbali-Balasore-Sightseeing-1079-8119.html',
        'https://www.holidayiq.com/Kharasahapur-Beach-Balasore-Sightseeing-1079-19031.html',
        'https://www.holidayiq.com/Talshari-Balasore-Sightseeing-1079-8127.html',
        'https://www.holidayiq.com/Dhamra-Balasore-Sightseeing-1079-8120.html',
        'https://www.holidayiq.com/Kashaphal-Beach-Balasore-Sightseeing-1079-19032.html',
        'https://www.holidayiq.com/Caranzalem-Beach-Caranzalem-Sightseeing-910-9296.html',
        'https://www.holidayiq.com/Vainguinim-Beach-Caranzalem-Sightseeing-910-9298.html',
        'https://www.holidayiq.com/Talashil-Beach-Malvan-Sightseeing-686-28903.html',
        'https://www.holidayiq.com/Akshi-Beach-Nagaon-Beach-Sightseeing-14850-13832.html',
        'https://www.holidayiq.com/Versoli-Beach-Nagaon-Beach-Sightseeing-14850-13826.html',
        'https://www.holidayiq.com/Brahma-Kund-Nagaon-Beach-Sightseeing-14850-13831.html',
        'https://www.holidayiq.com/Thal-Beach-Nagaon-Beach-Sightseeing-14850-13833.html',
        'https://www.holidayiq.com/Ashwem-Beach-Mapusa-Sightseeing-706-16372.html',
        'https://www.holidayiq.com/Malpe-Beach-Malpe-Sightseeing-450-13634.html',
        'https://www.holidayiq.com/St-Marys-Island-Malpe-Sightseeing-450-13633.html',
        'https://www.holidayiq.com/Bogmalo-Beach-Bogmalo-Sightseeing-315-11642.html',
        'https://www.holidayiq.com/Sernabatim-Beach-Bogmalo-Sightseeing-315-11653.html',
        'https://www.holidayiq.com/Colva-Beach-Bogmalo-Sightseeing-315-11652.html',
        'https://www.holidayiq.com/Siridao-Beach-Bogmalo-Sightseeing-315-11643.html',
        'https://www.holidayiq.com/Hansa-Beach-Bogmalo-Sightseeing-315-11646.html',
        'https://www.holidayiq.com/Hollant-Beach-Bogmalo-Sightseeing-315-11647.html',
        'https://www.holidayiq.com/Arossim-Beach-Bogmalo-Sightseeing-315-11655.html',
        'https://www.holidayiq.com/Cansaulim-Beach-Cansaulim-Sightseeing-907-9519.html',
        'https://www.holidayiq.com/Arossim-Beach-Cansaulim-Sightseeing-907-9521.html',
        'https://www.holidayiq.com/Mandrem-Beach-Mandrem-Sightseeing-908-15124.html',
        'https://www.holidayiq.com/Morjim-Beach-Mandrem-Sightseeing-908-15126.html',
        'https://www.holidayiq.com/Querim-Beach-Mandrem-Sightseeing-908-15129.html',
        'https://www.holidayiq.com/Calangute-Beach-Mandrem-Sightseeing-908-15137.html',
        'https://www.holidayiq.com/Maravanthe-Beach-Maravanthe-Sightseeing-720-783.html',
        'https://www.holidayiq.com/Kodi-Beach-Maravanthe-Sightseeing-720-14159.html',
        'https://www.holidayiq.com/Conco-Island-Agonda-Sightseeing-703-17611.html',
        'https://www.holidayiq.com/Cola-Beach-Agonda-Sightseeing-703-17607.html',
        'https://www.holidayiq.com/Galgibaga-Beach-Agonda-Sightseeing-703-17619.html',
        'https://www.holidayiq.com/Butterfly-Beach-Agonda-Sightseeing-703-17609.html',
        'https://www.holidayiq.com/Canaguinim-Beach-Agonda-Sightseeing-703-17616.html',
        'https://www.holidayiq.com/Rock-Formations-Agonda-Sightseeing-703-17620.html',
        'https://www.holidayiq.com/Tannirubhavi-Beach-Surathkal-Sightseeing-567-14671.html',
        'https://www.holidayiq.com/Hosabettu-Beach-Surathkal-Sightseeing-567-36778.html',
        'https://www.holidayiq.com/Hazira-Beach-Tithal-Sightseeing-737-31318.html',
        'https://www.holidayiq.com/Kihim-Beach-Kihim-Sightseeing-683-16406.html',
        'https://www.holidayiq.com/Marve-Beach-Madh-Marve-Sightseeing-606-14054.html',
        'https://www.holidayiq.com/Versova-Beach-Madh-Marve-Sightseeing-606-14055.html',
        'https://www.holidayiq.com/Silver-Beach-Cuddalore-Sightseeing-1140-11764.html',
        'https://www.holidayiq.com/Tarkarli-Beach-Sindhudurg-Sightseeing-695-16156.html',
        'https://www.holidayiq.com/Walaval-Creek-Sindhudurg-Sightseeing-695-16172.html',
        'https://www.holidayiq.com/Nivati-Beach-Sindhudurg-Sightseeing-695-16146.html',
        'https://www.holidayiq.com/Sargeshwar-Beach-Sindhudurg-Sightseeing-695-16147.html',
        'https://www.holidayiq.com/Vayangani-Beach-Sindhudurg-Sightseeing-695-16148.html',
        'https://www.holidayiq.com/Karli-Backwaters-Sindhudurg-Sightseeing-695-16154.html',
        'https://www.holidayiq.com/Kodikkarai-Beach-Nagapattinam-Sightseeing-630-19033.html',
        'https://www.holidayiq.com/Muzhappilangad-Beach-Coastal-Malabar-Sightseeing-600-9350.html',
        'https://www.holidayiq.com/Marari-Beach-Coastal-Malabar-Sightseeing-600-9352.html',
        'https://www.holidayiq.com/Beypore-Beach-Coastal-Malabar-Sightseeing-600-9348.html',
        'https://www.holidayiq.com/Ezhimala-Beach-Coastal-Malabar-Sightseeing-600-9353.html',
        'https://www.holidayiq.com/Moppila-Bay-Beach-Coastal-Malabar-Sightseeing-600-9354.html',
        'https://www.holidayiq.com/Kurumgad-Island-Devbagh-Sightseeing-1234-11808.html',
        'https://www.holidayiq.com/Tagore-Beach-Devbagh-Sightseeing-1234-11803.html',
        'https://www.holidayiq.com/Muzhappilangad-Beach-Thalassery-Sightseeing-997-15733.html',
        'https://www.holidayiq.com/Dharmadam-Thuruth-Thalassery-Sightseeing-997-15734.html',
        'https://www.holidayiq.com/Bangaram-Island-Bangaram-Sightseeing-1002-11256.html',
        'https://www.holidayiq.com/Arambol-Beach-Arambol-Sightseeing-702-285.html',
        'https://www.holidayiq.com/Querim-Beach-Arambol-Sightseeing-702-9084.html',
        'https://www.holidayiq.com/Harmal-Beach-Arambol-Sightseeing-702-23847.html',
        'https://www.holidayiq.com/Sweet-Lake-Beach-Arambol-Sightseeing-702-23857.html',
        'https://www.holidayiq.com/Paliem-Beach-Arambol-Sightseeing-702-23852.html',
        'https://www.holidayiq.com/Kalacha-Beach-Arambol-Sightseeing-702-9083.html',
        'https://www.holidayiq.com/Freshwater-Lake-Arambol-Sightseeing-702-284.html',
        'https://www.holidayiq.com/Arambol-Lake-Arambol-Sightseeing-702-23843.html',
        'https://www.holidayiq.com/Paliem-Lake-Arambol-Sightseeing-702-23853.html',
        'https://www.holidayiq.com/Manginapudi-Beach-Machilipatnam-Sightseeing-660-181.html',
        'https://www.holidayiq.com/Maginapudi-Beach-Bandar-Beach-Machilipatnam-Sightseeing-660-32173.html',
        'https://www.holidayiq.com/Velneshwar-Beach-Velneshwar-Sightseeing-700-11638.html',
        'https://www.holidayiq.com/Guhagar-Beach-Velneshwar-Sightseeing-700-11639.html',
        'https://www.holidayiq.com/Shastri-River-Velneshwar-Sightseeing-700-11636.html',
        'https://www.holidayiq.com/Covelong-Beach-Covelong-Sightseeing-341-9023.html',
        'https://www.holidayiq.com/Agatti-Kadmat-Sightseeing-1005-17800.html',
        'https://www.holidayiq.com/Bangaram-Kadmat-Sightseeing-1005-17804.html',
        'https://www.holidayiq.com/Kalpeni-Kadmat-Sightseeing-1005-17805.html',
        'https://www.holidayiq.com/Kappad-Beach-Kappad-Sightseeing-643-939.html',
        'https://www.holidayiq.com/Korapuzha-Kappad-Sightseeing-643-11537.html',
        'https://www.holidayiq.com/Pookot-Lake-Kappad-Sightseeing-643-11533.html',
        'https://www.holidayiq.com/Dana-Paani-Beach-Mumbai-Sightseeing-468-20154.html',
        'https://www.holidayiq.com/Bhogwe-Beach-Sindhudurg-Sightseeing-695-16168.html',
        'https://www.holidayiq.com/Redi-Beach-Sindhudurg-Sightseeing-695-16169.html',
        'https://www.holidayiq.com/Bagayat-Beach-Sindhudurg-Sightseeing-695-16170.html',
        'https://www.holidayiq.com/Kunkeshwar-Beach-Sindhudurg-Sightseeing-695-16171.html',
        'https://www.holidayiq.com/Nerurpar-Backwaters-Sindhudurg-Sightseeing-695-16173.html',
        'https://www.holidayiq.com/Tarakali-Backwaters-Sindhudurg-Sightseeing-695-16174.html',
        'https://www.holidayiq.com/Katwan-Backwaters-Sindhudurg-Sightseeing-695-16175.html',
        'https://www.holidayiq.com/Gahirmatha-Beach-Paradip-Sightseeing-1077-16350.html',
        'https://www.holidayiq.com/Bhatkal-Beach-Bhatkal-Sightseeing-713-17248.html',
        'https://www.holidayiq.com/Aksa-Beach-Madh-Island-Sightseeing-684-14048.html',
        'https://www.holidayiq.com/Versova-Beach-Madh-Island-Sightseeing-684-14050.html',
        'https://www.holidayiq.com/Marve-Beach-Madh-Island-Sightseeing-684-14049.html',
        'https://www.holidayiq.com/The-Beach-At-Mandvi-Palace-Mandvi-Sightseeing-733-28919.html',
        'https://www.holidayiq.com/Dhanushkodi-Beach-Dhanushkodi-Sightseeing-1236-19035.html',
        'https://www.holidayiq.com/Pamban-Island-Dhanushkodi-Sightseeing-1236-12050.html',
        'https://www.holidayiq.com/Ahmedpur-Mandvi-Beach-Ahmedpur-Mandvi-Sightseeing-732-10336.html',
        'https://www.holidayiq.com/Diu-Island-Ahmedpur-Mandvi-Sightseeing-732-10339.html',
        'https://www.holidayiq.com/Alappuzha-Beach-Mararikulam-Sightseeing-14842-13861.html',
        'https://www.holidayiq.com/Candolim-Beach-Sinquerim-Sightseeing-556-16894.html',
        'https://www.holidayiq.com/Sinquerim-Beach-Sinquerim-Sightseeing-556-16893.html',
        'https://www.holidayiq.com/Anjuna-Beach-Sinquerim-Sightseeing-556-16908.html',
        'https://www.holidayiq.com/Baga-Beach-Sinquerim-Sightseeing-556-16896.html',
        'https://www.holidayiq.com/Baga-River-Sinquerim-Sightseeing-556-16898.html',
        'https://www.holidayiq.com/Siridao-Beach-Sinquerim-Sightseeing-556-16912.html',
        'https://www.holidayiq.com/Vainguinim-Sinquerim-Sightseeing-556-16913.html',
        'https://www.holidayiq.com/Ozran-Beach-Sinquerim-Sightseeing-556-16919.html',
        'https://www.holidayiq.com/Utorda-Beach-Velsao-Sightseeing-909-12263.html',
        'https://www.holidayiq.com/Velsao-Beach-Velsao-Sightseeing-909-12258.html',
        'https://www.holidayiq.com/Majorda-Beach-Velsao-Sightseeing-909-12264.html',
        'https://www.holidayiq.com/Colva-Beach-Velsao-Sightseeing-909-12267.html',
        'https://www.holidayiq.com/Sunset-Beach-Velsao-Sightseeing-909-12265.html',
        'https://www.holidayiq.com/Erangal-Beach-Mumbai-Sightseeing-468-20171.html',
        'https://www.holidayiq.com/Udvada-Beach-Udvada-Sightseeing-1342-13948.html',
        'https://www.holidayiq.com/Chapora-Beach-Chapora-Sightseeing-327-8986.html',
        'https://www.holidayiq.com/Kalpeni-Beach-Kalpeni-Sightseeing-1006-17506.html',
        'https://www.holidayiq.com/Ross-Island-Ross-Island-Sightseeing-838-11843.html',
        'https://www.holidayiq.com/Neil-Island-Ross-Island-Sightseeing-838-11854.html',
        'https://www.holidayiq.com/Smith-Island-Ross-Island-Sightseeing-838-11852.html',
        'https://www.holidayiq.com/Viper-Island-Ross-Island-Sightseeing-838-11847.html',
        'https://www.holidayiq.com/Barren-Island-Ross-Island-Sightseeing-838-11853.html',
        'https://www.holidayiq.com/Harnai-Beach-Harnai-Sightseeing-1246-17675.html',
        'https://www.holidayiq.com/Dapoli-Beach-Harnai-Sightseeing-1246-17682.html',
        'https://www.holidayiq.com/Anjarle-Beach-Harnai-Sightseeing-1246-17673.html',
        'https://www.holidayiq.com/Burundi-Beach-Harnai-Sightseeing-1246-17674.html',
        'https://www.holidayiq.com/Palande-Beach-Harnai-Sightseeing-1246-17681.html',
        'https://www.holidayiq.com/Tara-Mumbai-Beach-Kunkeshwar-Sightseeing-1271-16431.html',
        'https://www.holidayiq.com/Kunkeshwar-Beach-Kunkeshwar-Sightseeing-1271-16426.html',
        'https://www.holidayiq.com/Devgad-Beach-Kunkeshwar-Sightseeing-1271-16429.html',
        'https://www.holidayiq.com/Mandwa-Beach-Mandwa-Sightseeing-687-13654.html',
        'https://www.holidayiq.com/Kihim-Beach-Mandwa-Sightseeing-687-13655.html',
        'https://www.holidayiq.com/Chandrabhaga-River-Chandrabhaga-Beach-Sightseeing-1073-10216.html',
        'https://www.holidayiq.com/Padinharekara-Beach-Ponnani-Sightseeing-995-17837.html',
        'https://www.holidayiq.com/Bharathapuzha-Ponnani-Sightseeing-995-17840.html',
        'https://www.holidayiq.com/Biyyam-Kayal-Backwater-Ponnani-Sightseeing-995-30670.html',
        'https://www.holidayiq.com/Ponnani-Beach-Ponnani-Sightseeing-995-30674.html',
        'https://www.holidayiq.com/Ponnani-Fishing-Centre-Ponnani-Sightseeing-995-30675.html',
        'https://www.holidayiq.com/Kavaratti-Island-Kavaratti-Sightseeing-1007-27618.html',
        'https://www.holidayiq.com/Agatti-Island-Kavaratti-Sightseeing-1007-12582.html',
        'https://www.holidayiq.com/Mandrem-Beach-Sinquerim-Sightseeing-556-16931.html',
        'https://www.holidayiq.com/Harmal-Beach-Sinquerim-Sightseeing-556-16932.html',
        'https://www.holidayiq.com/Minicoy-Island-Minicoy-Sightseeing-1009-14583.html',
        'https://www.holidayiq.com/Kaddipuram-Beach-Kodungallur-Sightseeing-1267-15785.html',
        'https://www.holidayiq.com/Redi-Beach-Redi-Sightseeing-1303-18553.html',
        'https://www.holidayiq.com/Mahabalipuram-Beach-Muttukadu-Sightseeing-14843-15911.html',
        'https://www.holidayiq.com/Chorwad-Beach-Chorwad-Sightseeing-731-9020.html',
        'https://www.holidayiq.com/Veraval-Beach-Chorwad-Sightseeing-731-9021.html',
        'https://www.holidayiq.com/Divar-Island-Chorao-Sightseeing-834-11753.html',
        'https://www.holidayiq.com/Havelock-Island-Viper-Island-Sightseeing-839-13022.html',
        'https://www.holidayiq.com/Viper-Island-Viper-Island-Sightseeing-839-13009.html',
        'https://www.holidayiq.com/Smith-Island-Viper-Island-Sightseeing-839-13019.html',
        'https://www.holidayiq.com/Barren-Island-Viper-Island-Sightseeing-839-13020.html',
        'https://www.holidayiq.com/Neil-Island-Viper-Island-Sightseeing-839-13021.html',
        'https://www.holidayiq.com/Middle-Ground-Island-Mumbai-Sightseeing-468-20273.html'



         

    ]

    #def start_requests(self):
    #    url= 'https://www.holidayiq.com/Rohtang-Pass-Manali-Sightseeing-451-8189.html'
    #    #url= 'https://www.holidayiq.com/page/Rohtang-Pass-Manali-Sightseeing-451-8189-p2.html'
        
    #    yield scrapy.Request(url=url, callback=self.parse)


    #Response
    def parse(self, response):
        for review in response.selector.xpath("//div[@class='col-xs-12 col-sm-9 col-md-9 col-lg-9 int-no-padding']"):
            
            yield {
                'Place': review.xpath(".//div[@class='link-menu-a']/a/text()[1]").extract_first(),              
                'Attraction': review.xpath(".//h1[@class='h1-tag attrOverviewHeading']/span/text()[1]").extract(),                
                'Description': review.xpath(".//div[@class='int-read-more-pera']//text()").extract()
                        
            }