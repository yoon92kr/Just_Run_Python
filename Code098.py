from urllib import request
from urllib import parse

url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
key = 'w93pEOT4y4redDKZxIwjdNDn3veFRdEsEhhTl9NbOeCKMCw68UKjq2f0TO%2FNmSNLwD6njsejjM7ZmemsFej3Og%3D%3D'
params = f'?{parse.quote_plus("srviceKey")}={key}&'+parse.urlencode({
    parse.quote_plus()
})

