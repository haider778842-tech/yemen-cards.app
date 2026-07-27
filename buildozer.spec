[app]
title = شبكة عيسى
package.name = yemencards
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1
requirements = python3,kivy,flask,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_SMS,RECEIVE_SMS
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
