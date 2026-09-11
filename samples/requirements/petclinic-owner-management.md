Synthetic Owner Management Requirements

These requirements are team-created evaluation material for the CodeGuard baseline. They describe a controlled subset of an owner-management feature and are not a claim about every detail of the upstream PetClinic implementation.

Owner search

REQ-OWNER-SEARCH-01: The user may search for an owner using a non-empty last-name value.

REQ-OWNER-SEARCH-02: An exact last-name match shall display the matching owner's identifier, full name, address, city, and telephone number.

REQ-OWNER-SEARCH-03: A partial last-name value with several matches shall display a selectable list of matching owners.

REQ-OWNER-SEARCH-04: When no owner matches, the application shall display a clear no-results message and shall not open an unrelated owner record.

REQ-OWNER-SEARCH-05: A blank search value shall be rejected with a validation message.

Add owner

REQ-OWNER-ADD-01: First name, last name, address, city, and telephone number are required.

REQ-OWNER-ADD-02: The telephone number shall contain between 1 and 10 numeric digits.

REQ-OWNER-ADD-03: A valid submission shall create one owner record and display the new owner details.

REQ-OWNER-ADD-04: An invalid submission shall preserve the entered non-sensitive values and display field-level validation messages.

Update owner

REQ-OWNER-UPDATE-01: A user may update an existing owner's address, city, and telephone number.

REQ-OWNER-UPDATE-02: Updating an owner shall not change the owner's identifier.

REQ-OWNER-UPDATE-03: If the selected owner does not exist, the application shall display a not-found response and shall not create a new owner.
