import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch001.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1446533711&myTokenPrefixhash=z6SHzub2W3cgvlcIwlVjqMTwHehvs2r32W4Fy-1reNQ='
li = xbmcgui.ListItem(label='TV1')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tv1.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch002.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1446533760&myTokenPrefixhash=wgYrvruNp_zHjt00aDE8ceBsVn5U-w1ZDH6LicVVG60='
li = xbmcgui.ListItem('TV2')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tv2.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://tv3liveios-i.akamaihd.net/hls/live/205900/ios/tv3live/master.m3u8'
li = xbmcgui.ListItem('TV3')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tv3.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://ntv7liveios-i.akamaihd.net/hls/live/205902/ios/ntv7live/master.m3u8'
li = xbmcgui.ListItem('NTV7')
li.setIconImage('http://myiptv.site40.net/kodi/logo/ntv7.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://8tvliveios-i.akamaihd.net/hls/live/205901/ios/8tvlive/master.m3u8'
li = xbmcgui.ListItem('8TV')
li.setIconImage('http://myiptv.site40.net/kodi/logo/8tv.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://tv9liveios-i.akamaihd.net/hls/live/205903/ios/tv9live/master.m3u8'
li = xbmcgui.ListItem('TV9')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tv9.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://d2f9tqsihrp4sc.cloudfront.net/livecf/smil:myStream.smil/playlist.m3u8'
li = xbmcgui.ListItem('AL-Hijrah')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tv_alhijrah.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://goo.gl/FSrrbv'
li = xbmcgui.ListItem('Ria')
li.setIconImage('http://myiptv.site40.net/kodi/logo/mobtv.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch003.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1446533784&myTokenPrefixhash=g4CTLDk3QkYOnOylqr2CMRfcnHl1AvulVdIQjkN2_Qk='
li = xbmcgui.ListItem('TVi')
li.setIconImage('http://myiptv.site40.net/kodi/logo/tvi.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch004.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1446533804&myTokenPrefixhash=zFPl98VJK4VQFbkbJp3HoxYBv88hj0Xq06yByVrHLgI='
li = xbmcgui.ListItem('Aktif Muzik')
li.setIconImage('http://myiptv.site40.net/kodi/logo/muzik.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://awaniioslive-i.akamaihd.net/hls/live/207096-b/awaniIOSLiveStream@207096/awani_stream.m3u8'
li = xbmcgui.ListItem('AWANI')
li.setIconImage('http://myiptv.site40.net/kodi/logo/astro_awani.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://d22b8vh21p20bg.cloudfront.net/mylive/smil:bernama2_all.smil/playlist.m3u8'
li = xbmcgui.ListItem('BERNAMA TV')
li.setIconImage('http://myiptv.site40.net/kodi/logo/bernama.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = ''
li = xbmcgui.ListItem('1NEWS')
li.setIconImage('http://myiptv.site40.net/kodi/logo/1news.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)