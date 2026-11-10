---
title: "I decompiled the White House's new app"
url: https://thereallo.dev/blog/decompiling-the-white-house-app
clipped: 2026-06-17 01:26:05
source: "HackerNews Digest"
tags:
  - hn-digest
  - clipping
processed: true
processed_at: 2026-06-23
summary_status: done
concepts:
  - Mobile App Security
  - Reverse Engineering
  - React Native
  - Supply Chain Risk
  - WebViews
  - Telemetry & Analytics
related:
  - "[[We intercepted the White House app's traffic. 77% of requests go to 3rd parties]]"
  - "[[Axios Compromised on NPM – Malicious Versions Drop Remote Access Trojan]]"
  - "[[Zero-day CSS CVE-2026-2441 exists in the wild]]"
---

<!-- ai-summary:start -->
> [!summary]
> **One-line summary:** A decompiler analyzes the new official White House mobile app, revealing hidden JavaScript injection to bypass third-party paywalls and cookie banners, built-in location tracking, and several supply-chain security risks.
>
> **Key points:**
> - The app is built using React Native, Expo SDK 54, and the Hermes engine, communicating with a custom WordPress API backend.
> - It injects custom JavaScript into third-party websites visited via its in-app browser WebView to actively hide cookie consent dialogs, GDPR banners, login walls, and paywalls.
> - The OneSignal SDK is compiled into the app, featuring a full GPS tracking pipeline that polls coordinates at minutes-long intervals and syncs them to external servers.
> - Severe supply-chain vulnerabilities exist, including loading YouTube player HTML from a personal GitHub Pages repository and executing unsandboxed widgets from Elfsight.
> - The production build lacks SSL certificate pinning and contains sloppy development leftovers, such as a developer's local IP address, localhost endpoints, and testing client modules.
>
> **Concept links:** [[Mobile App Security]], [[Reverse Engineering]], [[React Native]], [[Supply Chain Risk]], [[WebViews]], [[Telemetry & Analytics]]
>
> **Suggested connections:**
> - [[We intercepted the White House app's traffic. 77% of requests go to 3rd parties]] — Directly related follow-up or companion article analyzing network traffic for the same application.
> - [[Axios Compromised on NPM – Malicious Versions Drop Remote Access Trojan]] — Relates to JavaScript/NPM supply chain security compromises.
> - [[Zero-day CSS CVE-2026-2441 exists in the wild]] — Related to CSS/web vulnerabilities and injection.
<!-- ai-summary:end -->

# [I decompiled the White House's new app](https://thereallo.dev/blog/decompiling-the-white-house-app)

## Digest Summary
None

## Discussion Summary
Comments show a mix of technical critique and political reaction. Reviewers note that the app’s location‑tracking and remote code loading are typical for many Android apps, with some users questioning privacy and supply‑chain security while others consider the behavior benign or even helpful for bypassing paywalls. Performance complaints about GPU‑intensive scrolling appear alongside remarks that the article may be AI‑generated. Overall, opinions diverge between seeing the app as standard but poorly documented and viewing its data practices as unnecessarily intrusive.

---

## Full Article

The White House released an app on the App Store and Google Play.

[They posted a blog about it.](https://www.whitehouse.gov/releases/2026/03/new-white-house-app-delivers-unparalleled-access-to-the-trump-administration/)

"Unparalleled access to the Trump Administration."

It took a few minutes to pull the APKs with ADB, and threw them into JADX.

Here is everything I found.

What Is This App?
-----------------

It's a React Native app built with Expo (SDK 54), running on the Hermes JavaScript engine. The backend is WordPress with a custom REST API. The app was built by an entity called "forty-five-press" according to the Expo config.

The actual app logic is compiled into a 5.5 MB Hermes bytecode bundle. The native Java side is just a thin wrapper.

```
// sources/gov/whitehouse/app/BuildConfig.java

public final class BuildConfig {
    public static final String APPLICATION_ID = "gov.whitehouse.app";
    public static final String BUILD_TYPE = "release";
    public static final boolean DEBUG = false;
    public static final boolean IS_HERMES_ENABLED = true;
    public static final boolean IS_NEW_ARCHITECTURE_ENABLED = true;
    public static final int VERSION_CODE = 20;
    public static final String VERSION_NAME = "47.0.1";
}
```

Version 47.0.1. Build 20. Hermes enabled. New Architecture enabled. Nothing weird here. Let's keep going.

Expo Config
-----------

```
// resources/assets/app.config

{
  "name": "White House",
  "slug": "white-house",
  "owner": "forty-five-press",
  "version": "47.0.1",
  "scheme": "whitehouse",
  "sdkVersion": "54.0.0",
  "newArchEnabled": true,
  "plugins": [
    ["expo-router", {"sitemap": false}],
    ["onesignal-expo-plugin", {"mode": "production"}],
    "./plugins/withOkHttpFix",
    "./plugins/withResizeableActivity",
    "./plugins/withNoBackgroundAudio",
    "./plugins/withEdgeToEdge",
    "./plugins/withStripPermissions",
    "./plugins/withNoLocation"
  ],
  "updates": {
    "enabled": false,
    "url": "https://u.expo.dev/1590bd5c-74a2-4dd4-8fe6-ff5552ca15b6",
    "checkAutomatically": "NEVER"
  },
  "extra": {
    "eas": {
      "projectId": "1590bd5c-74a2-4dd4-8fe6-ff5552ca15b6"
    }
  }
}
```

Two things stand out here. First, there's a plugin called `withNoLocation`. Second, there's a plugin called `withStripPermissions`. Remember these. They become relevant very soon.

OTA updates are disabled. The Expo update infrastructure is compiled in but dormant.

What the App Actually Does
--------------------------

I extracted every string from the Hermes bytecode bundle and filtered for URLs and API endpoints. The app's content comes from a WordPress REST API at whitehouse.gov with a custom `whitehouse/v1` namespace.

Here are the endpoints:

| Endpoint | What It Serves |
| --- | --- |
| `/wp-json/whitehouse/v1/home` | Home screen |
| `/wp-json/whitehouse/v1/news/articles` | News articles |
| `/wp-json/whitehouse/v1/wire` | "The Wire" news feed |
| `/wp-json/whitehouse/v1/live` | Live streams |
| `/wp-json/whitehouse/v1/galleries` | Photo galleries |
| `/wp-json/whitehouse/v1/issues` | Policy issues |
| `/wp-json/whitehouse/v1/priorities` | Priorities |
| `/wp-json/whitehouse/v1/achievements` | Achievements |
| `/wp-json/whitehouse/v1/affordability` | Drug pricing |
| `/wp-json/whitehouse/v1/media-bias` | "Media Bias" section |
| `/wp-json/whitehouse/v1/social/x` | X/Twitter feed proxy |

Other hardcoded strings from the bundle: `"THE TRUMP EFFECT"`, `"Greatest President Ever!"` (lol), `"Text President Trump"`, `"Send a text message to President Trump at 45470"`, `"Visit TrumpRx.gov"`, `"Visit TrumpAccounts.gov"`.

There's also a direct link to `https://www.ice.gov/webform/ice-tip-form`. The ICE tip reporting form. In a news app.

It's a content portal. News, live streams, galleries, policy pages, social media embeds, and promotional material for administration initiatives. All powered by WordPress.

Now let's look at what else it does.

Consent/Paywall Bypass Injector
-------------------------------

The app has a WebView for opening external links. Every time a page loads in this WebView, the app injects a JavaScript snippet. I found it in the Hermes bytecode string table:

```
(function() {
  var css = document.createElement('style');
  css.textContent = [
    '[class*="cookie"], [id*="cookie"], [class*="Cookie"], [id*="Cookie"]',
    '[class*="consent"], [id*="consent"], [class*="Consent"], [id*="Consent"]',
    '[class*="gdpr"], [id*="gdpr"], [class*="GDPR"]',
    '[class*="privacy-banner"], [id*="privacy-banner"]',
    '[class*="onetrust"], [id*="onetrust"]',
    '[class*="cc-banner"], [class*="cc-window"]',
    '[aria-label*="cookie" i], [aria-label*="consent" i]',
    '[class*="login-wall"], [class*="loginWall"], [class*="LoginWall"]',
    '[class*="signup-wall"], [class*="signupWall"]',
    '[class*="upsell"], [class*="Upsell"]',
    '.cmpboxBtnYes, .cmpbox, #cmpbox, .cmpboxBG',
    '[class*="banner-cookie"], [class*="CookieBanner"]',
  ].join(',') + '{ display: none !important; visibility: hidden !important; }';
  css.textContent += 'body { overflow: auto !important; }';
  document.head.appendChild(css);

  var observer = new MutationObserver(function() {
    var els = document.querySelectorAll(
      '[class*="cookie" i], [class*="consent" i], [class*="gdpr" i], '
      + '[id*="cookie" i], [id*="consent" i]'
    );
    els.forEach(function(el) { el.style.display = 'none'; });
  });
  observer.observe(document.body, { childList: true, subtree: true });
})();
true;
```

Read that carefully. It hides:

* Cookie banners
* GDPR consent dialogs
* OneTrust popups
* Privacy banners
* Login walls
* Signup walls
* Upsell prompts
* Paywall elements
* CMP (Consent Management Platform) boxes

It forces `body { overflow: auto !important }` to re-enable scrolling on pages where consent dialogs lock the scroll. Then it sets up a MutationObserver to continuously nuke any consent elements that get dynamically added.

An official United States government app is injecting CSS and JavaScript into third-party websites to strip away their cookie consent dialogs, GDPR banners, login gates, and paywalls.

The native side confirms this is the `injectedJavaScript` prop on the React Native WebView:

```
// sources/com/reactnativecommunity/webview/RNCWebViewManagerImpl.java

public final void setInjectedJavaScript(
        RNCWebViewWrapper viewWrapper, String injectedJavaScript) {
    viewWrapper.getWebView().injectedJS = injectedJavaScript;
}
```

```
// sources/com/reactnativecommunity/webview/RNCWebView.java

public void callInjectedJavaScript() {
    String str;
    if (!getSettings().getJavaScriptEnabled()
            || (str = this.injectedJS) == null
            || TextUtils.isEmpty(str)) {
        return;
    }
    evaluateJavascriptWithFallback("(function() {\n" + this.injectedJS + ";\n})();");
}
```

Every page load in the in-app browser triggers this. It wraps the injection in an IIFE and runs it via Android's `evaluateJavascript()`.

Location Tracking Infrastructure
--------------------------------

Remember `withNoLocation` from the Expo config? The plugin that's supposed to strip location? Yeah. The OneSignal SDK's native location tracking code is fully compiled into the APK.

```
// sources/com/onesignal/location/internal/common/LocationConstants.java

public final class LocationConstants {
    public static final String ANDROID_BACKGROUND_LOCATION_PERMISSION_STRING =
        "android.permission.ACCESS_BACKGROUND_LOCATION";
    public static final String ANDROID_COARSE_LOCATION_PERMISSION_STRING =
        "android.permission.ACCESS_COARSE_LOCATION";
    public static final String ANDROID_FINE_LOCATION_PERMISSION_STRING =
        "android.permission.ACCESS_FINE_LOCATION";
    public static final long BACKGROUND_UPDATE_TIME_MS = 570000;
    public static final long FOREGROUND_UPDATE_TIME_MS = 270000;
    public static final long TIME_BACKGROUND_SEC = 600;
    public static final long TIME_FOREGROUND_SEC = 300;
}
```

270,000 milliseconds is 4.5 minutes. 570,000 is 9.5 minutes.

To be clear about what activates this: the tracking doesn't start silently. There are three gates. The `LocationManager` checks all of them before the fused location API ever fires.

```
// sources/com/onesignal/location/internal/LocationManager.java

// Gate 1: _isShared must be true (defaults to false in SharedPreferences)
boolean r7 = r6.get_isShared()
if (r7 != 0) goto L42
kotlin.Unit r7 = kotlin.Unit.INSTANCE
return r7  // bail out if location sharing is off
```

First, the `_isShared` flag. It's read from SharedPreferences on init and defaults to `false`. The JavaScript layer can flip it on with `setLocationShared(true)`. The Hermes string table confirms both `setLocationShared` and `isLocationShared` are referenced in the app's JS bundle, so the app has the ability to toggle this.

Second, the user has to grant the Android runtime location permission. The location permissions aren't declared in the AndroidManifest but requested at runtime. The Google Play Store listing confirms the app asks for "access precise location only in the foreground" and "access approximate location only in the foreground."

Third, the `start()` method only proceeds if the device actually has a location provider (GMS or HMS).

If all three gates pass, here's what runs. The fused location API requests GPS at the intervals defined above:

```
// sources/com/onesignal/location/internal/controller/impl/GmsLocationController.java

private final void refreshRequest() {
    if (!this.googleApiClient.isConnected()) {
        return;
    }
    if (this.hasExistingRequest) {
        this._fusedLocationApiWrapper.cancelLocationUpdates(
            this.googleApiClient, this);
    }

    long j = this._applicationService.isInForeground()
        ? LocationConstants.FOREGROUND_UPDATE_TIME_MS   // 270000
        : LocationConstants.BACKGROUND_UPDATE_TIME_MS;  // 570000

    LocationRequest priority = LocationRequest.create()
        .setFastestInterval(j)
        .setInterval(j)
        .setMaxWaitTime((long) (j * 1.5d))
        .setPriority(102);  // PRIORITY_BALANCED_POWER_ACCURACY

    this._fusedLocationApiWrapper.requestLocationUpdates(
        googleApiClient, priority, this);
    this.hasExistingRequest = true;
}
```

This gets called on both `onFocus()` and `onUnfocused()`, dynamically switching between the 4.5-minute foreground interval and the 9.5-minute background interval.

When a location update comes in, it feeds into the `LocationCapturer`:

```
// sources/com/onesignal/location/internal/capture/impl/LocationCapturer.java

private final void capture(Location location) {
    LocationPoint locationPoint = new LocationPoint();
    locationPoint.setAccuracy(Float.valueOf(location.getAccuracy()));
    locationPoint.setBg(Boolean.valueOf(!this._applicationService.isInForeground()));
    locationPoint.setType(getLocationCoarse() ? 0 : 1);
    locationPoint.setTimeStamp(Long.valueOf(location.getTime()));

    if (getLocationCoarse()) {
        locationPoint.setLat(Double.valueOf(
            new BigDecimal(location.getLatitude())
                .setScale(7, RoundingMode.HALF_UP).doubleValue()));
        locationPoint.setLog(Double.valueOf(
            new BigDecimal(location.getLongitude())
                .setScale(7, RoundingMode.HALF_UP).doubleValue()));
    } else {
        locationPoint.setLat(Double.valueOf(location.getLatitude()));
        locationPoint.setLog(Double.valueOf(location.getLongitude()));
    }

    PropertiesModel model = this._propertiesModelStore.getModel();
    model.setLocationLongitude(locationPoint.getLog());
    model.setLocationLatitude(locationPoint.getLat());
    model.setLocationAccuracy(locationPoint.getAccuracy());
    model.setLocationBackground(locationPoint.getBg());
    model.setLocationType(locationPoint.getType());
    model.setLocationTimestamp(locationPoint.getTimeStamp());
}
```

Latitude, longitude, accuracy, timestamp, whether the app was in the foreground or background, and whether it was fine (GPS) or coarse (network). All of it gets written into OneSignal's `PropertiesModel`, which syncs to their backend.

The data goes here:

```
// sources/com/onesignal/core/internal/http/OneSignalService.java

public final class OneSignalService {
    public static final String ONESIGNAL_API_BASE_URL = "https://api.onesignal.com/";
}
```

There's also a background service that keeps capturing location even when the app isn't active:

```
// sources/com/onesignal/location/internal/background/LocationBackgroundService.java

public final class LocationBackgroundService implements IBackgroundService {
    @Override
    public Long getScheduleBackgroundRunIn() {
        if (!this._locationManager.isShared()) {
            return null;
        }
        if (!LocationUtils.INSTANCE.hasLocationPermission(
                this._applicationService.getAppContext())) {
            return null;
        }
        return Long.valueOf(
            MediaSessionService.DEFAULT_FOREGROUND_SERVICE_TIMEOUT_MS
            - (this._time.getCurrentTimeMillis()
               - this._prefs.getLastLocationTime()));
    }

    @Override
    public Object backgroundRun(Continuation<? super Unit> continuation) {
        this._capturer.captureLastLocation();
        return Unit.INSTANCE;
    }
}
```

So the tracking isn't unconditionally active. But the entire pipeline including permission strings, interval constants, fused location requests, capture logic, background scheduling, and the sync to OneSignal's API, all of them are fully compiled in and one `setLocationShared(true)` call away from activating. The `withNoLocation` Expo plugin clearly did not strip any of this. Whether the JS layer currently calls `setLocationShared(true)` is something I can't determine from the native side alone, since the Hermes bytecode is compiled and the actual call site is buried in the 5.5 MB bundle. What I can say is that the infrastructure is there, ready to go, and the JS API to enable it is referenced in the bundle.

OneSignal User Profiling
------------------------

OneSignal is doing a lot more than push notifications in this app. From the Hermes string table:

* `addTag` - tag users for segmentation
* `addSms` - associate phone numbers with user profiles
* `addAliases` - cross-device user identification
* `addOutcomeWithValue` / `addUniqueOutcome` - track user actions and conversions
* `OneSignal-notificationClicked` - notification tap tracking
* `OneSignal-inAppMessageClicked` / `WillDisplay` / `DidDisplay` / `WillDismiss` / `DidDismiss` - full in-app message lifecycle tracking
* `OneSignal-permissionChanged` / `subscriptionChanged` / `userStateChanged` - state change tracking
* `setLocationShared` / `isLocationShared` - location toggle
* `setPrivacyConsentRequired` / `setPrivacyConsentGiven` - consent gating

The local database tracks every notification received and whether it was opened or dismissed:

```
// sources/com/onesignal/core/internal/database/impl/OneSignalDbContract.java

public static final class NotificationTable implements BaseColumns {
    public static final String TABLE_NAME = "notification";
    public static final String COLUMN_NAME_NOTIFICATION_ID = "notification_id";
    public static final String COLUMN_NAME_OPENED = "opened";
    public static final String COLUMN_NAME_DISMISSED = "dismissed";
    public static final String COLUMN_NAME_TITLE = "title";
    public static final String COLUMN_NAME_MESSAGE = "message";
    public static final String COLUMN_NAME_CREATED_TIME = "created_time";
    public static final String COLUMN_NAME_FULL_DATA = "full_data";
}

public static final class InAppMessageTable implements BaseColumns {
    public static final String TABLE_NAME = "in_app_message";
    public static final String COLUMN_NAME_MESSAGE_ID = "message_id";
    public static final String COLUMN_NAME_DISPLAY_QUANTITY = "display_quantity";
    public static final String COLUMN_NAME_LAST_DISPLAY = "last_display";
    public static final String COLUMN_CLICK_IDS = "click_ids";
    public static final String COLUMN_DISPLAYED_IN_SESSION = "displayed_in_session";
}
```

Your location, your notification interactions, your in-app message clicks, your phone number if you provide it, your tags, your state changes. All going to OneSignal's servers.

Supply Chain: Loading JS From Some Guy's GitHub Pages
-----------------------------------------------------

The app embeds YouTube videos using the `react-native-youtube-iframe` library. This library loads its player HTML from:

```
https://lonelycpp.github.io/react-native-youtube-iframe/iframe_v2.html
```

That's a personal GitHub Pages site. If the `lonelycpp` GitHub account gets compromised, whoever controls it can serve arbitrary HTML and JavaScript to every user of this app, executing inside the WebView context.

This is a government app loading code from a random person's GitHub Pages.

Supply Chain: Elfsight Widget Platform
--------------------------------------

The app loads third-party JavaScript from Elfsight to embed social media feeds:

```
https://elfsightcdn.com/platform.js
```

Elfsight is a commercial SaaS widget company. Their JavaScript runs inside the app's WebView with no sandboxing. Whatever tracking Elfsight does, it does it here too. Their code can change at any time. The Elfsight widget ID `4a00611b-befa-466e-bab2-6e824a0a98a9` is hardcoded in an HTML embed.

Supply Chain: Everything Else
-----------------------------

* **Mailchimp** at `whitehouse.us10.list-manage.com/subscribe/post-json` handles email signups. User emails go to Mailchimp's infrastructure.
* **Uploadcare** at `ucarecdn.com` hosts content images via six hardcoded UUIDs.
* **Truth Social** has a hardcoded HTML embed with Trump's profile, avatar image URL from `static-assets-1.truthsocial.com`, and a "Follow on Truth Social" button.
* **Facebook** page plugin is loaded in an iframe via `facebook.com/plugins/page.php`.

None of these are government-controlled infrastructure.

No Certificate Pinning
----------------------

The app uses standard Android TrustManager for SSL with no custom certificate pinning. If you're on a network with a compromised CA (corporate proxies, public wifi with MITM, etc.), traffic between the app and its backends can be intercepted and read.

Development Artifacts in Production
-----------------------------------

The build has some sloppy leftovers.

A localhost URL made it into the production Hermes bundle:

```
http://localhost:8081/wp-json/whitehouse/v1/galleries?page=
```

That's the React Native Metro bundler dev server.

A developer's local IP is hardcoded in the string resources:

```
<!- resources/res/values/strings.xml -->

<string name="react_native_dev_server_ip">10.4.4.109</string>
```

The Expo development client (`expo-dev-client`, `expo-devlauncher`, `expo-devmenu`) is compiled into the release build. There's a `dev_menu_fab_icon.png` in the drawable resources. The Compose `PreviewActivity` is exported in the manifest, which is a development-only component that should not be in a production APK.

```
<activity
    android:name="androidx.compose.ui.tooling.PreviewActivity"
    android:exported="true"/>
```

Permissions
-----------

The AndroidManifest itself is pretty standard for a notification-heavy app:

```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.VIBRATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
<uses-permission android:name="com.google.android.c2dm.permission.RECEIVE"/>
<uses-permission android:name="com.android.vending.CHECK_LICENSE"/>
```

Plus about 16 badge permissions for Samsung, HTC, Sony, Huawei, OPPO, and other launchers. These just let the app show notification badge counts. Not interesting.

The interesting permissions are the ones that aren't in the manifest but are hardcoded as runtime request strings in the OneSignal SDK, as covered above. Fine location. Coarse location. Background location.

The Google Play listing also mentions: "modify or delete the contents of your shared storage", "run foreground service", "this app can appear on top of other apps", "run at startup", "use fingerprint hardware", "use biometric hardware."

The file provider config is also worth mentioning:

```
<!- resources/res/xml/file_provider_paths.xml -->

<paths>
    <external-path name="shared" path="."/>
</paths>
```

That exposes the entire external storage root. It's used by the WebView for file access.

Full SDK List
-------------

68+ libraries are compiled into this thing. The highlights:

| Category | Libraries |
| --- | --- |
| Framework | React Native, Expo SDK 54, Hermes JS engine |
| Push/Engagement | OneSignal, Firebase Cloud Messaging, Firebase Installations |
| Analytics/Telemetry | Firebase Analytics, Google Data Transport, OpenTelemetry |
| Networking | OkHttp 3, Apollo GraphQL, Okio |
| Images | Fresco, Glide, Coil 3, Uploadcare CDN |
| Video | ExoPlayer (Media3), Expo Video |
| ML | Google ML Kit Vision (barcode scanning), Barhopper model |
| Crypto | Bouncy Castle |
| Storage | Expo Secure Store, React Native Async Storage |
| WebView | React Native WebView (with the injection script) |
| DI | Koin |
| Serialization | GSON, Wire (Protocol Buffers) |
| License | PairIP license check (Google Play verification) |

25 native `.so` libraries in the arm64 split. The full Hermes engine, React Native core, Reanimated, gesture handler, SVG renderer, image pipeline, barcode scanner, and more.

Recap
-----

The official White House Android app:

1. **Injects JavaScript into every website you open** through its in-app browser to hide cookie consent dialogs, GDPR banners, login walls, signup walls, upsell prompts, and paywalls.
2. **Has a full GPS tracking pipeline compiled in** that polls every 4.5 minutes in the foreground and 9.5 minutes in the background, syncing lat/lng/accuracy/timestamp to OneSignal's servers.
3. **Loads JavaScript from a random person's GitHub Pages site** (`lonelycpp.github.io`) for YouTube embeds. If that account is compromised, arbitrary code runs in the app's WebView.
4. **Loads third-party JavaScript from Elfsight** (`elfsightcdn.com/platform.js`) for social media widgets, with no sandboxing.
5. **Sends email addresses to Mailchimp**, images are served from Uploadcare, and a Truth Social embed is hardcoded with static CDN URLs. None of this is government infrastructure.
6. **Has no certificate pinning.** Standard Android trust management.
7. **Ships with dev artifacts in production.** A localhost URL, a developer IP (`10.4.4.109`), the Expo dev client, and an exported Compose PreviewActivity.
8. **Profiles users extensively through OneSignal** - tags, SMS numbers, cross-device aliases, outcome tracking, notification interaction logging, in-app message click tracking, and full user state observation.

Is any of this illegal? Probably not. Is it what you'd expect from an official government app? Probably not either.