def dateToday(date):
    year, month, day = map(int, date.split("."))
    return int((year * 12 * 28) + (month * 28) + day)
    
def solution(today, terms, privacies):
    terms_val = dict()
    answer = []
    
    for var in terms:
        a, b = var.split(' ')
        b = int(b)
        terms_val[a] = b
        
    for index, val in enumerate(privacies):
        d, v = val.split(' ')
        priv_date = dateToday(d)
        priv_var_val = terms_val[v]
        
        if priv_date + priv_var_val*28 <= dateToday(today):
            answer.append(index+1)
        
    
    return answer