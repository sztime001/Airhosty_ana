# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:57:45 2018

@author: Sofei
"""

import base64
import http.client
import json
import sys


class Client(object):
    def __init__(self, clientId, clientSecret,
                 papiHostname="ws.homeaway.com",
                 oauthHostname="ws.homeaway.com",
                 platformSite="https://www.homeaway.com/platform"):
        self.clientId = clientId
        self.clientSecret = clientSecret
        self.papiHostname = papiHostname
        self.oauthHostname = oauthHostname
        self.platformSite = platformSite
        self.creds = base64.b64encode("{}:{}".format(self.clientId, self.clientSecret).encode("utf-8")).decode("utf-8")
        self.token = self.getToken()

    def getToken(self, ticket=None):
        conn = http.client.HTTPSConnection(self.oauthHostname)
        path = "/oauth/token?_restfully=true&credentials={}".format(self.creds)
        if ticket is not None:
            path += "&ticket={}".format(ticket)
        conn.request("GET", path)
        body = json.loads(conn.getresponse().read().decode("utf-8"))
        return body['value']

    def getAuthUrl(self):
        return "{}/grantAccess?id={}".format(self.platformSite, self.clientId)

    def listing(self, id, q=None):
        return self.get("/public/listing", {"id": id, "q": q})

    def bookStay(self, listingId, unitId, arrivalDate, departureDate, adultsCount,
                 childrenCount=None, petIncluded=None):
        query = {"listingId": listingId, "unitId": unitId,
                 "arrivalDate": arrivalDate, "departureDate": departureDate,
                 "adultsCount": adultsCount}
        if childrenCount is not None: query["childrenCount"] = childrenCount
        if petIncluded is not None: query["petIncluded"] = petIncluded
        return self.get("/public/bookStay", query)

    def listingReviews(self, listingId, unitId,
                       page=None, pageSize=None):
        query = {"listingId": listingId, "unitId" : unitId}
        if page is not None: query["page"] = page
        if pageSize is not None: query["pageSize"] = pageSize
        return self.get("/public/listingReviews", query)

    def me(self, token):
        return self.get("/public/me", {}, token=token)

    def myListings(self, token, page=None, pageSize=None):
        query = {}
        if page is not None: query["page"] = page
        if pageSize is not None: query["pageSize"] = pageSize
        return self.get("/public/myListings", query, token=token)

    def myListingReservations(self, token, listingId, page=None, pageSize=None):
        query = {"listingId": listingId}
        if page is not None: query["page"] = page
        if pageSize is not None: query["pageSize"] = pageSize
        return self.get("/public/myListingReservations", query, token=token)

    def search(self, q,
               page=None, pageSize=None,
               availabilityStart=None, availabilityEnd=None,
               minBedrooms=None, maxBedrooms=None,
               minBathrooms=None, maxBathrooms=None,
               minSleeps=None, maxSleeps=None,
               minPrice=None, maxPrice=None,
               refine=None, sort=None,
               imageSize=None, locale=None):
        query = {"q": q}
        if page is not None: query["page"] = page
        if pageSize is not None: query["pageSize"] = pageSize
        if availabilityStart is not None: query["availabilityStart"] = availabilityStart
        if availabilityEnd is not None: query["availabilityEnd"] = availabilityEnd
        if minBedrooms is not None: query["minBedrooms"] = minBedrooms
        if maxBedrooms is not None: query["maxBedrooms"] = maxBedrooms
        if minBathrooms is not None: query["minBathrooms"] = minBathrooms
        if maxBathrooms is not None: query["maxBathrooms"] = maxBathrooms
        if minSleeps is not None: query["minSleeps"] = minSleeps
        if maxSleeps is not None: query["maxSleeps"] = maxSleeps
        if minPrice is not None: query["minPrice"] = minPrice
        if maxPrice is not None: query["maxPrice"] = maxPrice
        if refine is not None: query["refine"] = refine
        if sort is not None: query["sort"] = sort
        if imageSize is not None: query["imageSize"] = imageSize
        if locale is not None: query["locale"] = locale
        return self.get("/public/search", query)

    def submitReview(self, review):
        data = json.dumps(review)
        return self.post("/public/submitReview", body=data)

    def httpRequest(self, method, path, query, body=None, token=None):
        conn = http.client.HTTPSConnection(self.papiHostname)
        apply = lambda f, a: list(map(f, a)) if isinstance(a, list) else [f(a)]
        url = "?".join([path] if query is None else
                       [path, "&".join(
                           list(map(
                               lambda t: "&".join(
                                   apply(lambda v: "{}={}".format(t[0], v), t[1])),
                               list(query.items()))))])
        conn.request(method, url,
                     headers={"Authorization": "Bearer {}".format(self.token if token is None else token)},
                     body=body)
        response_body = conn.getresponse().read().decode("utf-8")
        return json.loads(response_body)

    def get(self, path, query=None, token=None):
        return self.httpRequest("GET", path, query, token=token)

    def post(self, path, query=None, body=None, token=None):
        return self.httpRequest("POST", path, query, body=body, token=token)