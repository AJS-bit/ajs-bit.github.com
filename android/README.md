# 안드로이드 APK

웹 앱을 웹뷰에 담는 껍데기다. **웹 코드는 여기에 없다** — 저장소 루트의
`index.html` · `css/` · `js/` · `sw.js` 하나가 원본이고, 빌드할 때
`syncWebAssets` 태스크가 그것을 APK 의 assets 로 가져온다. 여기에 사본을 두면
사본이 둘이 되어 반드시 어긋나기 때문이다.

## 빌드

Android SDK 만 있으면 된다 (JDK 는 SDK 에 따라온 것을 쓰거나 17 이상).

```bash
export ANDROID_HOME=~/Android/Sdk      # 각자의 SDK 경로
cd android
./gradlew assembleDebug                # → app/build/outputs/apk/debug/app-debug.apk
```

SDK 가 없으면 [Android Studio](https://developer.android.com/studio) 를 설치하거나
커맨드라인 도구만 받아 다음을 설치한다.

```bash
sdkmanager "platform-tools" "platforms;android-35" "build-tools;35.0.0"
```

`ANDROID_HOME` 대신 `android/local.properties` 에
`sdk.dir=/경로/Android/Sdk` 를 적어도 된다 (이 파일은 커밋하지 않는다).

## 설치

`app-debug.apk` 를 폰으로 옮겨 누르면 된다. 스토어를 거치지 않으므로 처음 한 번
"이 출처의 앱 설치" 를 허용해야 한다. 개발용 서명이라 스토어 배포는 불가하고,
배포하려면 `app/build.gradle` 의 `signingConfig` 를 자기 키로 바꿔야 한다.

## 설계에서 지킬 것

### 왜 `file://` 이 아니라 `https://appassets.androidplatform.net`

앱의 `js/` 는 전부 ES 모듈이다. `file://` 로 열면 오리진이 불투명해져 모듈이
CORS 에 막히고 **아무것도 뜨지 않는다.** `WebViewAssetLoader` 로 assets 를
https 오리진에 얹으면 모듈도 `localStorage` 도 서비스워커도 웹과 똑같이 돈다.

서비스워커가 가로챈 요청도 같은 로더를 타야 한다(`ServiceWorkerClientCompat`).
안 걸어두면 `sw.js` 가 등록된 **두 번째 실행부터** 화면이 빈다.

### `onRenderProcessGone` 을 지울 것

안드로이드 O 부터 웹뷰 렌더러는 별도 프로세스다. 그 프로세스가 죽었을 때
이 콜백에서 `true` 를 돌려주지 않으면 **앱 프로세스까지 함께 죽는다.**
에뮬레이터에서 실제로 그랬다 —
`Render process's crash wasn't handled by all associated webviews,
triggering application crash.` 메모리 부족 시 실제 기기에서도 일어난다.

### 인터넷 권한을 넣지 말 것

매니페스트에 `INTERNET` 권한이 없다. "데이터가 네트워크로 나가지 않는다" 는
이 앱의 약속을 매니페스트 수준에서 못박은 것이고, 설치할 때 권한 목록이 비어
있는 것이 사용자에게 보이는 증거다.

### 웹 코드의 하한은 Chrome 80

WebView 는 Play 스토어로 따로 업데이트되므로 안드로이드 버전과 무관하게
낡을 수 있다. 하한을 넘는 문법이 한 줄이라도 섞이면 그 화면이 통째로 죽는다.
`test/legacy.mjs` 가 이것을 검사한다. 실제로 밟은 것:

| 문법 | 필요 버전 | 증상 |
|---|---|---|
| `?.` `??` | Chrome 80 | 앱 전체가 빈 화면 (WebView 66) |
| `\|\|=` | Chrome 85 | 지출·내역이 죽음 (WebView 83) |
| `.at(-1)` | Chrome 92 | 목표·미래 예측이 죽음 |

## 확인한 환경

| 이미지 | WebView | 결과 |
|---|---|---|
| Android 11 (API 30) | 83 | 정상 — 콘솔 에러 0건, 전 화면 동작 |
| Android 14 (API 34) | 113 | 앱은 정상. KVM 없는 에뮬레이터에서는 시스템이 ANR 이라 화면 확인 불가 |
| Android 9 (API 28) | 66 | 하한 미달 — 업데이트 안내가 뜬다 (의도된 동작) |
