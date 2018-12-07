def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.
    
    
    for i in range(len('tree.xpath(//tbody/tr)')):
        id = _gettext(tree.xpath('//tbody/tr/td[2]'))
        street_kg = _gettext(tree.xpath('//tbody/tr/td[3]'))
        
    
    org_data = {
        "id": id
        "street_kg": street_kg
    }
    print("----------------PRINTING ORG_DATA----------------")
    print(org_data)

    result['street_kg'] = street_kg
        contecst.emit(data=org_data)


def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
        