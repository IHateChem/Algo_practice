from  bisect import bisect_left as bl
db = {"cpp":  {}, "java":{}, "python":{}}
def solution(info, query):
    for lang in ("cpp", "java", "python"):
        for pos in ("backend", "frontend"):
            if pos not in db[lang]:
                db[lang][pos] = {}
            for career in ("junior", "senior"):
                if career not in db[lang][pos]:
                    db[lang][pos][career] = {}
                for food in ("chicken", "pizza"):
                    if food not in db[lang][pos][career]:
                        db[lang][pos][career][food] = []
    for personal_info in info:
        t = db
        for param in personal_info.split():
            if param.isnumeric():
                t.append(int(param))
            else:
                t = t[param]
    for lang in ("cpp", "java", "python"):
        for pos in ("backend", "frontend"):
            for career in ("junior", "senior"):
                for food in ("chicken", "pizza"):
                    db[lang][pos][career][food].sort()
    answer = []
    for q in query:
        t = 0
        dbs = [db]
        for param in q.split():
            if param == "and": continue
            next_db = []
            if not param.isnumeric():
                if param == "-":
                    for tdb in dbs:
                        for v in tdb.values():
                            next_db.append(v)
                else:
                    for tdb in dbs:
                        next_db.append(tdb[param])
            else:
                for tdb in dbs:
                    t += len(tdb) - bl(tdb, int(param))
            dbs = next_db
        answer.append(t)
                    
            
        
    return answer