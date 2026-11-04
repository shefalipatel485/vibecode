# HomeServe Security Checklist

Mark each item only after performing and recording the check.

## Authentication and identity
- [ ] Passwords are stored only as strong salted hashes.
- [ ] JWT signing key is randomly generated, private, and supplied through environment variables.
- [ ] Token expiry and invalid-token behavior are tested.
- [ ] Registration prevents duplicate email/mobile values.
- [ ] Admin account credentials are changed and not shared.
- [ ] Account activation/deactivation is enforced.

## Authorization and data ownership
- [ ] Each role can access only its permitted endpoints.
- [ ] Customers can access only their own addresses, bookings, payments, reviews and complaints.
- [ ] Providers can access only their own provider records and assigned bookings.
- [ ] Technician access is restricted to assigned work.
- [ ] Admin-only operations reject non-admin users.
- [ ] Object-level authorization is tested for guessed IDs.

## Application and infrastructure
- [ ] HTTPS is enabled in deployed environments.
- [ ] CORS allows only the real frontend domain.
- [ ] Secrets and `.env` are excluded from Git.
- [ ] Database user has least-privilege permissions.
- [ ] Database backups and restore procedure are tested.
- [ ] Dependencies are reviewed and updated.
- [ ] Request size limits, rate limits and abuse protection are configured.
- [ ] Errors do not expose stack traces, credentials or sensitive data.
- [ ] Logs avoid passwords, tokens and payment secrets.

## Payments and uploads
- [ ] Razorpay signature verification is implemented server-side before marking a payment successful.
- [ ] Payment webhook idempotency is implemented.
- [ ] Payment amounts are calculated server-side and never trusted from frontend input.
- [ ] Cloudinary upload restrictions validate type, size and ownership.
- [ ] Uploaded files are not trusted as executable content.

## Release decision
Do not mark this checklist complete until every applicable item is verified. The supplied starter includes basic JWT/password hashing, but it is not a completed security audit. Payment gateway and upload security are not yet implemented.
