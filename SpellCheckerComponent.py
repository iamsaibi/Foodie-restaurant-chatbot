from rasa.nlu.components import Component
from rasa.shared.nlu.training_data.message import Message
from nltk.metrics import edit_distance
from nltk.tokenize import word_tokenize
from string import punctuation

Cities = [
'Ahmedabad',
'Bengaluru',
'Chennai',
'Delhi',
'Hyderabad',
'Kolkata',
'Mumbai',
'Pune',
'Agra',
'Ajmer',
'Aligarh',
'Amravati',
'Amritsar',
'Asansol',
'Aurangabad',
'Bareilly',
'Belgaum',
'Bhavnagar',
'Bhiwandi',
'Bhopal',
'Bhubaneswar',
'Bikaner',
'Bilaspur',
'Bokaro Steel City',
'Chandigarh',
'Coimbatore',
'Cuttack',
'Dehradun',
'Dhanbad',
'Bhilai',
'Durgapur',
'Dindigul',
'Erode',
'Faridabad',
'Firozabad',
'Ghaziabad',
'Gorakhpur',
'Gulbarga',
'Guntur',
'Gwalior',
'Gurgaon',
'Guwahati',
'Hamirpur',
'Hubli',
'Indore',
'Jabalpur',
'Jaipur',
'Jalandhar',
'Jammu',
'Jamnagar',
'Jamshedpur',
'Jhansi',
'Jodhpur',
'Kakinada',
'Kannur',
'Kanpur',
'Karnal',
'Kochi',
'Kolhapur',
'Kollam',
'Kozhikode',
'Kurnool',
'Ludhiana',
'Lucknow',
'Madurai',
'Malappuram',
'Mathura',
'Mangalore',
'Meerut',
'Moradabad',
'Mysore',
'Nagpur',
'Nanded',
'Nashik',
'Nellore',
'Noida',
'Patna',
'Pondicherry',
'Purulia',
'Prayagraj',
'Raipur',
'Rajkot',
'Rajahmundry',
'Ranchi',
'Rourkela',
'Rishikesh',
'Ratlam',
'Salem',
'Sangli',
'Shimla',
'Siliguri',
'Solapur',
'Srinagar',
'Surat',
'Thanjavur',
'Thiruvananthapuram',
'Thrissur',
'Tiruchirappalli',
'Tirunelveli',
'Tiruvannamalai',
'Ujjain',
'Bijapur',
'Vadodara',
'Varanasi',
'Vijayawada',
'Visakhapatnam',
'Vellore',
'Warangal'
]
Dishes = [
    'Paneer','Do','Pyaza', 'Handwi','Kadhai','butter','Mutter','Lababdaar','Amritsari',
    'Chhole','Kulche', 'Potato','Spring','Roll','Fried','Rice','Schezwan','Rice', 'Custard','Bhature',
    'Rajma','Chawal','Rasgulla','Gulab','Jamun','Pastry','Chocolate','Pastry','Mud','cake','Red','velvet', 'cake',
    'Spicy','Mexican','Burger','Aloo','Patty','california','Marghareeta','Cheese','Burst',
    'Maggie','Rolls','Shwarma', 'Dum','biryani','Cutlet','Pasta','Alfredo','Arrabaita',
    'Coleslaw','Pizza','Cheese','Corn','double','decker','sandwich','Peppy','Farmhouse',
    'Uttapam','Pani Puri','Dahi Puri','Chat','Khandwi','fish',
    'Dosa','Rasam','Medu','Wada','Hakka','Noodles','Mutton','Kabaab','Veg','Seekh',
    'Pav','Bhaji', 'Risotto','Pesto','Kachori','Methi','malai','matar','Aloo','Gobhi','Kofta',
    'Biryani', 'Dhokla','Fafda','Khaman','Crispy','Corn','Biryani','Red','Salsa','Burrito','Bowl',
    'Masala','Dosa','Beacon','Chicken','Roasted','Chicken','French','fries','Potato','Twister',
    'Wada','Sambhar','Fried Idli','Manchurian','Tacos','Kaju','Curry',
    'Idli','Appam','Naan','Chana', 'Daal','Makhni','Tikka','Salad','Gajar','Halwa','Samosa'
]
known_words = []
known_words.extend(Dishes)
known_words.extend(Cities)
known_words = [word.strip().lower() for word in known_words]

class CorrectSpelling(Component):

    name = "Spell_checker"
    provides = ["message"]
    requires = ["message"]
    language_list = ["en"]

    def __init__(self, component_config=None):
        self.phonetics = []
        for word in known_words:
            self.phonetics.append(self._phonetic(word))
        super(CorrectSpelling, self).__init__(component_config)

    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass

    def _phonetic(self, word: str):
        word = word.lower().strip()

        hash = word[0]

        replacement_map = {'a':'','b':'1','c':'2','d':'3','e':'','f':'1','g':'2','h':'','i':'','j':'2','k':'2','l':'4','m':'5','n':'5','o':'','p':'1','q':'2','r':'6',
            's':'2','t':'3','u':'','v':'1','w':'','x':'2','y':'','z':'2', ' ':' '}

        for letter in word[1:]:
            if hash[-1] != replacement_map[letter]:
                hash+=replacement_map[letter]

        hash = hash[:4].ljust(4, '0')
        return hash

    def process(self, message, **kwargs):
        """Retrieve the text message, do spelling correction word by word,
        then append all the words and form the sentence,
        pass it to next component of pipeline"""
        
        text = message.get('text')
        if not text:
            return message

        tokens = word_tokenize(text)
        rectified_tokens = []
        for token in tokens:
            if token.strip().lower() not in known_words and token.strip().lower() not in punctuation:
                correct_word_found = False
                for idx, word in enumerate(known_words):
                    d = edit_distance(token.strip().lower(), word) 
                    if d <= 2 and self.phonetics[idx] == self._phonetic(token):
                        correct_word_found = True
                        break
                if correct_word_found:
                    rectified_tokens.append(word)
                else:
                    rectified_tokens.append(token)
            else:
                rectified_tokens.append(token)
        
        message.set('text', ' '.join(rectified_tokens))
        
        return message

    def persist(self,file_name, model_dir):
        """Pass because a pre-trained model is already persisted"""
        pass