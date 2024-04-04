from __init__ import collection,index_path,alert_now



    

    




def alert_show()->dict:
    if alert_now:
        return alert_now
    return None