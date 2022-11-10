import requests

def get_profesores():
    url = 'http://consultas.cuc.edu.co/api/v1.0/profesores'
    acces_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InBydWViYTIwMjJAY3VjLmVkdS5jbyIsImV4cCI6MTY0OTQ1MzA1NCwiY29ycmVvIjoicHJ1ZWJhMjAyMkBjdWMuZWR1LmNvIn0.MAoFJE2SBgHvp9BS9fyBmb2gZzD0BHGPiyKoAo_uYAQ'

    result = requests.get(
        url, headers={'Authorization': 'JWT %s' % acces_token})
    profesores = result.json()
    profesores_list = []
    for i in range(len(profesores)):
        profesores_list.append(profesores[i])

    return profesores_list
