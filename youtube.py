import uiautomator2 as u2
import time


def youtube_automation(device_id):

    d = u2.connect(device_id)

    print(f"🚀 Opening YouTube on {device_id}")

    d.app_start("com.google.android.youtube")

    print("⏳ Waiting for YouTube UI...")

    start = time.time()
    ui_found = False

    while time.time() - start < 19:

        print("🔍 Checking UI...")

        if (
            d(resourceId="com.google.android.youtube:id/menu_search").exists
            or d(text="Search").exists
            or d(descriptionContains="Search").exists
        ):
            ui_found = True
            print("✅ YouTube UI Loaded")
            break

        time.sleep(1)

    if not ui_found:
        print("❌ YouTube UI not loaded")
        print("🌐 Internet issue or app loading failed")
        return

    time.sleep(2)

    if d(resourceId="com.google.android.youtube:id/menu_search").exists:
        d(resourceId="com.google.android.youtube:id/menu_search").click()

    elif d(text="Search").exists:
        d(text="Search").click()

    elif d(descriptionContains="Search").exists:
        d(descriptionContains="Search").click()

    else:
        print("❌ Search button not found")
        return

    time.sleep(2)

    if d(className="android.widget.EditText").exists:
        d(className="android.widget.EditText").set_text("MrBeast")
        d.press("enter")

    else:
        print("❌ Search input not found")
        return

    time.sleep(5)

    while True:
        d.swipe(0.5, 0.8, 0.5, 0.3)
        time.sleep(2)
