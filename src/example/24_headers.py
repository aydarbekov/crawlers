def extractdata(context, data):
    # This stage comes after 'fetch' so the 'data' input contains an
    # HTTPResponse object.
    response = context.http.rehash(data)
    url = response.url
    page = response.html

    # Parse the rest of the page to extract structured data.

    header = _gettext(page.xpath('.//h1/text()'))
    autor = _gettext(page.xpath('.//header/div/div/a/text()'))
    foto = _gettext(page.xpath('.//div[@class="stk-mask"]/img/@src'))
    text = _gettext(page.xpath('.//p'))
	
    article_data = {
		"url": response.url,
		"autor": autor,
		"header": header,
		"foto": foto,
		"text": text
	}

    if article_data["header"] is not None:
        # If 'rule' is not set, it defaults to 'pass', which triggers the
        # final 'store' stage.
        context.emit(data=article_data)

def _gettext(list):
    if not list:
        return list
    else:
        return list[0].strip()