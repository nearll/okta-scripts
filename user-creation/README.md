# Scripts for automating creation of Users

From https://developer.okta.com/docs/reference/api/users/#create-user-with-password

Request example:
```
curl -v -X POST \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "Authorization: SSWS ${api_token}" \
-d '{
  "profile": {
      "firstName": "Isaac",
      "lastName": "Brock",
      "email": "isaac.brock@example.com",
      "login": "isaac.brock@example.com",
      "mobilePhone": "555-415-1337"
    },
  "credentials": {
      "password" : { "value": "tlpWENT2m" }
    }
}'"https://${yourOktaDomain}/api/v1/users?activate=true"
```

Response example:
```
{
  "id": "00ub0oNGTSWTBKOLGLNR",
  "status": "STAGED",
  "created": "2013-07-02T21:36:25.344Z",
  "activated": null,
  "statusChanged": null,
  "lastLogin": null,
  "lastUpdated": "2013-07-02T21:36:25.344Z",
  "passwordChanged": "2013-07-02T21:36:25.344Z",
  "profile": {
    "firstName": "Isaac",
    "lastName": "Brock",
    "email": "isaac.brock@example.com",
    "login": "isaac.brock@example.com",
    "mobilePhone": "555-415-1337"
  },
  "credentials": {
    "password": {},
    "provider": {
      "type": "OKTA",
      "name": "OKTA"
    }
  },
  "_links": {
    "activate": {
      "href": "https://${yourOktaDomain}/api/v1/users/00ub0oNGTSWTBKOLGLNR/lifecycle/activate"
    },
    "self": {
      "href": "https://${yourOktaDomain}/api/v1/users/00ub0oNGTSWTBKOLGLNR"
    }
  }
}
```
