import urllib
import urllib2
import re;

params = {'param1': 'value1'}

req = urllib2.Request("http://www.ryanair.com", urllib.urlencode(params))
res = urllib2.urlopen(req)

data = res.read();



print("aaa.");
print(type(data));
print("baseUrl" in data);
[m.start() for m in re.finditer('baseUrl', data)]
#print(data);
counter = 0;
#if data.find("baseUrl"): counter=counter+1;
#print data.find("window.addEventListener('load', shares, false);");
#print counter;
#myConnection = httplib.HTTPConnection('http://www.example.com');
#myConnection.