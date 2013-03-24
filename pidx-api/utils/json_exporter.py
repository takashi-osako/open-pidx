'''
Created on Mar 19, 2013

@author: tosako
'''
from entity.Receipt import parse

def xml_to_json(xml_file):
    obj = parse(xml_file)
    return export(xml_obj=obj)

def export(xml_obj=None, parent_element_name=None):
    xml_dict = {}
    if xml_obj is None:
        return None
    member_data_items_ = xml_obj.member_data_items_
    for current_element_name in member_data_items_.keys():
        member_obj = member_data_items_[current_element_name]
        data_type = member_obj.get_data_type()
        container = member_obj.get_container()
        if container == 1:
            obj = getattr(xml_obj, current_element_name)
            if len(obj) > 0:
                new_dict = {current_element_name: obj}
                xml_dict = dict(xml_dict.items() + new_dict.items())
        elif data_type == 'string':
            obj = getattr(xml_obj, current_element_name)
            if obj is not None:
                new_dict = {current_element_name: obj}
                xml_dict = dict(xml_dict.items() + new_dict.items())
        elif data_type == 'dateTime':
            obj = getattr(xml_obj, current_element_name)
            if obj is not None:
                new_dict = {current_element_name: obj.strftime("%Y-%m-%d %H:%M:%S")}
                xml_dict = dict(xml_dict.items() + new_dict.items())
        else:
            returned_dict = export(xml_obj=getattr(xml_obj, current_element_name), parent_element_name=current_element_name)
            if returned_dict is not None:
                xml_dict = dict(xml_dict.items() + returned_dict.items())
    if parent_element_name is None:
        return xml_dict
    return {parent_element_name: xml_dict}
