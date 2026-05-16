import uiautomator2 as u2
import time


def youtube_automation(device_id):

    d = u2.connect(device_id)

    print(f"🚀 Opening YouTube on {device_id}")

    d.app_start("com.google.android.youtube")

    time.sleep(5)


    if d(resourceId="com.google.android.youtube:id/menu_search").exists:

        d(resourceId="com.google.android.youtube:id/menu_search").click()

    # LEVEL 2 → text
    elif d(text="Search").exists:

        d(text="Search").click()

    # LEVEL 3 → description
    elif d(descriptionContains="Search").exists:

        d(descriptionContains="Search").click()

    else:

        print("❌ Search button not found")
        return

    time.sleep(2)

    # Search input
    if d(className="android.widget.EditText").exists:

        d(className="android.widget.EditText").set_text("MrBeast")

        d.press("enter")

    else:

        print("❌ Search input not found")
        return

    time.sleep(5)

    # Scroll loop
    while True:

        d.swipe(0.5, 0.8, 0.5, 0.3)

        time.sleep(2)
