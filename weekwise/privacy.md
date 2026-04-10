---
layout: legal
permalink: /weekwise/privacy/
title: Privacy Policy
project: Weekwise
project_url: /weekwise/
kind: Privacy
effective_date: 11 April 2026
description: Weekwise privacy policy. What the app touches, and why.
---

## Summary

Weekwise is mostly an on-device app. Your calendar data never leaves your iPhone by way of anything we operate. A small number of third-party services are used for crash reporting, in-app purchases, and weather — described in detail below. This policy explains exactly what happens with your data and who sees it.

## 1. Who we are

"We," "us," and "MC Software" refer to **MC Software ltd**, a company registered in England and Wales under company number **16230837**. Contact: [matteo@mcsoftware.dev](mailto:matteo@mcsoftware.dev).

## 2. What Weekwise stores on your device

Weekwise reads from and writes to your iOS Calendar using Apple's EventKit framework. The app itself stores, locally on your device:

- **App metadata** linked to your calendar events: completion status, todo state, notes you've added, and prep-chain suggestions. This is kept in a local SwiftData store inside the app sandbox.
- **Preferences** such as which calendars to sync, notification defaults, and appearance settings.
- **Location** (optional) — if you grant permission, your current location is used to fetch a weather forecast.

Calendar events themselves remain where they already live — in Apple's Calendar database — and are not duplicated by us.

## 3. Third-party services Weekwise uses

Weekwise relies on a small number of third-party services. Each is described below with the data involved.

### a) Apple WeatherKit

Weekwise uses **WeatherKit**, Apple's weather service, to show forecasts next to your days. To return a forecast, WeatherKit needs a location — either your current location (if you have granted Location permission) or a location you pick manually.

WeatherKit is operated by Apple. Apple's own privacy practices apply, and Apple has stated that WeatherKit location requests are not associated with your Apple ID or used for advertising. See Apple's [Weather privacy page](https://www.apple.com/legal/privacy/data/en/weather/) for details.

### b) RevenueCat (in-app purchases)

Weekwise uses **RevenueCat** to manage in-app purchases and subscriptions. When you purchase or restore a subscription, RevenueCat receives:

- An anonymized, randomly generated app user ID (not your Apple ID, email address, or name).
- The App Store transaction receipt.
- Basic product and country metadata.

RevenueCat uses this to validate the purchase with Apple, determine your entitlements, and make them available to the app. RevenueCat is operated by RevenueCat, Inc. See the [RevenueCat privacy policy](https://www.revenuecat.com/privacy/).

### c) Firebase Crashlytics (crash reporting)

Weekwise uses **Google Firebase Crashlytics** to receive anonymized crash reports so we can fix the bugs that cause the app to crash. When the app crashes, Crashlytics collects:

- A stack trace of the crash.
- The device model and operating system version.
- A randomly generated installation identifier that is not linked to your Apple ID or any personal information.
- Non-personal breadcrumb logs describing what the app was doing before the crash.

Crashlytics does not receive your calendar events, todos, notes, location, or any personal information you have entered into the app. Crashlytics is operated by Google LLC. See the [Firebase privacy and security page](https://firebase.google.com/support/privacy).

## 4. Permissions Weekwise asks for

- **Calendar (EventKit)** — required, so the app can show and modify your events. You can revoke this at any time in **Settings → Privacy &amp; Security → Calendars**. Without it, the app cannot function.
- **Notifications** — optional, used for event reminders you choose to enable.
- **Location (While Using)** — optional, only used to fetch weather via WeatherKit. You can pick a location manually instead.

## 5. What we do *not* do

- We do not operate a server that receives your calendar events, todos, or notes.
- We do not sell, rent, or share your data with advertisers.
- We do not run marketing analytics or A/B testing SDKs inside the app.
- We do not profile you or build an advertising identifier.

## 6. Data retention

Data stored locally by Weekwise stays on your device for as long as you keep the app installed. Delete the app and everything goes with it. Third-party services retain data according to their own policies, linked above.

## 7. Children's privacy

Weekwise is not directed at children under the age of 13.

## 8. Your rights

Under the UK GDPR and the EU GDPR, you have rights to access, correct, delete, port, and object to processing of your personal data. Because Weekwise does not send your calendar content to us, there is typically no personal data held by MC Software for us to act on. For requests concerning data held by RevenueCat, Firebase, or Apple, please see their respective privacy policies, or contact us and we will help direct the request.

## 9. International transfers

Crashlytics and RevenueCat are operated by companies based in the United States. By using Weekwise, you understand that anonymized crash and purchase data described above may be transferred to and processed in the United States under the operators' own safeguards.

## 10. Changes to this policy

If this policy changes, we will update the effective date at the top of this page and publish the new version at [https://mcsoftware.dev/weekwise/privacy](https://mcsoftware.dev/weekwise/privacy). Material changes will be communicated through an in-app notice.

## 11. Contact

Questions, concerns, or complaints: [matteo@mcsoftware.dev](mailto:matteo@mcsoftware.dev).

---

*This policy was last updated on 11 April 2026.*
