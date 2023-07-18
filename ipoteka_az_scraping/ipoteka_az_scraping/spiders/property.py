import scrapy


class PropertyLinkSpider(scrapy.Spider):
    name = "property"
    allowed_domains = ["ipoteka.az"]
    start_urls = ["https://ipoteka.az/elan/69465-satilir-buzovna-qesebesi"]

    def parse(self, response):
        user_name = response.xpath('//div[@class="user"]/text()').get()
        phone_number = response.xpath('//div[@class="showNumber active"]/text()').get()
        announcement_id = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Elan İD")]/following-sibling::div[1]/text()').get()
        update_date = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Yeniləndi")]/following-sibling::div[1]/text()').get()
        baxis_sayi = response.xpath(
            '//div[@class="stats"]//div[contains(text(), "Baxış sayı")]/following-sibling::div[1]/text()').get()
        area = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Ümumi sahə")]/following-sibling::div[1]/text()').get()
        flat = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Mərtəbə")]/following-sibling::div[1]/text()').get()
        room_count = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Otaq sayı")]/following-sibling::div[1]/text()').get()
        document_type = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Sənədin tipi")]/following-sibling::div[1]/text()').get()
        repair_type = response.xpath(
            '//div[@class="params_block"]//div[@class="rw"]/div[contains(text(), "Təmir")]/following-sibling::div[1]/text()').get()
        yield {
            "user_name": user_name,
            "phone_number": phone_number,
            "announcement_id": announcement_id,
            "update_date": update_date,
            "baxis_sayi": baxis_sayi,
            "area": area,
            "flat": flat,
            "room_count": room_count,
            "document_type": document_type,
            "repair_type": repair_type
        }
