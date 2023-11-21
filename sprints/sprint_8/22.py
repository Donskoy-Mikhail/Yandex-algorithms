from lxml import etree

def generate_xsd_schema(xml_element, parent_element=None):
    if len(xml_element) == 0:
        xsd_element = etree.Element('xsd:element', name=xml_element.tag)
        xsd_complex_type = etree.Element('xsd:complexType')
        xsd_attributes = etree.Element('xsd:complexType')

        for attribute, value in xml_element.attrib.items():
            xsd_attribute = etree.Element('xs:attribute', name=attribute, type=f'xs:{value}')
            xsd_attributes.append(xsd_attribute)

        xsd_complex_type.append(xsd_attributes)
        xsd_element.append(xsd_complex_type)

        if parent_element is not None:
            parent_element.append(xsd_element)
    else:
        if xml_element.tag not in xsd_element_dict:
            xsd_complex_type = etree.Element('xsd:complexType')
            sequence = etree.Element('xsd:sequence')

            for child in xml_element:
                generate_xsd_schema(child, sequence)

            xsd_complex_type.append(sequence)
            xsd_element_dict[xml_element.tag] = xsd_complex_type

        xsd_element = etree.Element('xsd:element', name=xml_element.tag, ref=xml_element.tag, minoccurs="0", maxoccurs="unbounded")

        if parent_element is not None:
            parent_element.append(xsd_element)

xsd_element_dict = {}

# Прочитаем XML из примера 1
xml_string = '''
<default_check>
	<decision final_decision="Decline" score="0.85" date_decison="2023-10-01">
    </decision>
	<federal>
	 <data mau="rdgrdh">
     </data>
	 <data mau="rdgrdh">
     </data>
	</federal>
</default_check>
'''

root = etree.fromstring(xml_string)

# Создадим корневой элемент XSD схемы
xsd_schema = etree.Element('element', name='default_check')

# Генерируем XSD схему
generate_xsd_schema(root, xsd_schema)

# Выводим XSD схему в виде строки
xsd_schema_string = etree.tostring(xsd_schema, pretty_print=True, encoding='utf-8').decode()
xsd_schema_string = f'<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">{xsd_schema_string}</xsd:schema>'
print(xsd_schema_string)
