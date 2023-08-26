from lxml import etree
import json
import xmltodict

#Маємо такий словник:
test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}

# Завдання XML:
#     Завдання 1: Збереження словника у форматі XML: Конвертуйте словник у формат XML та збережіть його у файл з розширенням ".xml".

root = etree.Element("root")
for key in test_dict:
    #print(key) # user1 / user2
    user = etree.Element(key)
    elem = test_dict[key]
    for attr in elem:
        #print(attr + ' = ' + str(elem[attr]))
        user.set(attr, str(elem[attr]))
    root.append(user)

with open('dict_file.xml', 'w+') as file:
    file.write(etree.tostring(root, pretty_print=True).decode('utf-8'))

#     Завдання 2: Читання XML-файлу: Відкрийте XML-файл та розпарсіть його, щоб отримати знову словник Python як оригінал.
parsed_dict = {}
parsed_xml = etree.parse('dict_file.xml')
root = parsed_xml.getroot()
for element in root:
    user = {}
    for att in element.attrib:
        user[att] = element.attrib[att]
    parsed_dict[element.tag] = user

#print(parsed_dict)

# Завдання JSON:
#     Завдання 3: Збереження словника у форматі JSON: Конвертуйте словник у формат JSON та збережіть його у файл з розширенням ".json".
json_data = json.dumps(test_dict)
# print(test_dict)
# print(json_data)
with open('dict_data.json', 'w') as file:
    file.write(json_data)
#     Завдання 4: Читання JSON-файлу: Відкрийте JSON-файл та завантажте його дані у Python як словник.
with open('dict_data.json', 'r') as file:
    data = json.loads(file.read())
    # print(data)

# Завдання XML та JSON (бонус):
#     Завдання 5: Конвертація з XML до JSON: Завантажте XML-файл, розпарсіть його та конвертуйте у формат JSON. Потім збережіть в файл.
with open("dict_file.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read(), attr_prefix="")

json_data = json.dumps(data_dict)

with open("data.json", "w") as json_file:
    json_file.write(json_data)
