from backend.api.catalog.models.catalog_model import Catalog
from backend.api.catalog.mapper.catalog_SQL import search_book_class



def create_catalog_id(book_class):
    #假设每种书有两个书架
    #每个书架有五层
    #每层可以放20本书
    count = len(search_book_class(book_class))+1
    if count//100 > 1:
        return "0"
    else:
        catalog_id = book_class + '-' + str(count//100+1) + '-' + str((count//20)%5) + '-' + str(count%20)
        return catalog_id