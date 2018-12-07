def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.
    
    
    
    for i in range(len(page.xpath('//tbody/tr'))):
        id_street = _gettext(page.xpath('//tbody/tr['+str(i)+']/td[2]/text()'))
        street_kg = _gettext(page.xpath('//tbody/tr['+str(i)+']/td[3]/div/p/text()'))
        
        print("----------------PRINTING ORG_DATA----------------")
        print(org_data)
        
    org_data = {
            "id_street": id_street,
            "street_kg": street_kg
    }
    context.emit(data=org_data)
    
   
def clean_dict(data):
    result = {}
    for key, value in data.items():
        if value is None or value=='' or value ==[]:
            value = '__'
            result[key] = value
        else:
            result[key] = data[key]
    return result    
    
def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()