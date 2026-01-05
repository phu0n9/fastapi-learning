# Practice FastAPI + SQLAlchemy

- Users: need to add modification user, list of users with pagination + limit and add search users, add validation for the input as well, delete (soft and hard)
- Database migration

# AI Chat Support Ticket System — Requirements

## Functional Requirements

### User Management

* The system must allow creating users.
* Each user can have multiple chat sessions.

---

### Chat Management

* A user can start multiple chat sessions.
* Each chat session stores multiple messages.
* Messages belong to exactly one chat.

---

### Message Handling

* A message must contain:

  * User input
  * AI response
* Messages are immutable after creation.

---

### Ticketing / Issue Reporting

* A support ticket can be created for a specific message.
* Each message can have **at most one ticket**.
* A ticket must include:

  * Issue type (e.g. wrong reference, bad prompt, UI error)
  * Status (open, in progress, resolved)
* Ticket status must be updatable.

---

## API Requirements

* The API must expose endpoints to:

  * Create users
  * Create chats
  * Add messages to a chat
  * Create tickets for messages
  * Retrieve tickets (basic listing)
* All endpoints must be exposed under a common `/api` prefix.
* APIs must follow REST conventions.

---

## Data & Persistence Requirements

* The system must persist data using a relational database.
* Relationships must be enforced via foreign keys.
* Enumerations must be used for issue types and ticket statuses.
* Database access must be asynchronous.

---

## Architecture Requirements

* The application must follow a layered architecture:

  * API layer
  * Business logic layer
  * Data access layer
* Database logic must be isolated from API routes.
* Business rules must not be implemented directly in API handlers.

---

## Error Handling Requirements

* The system must handle:

  * Creating tickets for non-existent messages
  * Duplicate ticket creation attempts
* Errors must return meaningful responses.

---

## Performance & Design Considerations

* The system must avoid unnecessary database queries.
* Relationships must be loaded only when needed.
* The design must be maintainable and extensible.

---

## Non-Functional Requirements

* Code must be readable and logically structured.
* Clear naming conventions must be used.
