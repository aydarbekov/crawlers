def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    street_kg = _gettext(page.xpath('//tbody/tr/td[4]/div/p/text'))
    
    org_data = {
        "street_kg": street_kg,
    }
    print("----------------PRINTING ORG_DATA----------------")
    print(org_data)

    


def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()
        