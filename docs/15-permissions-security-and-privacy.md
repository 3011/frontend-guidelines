# Permissions, Security, and Privacy

## UI capability vs authorization

The interface should show actions appropriate to the current role, resource state, and capability. This improves clarity, but client behavior is not a security boundary.

Every protected read and mutation must be enforced by an authoritative server or trusted policy layer. Hidden buttons, disabled controls, route guards, and client-side role checks are not sufficient enforcement.

## Permission states

Design distinct behavior for:

- no permission to discover a resource;
- permission to view but not edit;
- permission to edit only part of a resource;
- temporary lock or approval state;
- expired or changed permission;
- action rejected after the UI was loaded.

Do not expose an editable-looking form when the current user can only view it. Do not show a generic “not found” when policy requires an explicit permission explanation, or disclose existence when policy requires concealment.

## Sensitive information

Minimize exposure of:

- access tokens and secrets;
- private identifiers;
- personal data;
- internal topology and diagnostics;
- hidden fields;
- credentials in generated commands;
- sensitive values in URLs, analytics, browser history, logs, clipboard, or screenshots.

Masking is not equivalent to access control. Provide reveal and copy actions only when the user needs them and the environment is appropriate.

## Clipboard and downloads

Copying or downloading sensitive material should identify what will be copied, its sensitivity, and any expiry. Avoid silent clipboard writes.

Downloads should use safe names, correct content type, and an explicit scope. Do not include more data than the user selected or is authorized to access.

## Untrusted content

Treat user-generated and remote content as untrusted. Do not interpret it as executable markup, script, style, URL, command, or file path without an explicit trust and sanitization model.

When rendering logs, markdown, HTML, filenames, links, or rich text, preserve content without granting it code execution or privileged navigation.

## External destinations

External links and redirects should make the destination understandable, particularly when leaving a trusted domain, sharing context, or including sensitive query data.

Do not place secrets in external URLs. Use confirmation when an external effect is high-impact or difficult to reverse.

## Error privacy

User-facing errors should not reveal stack traces, database details, provider credentials, internal addresses, or whether a protected resource exists beyond policy.

Diagnostic references may be shown when they are safe and useful for support.

## Analytics

Do not send field values, free-form user text, secrets, or sensitive identifiers to analytics by default. Event design should capture product behavior with the minimum necessary data.
