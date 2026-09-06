package com.ajsbit.assetcompass;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Build;
import android.os.Bundle;
import android.view.ViewGroup;
import android.webkit.RenderProcessGoneDetail;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

import androidx.activity.OnBackPressedCallback;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.webkit.ServiceWorkerClientCompat;
import androidx.webkit.ServiceWorkerControllerCompat;
import androidx.webkit.WebViewAssetLoader;
import androidx.webkit.WebViewFeature;

/**
 * 자산 나침반을 웹뷰에 담는 껍데기.
 *
 * 정적 파일을 file:// 로 열면 ES 모듈이 CORS 에 막혀 동작하지 않는다(앱의 js/ 는 전부
 * ES 모듈이다). WebViewAssetLoader 로 assets/ 를 https://appassets.androidplatform.net/
 * 오리진에 얹으면 모듈도, localStorage 도, 서비스워커도 웹에서와 똑같이 돈다.
 *
 * 인터넷 권한을 선언하지 않았다. 네트워크로 나가는 코드가 앱에 없다는 약속을
 * 매니페스트 수준에서 못박는 것이다.
 */
public class MainActivity extends AppCompatActivity {

  private static final String ORIGIN = "https://appassets.androidplatform.net";
  private static final String START = ORIGIN + "/index.html";

  private FrameLayout root;
  private WebView web;
  private WebViewAssetLoader loader;

  @Override
  protected void onCreate(Bundle saved) {
    super.onCreate(saved);

    loader = new WebViewAssetLoader.Builder()
        .addPathHandler("/", new WebViewAssetLoader.AssetsPathHandler(this))
        .build();

    root = new FrameLayout(this);
    root.setBackgroundColor(Color.parseColor("#0b0f19"));   // 첫 프레임 흰 번쩍임 방지
    setContentView(root);

    // 서비스워커가 가로챈 요청도 같은 로더를 타야 한다. 안 걸어두면 sw.js 가
    // 등록된 뒤 두 번째 실행부터 화면이 비어버린다.
    if (WebViewFeature.isFeatureSupported(WebViewFeature.SERVICE_WORKER_BASIC_USAGE)) {
      ServiceWorkerControllerCompat.getInstance().setServiceWorkerClient(
          new ServiceWorkerClientCompat() {
            @Override
            public WebResourceResponse shouldInterceptRequest(WebResourceRequest req) {
              return loader.shouldInterceptRequest(req.getUrl());
            }
          });
    }

    attachWebView(saved);

    getOnBackPressedDispatcher().addCallback(this, new OnBackPressedCallback(true) {
      @Override
      public void handleOnBackPressed() {
        if (web != null && web.canGoBack()) web.goBack();
        else finish();
      }
    });
  }

  /** 웹뷰를 새로 만들어 붙인다. 렌더러가 죽었을 때 다시 부르기 위해 분리해 뒀다. */
  @SuppressLint("SetJavaScriptEnabled")
  private void attachWebView(Bundle saved) {
    web = new WebView(this);
    web.setBackgroundColor(Color.parseColor("#0b0f19"));
    root.addView(web, new FrameLayout.LayoutParams(
        ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));

    WebSettings s = web.getSettings();
    s.setJavaScriptEnabled(true);
    s.setDomStorageEnabled(true);            // localStorage — 이 앱의 유일한 저장소
    s.setAllowFileAccess(false);
    s.setAllowContentAccess(false);
    s.setMediaPlaybackRequiresUserGesture(true);

    web.setWebViewClient(new WebViewClient() {
      @Override
      public WebResourceResponse shouldInterceptRequest(WebView v, WebResourceRequest req) {
        return loader.shouldInterceptRequest(req.getUrl());
      }

      /*
       * 안드로이드 O 부터 웹뷰 렌더러는 별도 프로세스다. 그 프로세스가 죽었을 때
       * 이 콜백에서 true 를 돌려주지 않으면 **앱 프로세스까지 함께 죽는다.**
       * 에뮬레이터에서 실제로 그랬다 —
       *   FATAL: Render process's crash wasn't handled by all associated webviews,
       *          triggering application crash.
       * 데이터는 localStorage 에 있으므로 웹뷰만 새로 만들어 다시 그리면 복구된다.
       */
      @RequiresApi(Build.VERSION_CODES.O)
      @Override
      public boolean onRenderProcessGone(WebView v, RenderProcessGoneDetail detail) {
        if (v != web) return true;
        root.removeView(web);
        web.destroy();
        web = null;
        attachWebView(null);
        return true;                          // 앱은 계속 산다
      }
    });

    if (saved != null) web.restoreState(saved);
    else web.loadUrl(START);
  }

  @Override
  protected void onSaveInstanceState(Bundle out) {
    super.onSaveInstanceState(out);
    if (web != null) web.saveState(out);
  }
}
