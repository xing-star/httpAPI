#!/usr/bin/env python

import httplib

#connect
getConn = httplib.HTTPConnection("127.0.0.1:5000")
postConn = httplib.HTTPConnection("127.0.0.1:5000")
deleteConn = httplib.HTTPConnection("127.0.0.1:5000")
putConn = httplib.HTTPConnection("127.0.0.1:5000")

#request
getConn.request("GET", "/httpAPI")
postConn.request("POST", "/httpAPI")
deleteConn.request("DELETE", "/httpAPI")
putConn.request("PUT", "/httpAPI")

#response
get = getConn.getresponse()
post = postConn.getresponse()
delete = deleteConn.getresponse()
put = putConn.getresponse()

#output
print get.status, get.reason
print get.read()
print '-------------'
print post.status, post.reason
print post.read()
print '-------------'
print delete.status, delete.reason
print delete.read()
print '-------------'
print put.status, put.reason
print put.read()
print '-------------'

#close
getConn.close()
postConn.close()
deleteConn.close()
putConn.close()
