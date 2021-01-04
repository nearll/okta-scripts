# Scripts for automating creation of Users

You execute the script by running:
`python3 user_create.py`

The script will ask you for how many members you want to create payloads for.
_Note: Since all we are doing is creating a data file their is no input
validation, use at your own risk._

From https://developer.okta.com/docs/reference/api/users/#create-user-with-password

Request example with curl:
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

We will be using Postman to automate the creation of the members, you can find
the link for importing Okta's Postman collection at the link above. To format
the json properly to create bulk members we will create a file with the
following format:

```
[
  {
    "profile": {
      "firstName": "Deckard", 
      "lastName": "Johnson", 
      "email": "DeckardJohnson@gmail.com", 
      "login": "DeckardJohnson@gmail.com", 
      "mobilePhone": "231-313-1313"
    }, 
      "credentials": {
        "password": {
          "value":"0ed4e644a72d404fbcabe35718d7db94"
      }
    }
  },
    "profile": {
      "firstName": "Deckard", 
      "lastName": "Johnson", 
      "email": "DeckardJohnson@gmail.com", 
      "login": "DeckardJohnson@gmail.com", 
      "mobilePhone": "231-313-1313"
    }, 
      "credentials": {
        "password": {
          "value":"0ed4e644a72d404fbcabe35718d7db94"
      }
    }
 ]
```

Instructions for automating input data with Postman API calls can be found at:
https://learning.postman.com/docs/running-collections/working-with-data-files/

The script will also output a file in the following format to allow you to
later login to your member:
```
[
  {
    "password": "0ed4e644a72d404fbcabe35718d7db94",
    "username":"DeckardJohnson@gmail.com"
  },
  {
    "password": "79d5c93329194e699d814c24908f3939",
    "username": "NickShaffer@gmail.com"}
  }
]
```
