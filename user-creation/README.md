# Scripts for automating creation of Users

From https://developer.okta.com/docs/reference/api/users/#create-user-with-password

Request URL:
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
