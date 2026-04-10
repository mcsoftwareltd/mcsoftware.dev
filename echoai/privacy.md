---
layout: legal
permalink: /echoai/privacy/
title: Privacy Policy
project: EchoAI
project_url: /echoai/
kind: Privacy
effective_date: 11 April 2026
description: EchoAI privacy policy. Nothing leaves your device.
---

## Summary

EchoAI is an on-device app. It does not collect, transmit, or store any information on MC Software servers — because MC Software does not operate any servers for EchoAI. This document describes, in detail, exactly what that means.

## 1. Who we are

"We," "us," and "MC Software" refer to **MC Software ltd**, a company registered in England and Wales under company number **16230837**. You can reach us at [matteo@mcsoftware.dev](mailto:matteo@mcsoftware.dev).

## 2. What we collect

**Nothing.** EchoAI has no backend, no account system, no analytics, and no telemetry. We do not know who you are, when you use the app, how often you use it, or what you record.

## 3. What the app stores on your device

Everything that EchoAI works with is stored locally on your iPhone in the app's sandboxed storage:

- **Audio recordings** of the sessions you choose to record.
- **Transcripts** generated from those recordings.
- **Summaries, titles, and action items** generated from those transcripts.
- **Session metadata** such as timestamps and labels you add.

These files live on your device for as long as you keep them. Delete a session inside the app and the underlying files are removed. Uninstall EchoAI and everything goes with it.

If you have iCloud device backup enabled in iOS Settings, the app's data may be included in that backup according to your iOS settings. That backup is managed by Apple, not by us.

## 4. Third-party services

**None.** EchoAI does not integrate any third-party analytics, advertising, crash-reporting, or tracking service. There are no SDKs that phone home.

Transcription, summarization, and speaker separation are performed entirely on your device using Apple's built-in frameworks and embedded open-source libraries:

- **Apple Speech framework** — real-time transcription.
- **WhisperKit** — alternative transcription engine running locally on the Neural Engine.
- **Apple Foundation Models (Apple Intelligence)** — on-device language model used for summaries and action items.
- **SpeakerKit** — on-device speaker diarization.

None of these components send your audio or transcripts to remote servers when used by EchoAI.

## 5. Permissions the app asks for

EchoAI requests two iOS permissions, both strictly needed for the app to function:

- **Microphone** — required to record audio.
- **Speech Recognition** — required for on-device transcription via Apple's Speech framework.

You can grant or revoke these at any time in **Settings → Privacy &amp; Security** on your iPhone. If you revoke them, the relevant features will stop working, but the app will continue to open and let you review past sessions.

## 6. How we use what you record

We don't. We never see it. EchoAI processes your audio and transcripts locally to provide the features of the app, and for no other purpose.

## 7. Sharing

Because we do not receive your data, we do not share it with anyone. If you choose to export a transcript or summary out of the app (for example, by copying it or saving it to the Files app), you are in control of where it goes next.

## 8. Children's privacy

EchoAI is not directed at children under the age of 13. We do not knowingly process data from children — because we do not knowingly process data from anyone.

## 9. Your rights

Under data protection laws including the UK GDPR and the EU GDPR, you have rights to access, correct, delete, and port your personal data. Because MC Software does not hold any personal data about you in connection with EchoAI, there is nothing for us to provide, correct, or delete on our side. Data stored by the app on your device is fully under your control and can be deleted by you at any time.

## 10. Changes to this policy

If this policy changes, we will update the effective date at the top of this page and publish the new version at [https://mcsoftware.dev/echoai/privacy](https://mcsoftware.dev/echoai/privacy). Material changes will be communicated through an in-app notice.

## 11. Contact

Questions, concerns, or complaints about this policy: [matteo@mcsoftware.dev](mailto:matteo@mcsoftware.dev).

---

*This policy was last updated on 11 April 2026.*
