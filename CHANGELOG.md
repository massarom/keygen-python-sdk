## v0.3.1 (2025-02-18)

### Fix

- properly pass 'relationships' to Token from API

## v0.3.0 (2025-01-10)

### BREAKING CHANGE

- Previously, creating a user would return the raw JSON
response. Now a `User` object is returned instead.
- The returned Entitlements from a License object are now
objects, not raw JSON

### Feat

- **functional**: newly created users are returned as object
- **models**: return Entitlement objects from License property
- **functional**: add function to get a user from its ID
- **functional**: add token parameter to all functions to bypass config

### Fix

- **models**: use correct type when creating user licenses objects

## v0.2.0 (2025-01-10)

### Feat

- add licenses property to User model

## v0.1.0 (2025-01-07)
