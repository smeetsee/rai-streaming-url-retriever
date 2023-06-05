from get_video_url import get_channel_m3u8


def produce_m3u(channel=None):
    string = ''
    # Start of an m3u playlist
    string += "#EXTM3U\n"

    # RAI 1
    if channel == 'rai1' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI1HD",Rai Uno\n'
        url_rai1 = get_channel_m3u8('rai1')
        if url_rai1 in [403, 404]:
            return url_rai1
        string += url_rai1 + '\n'

    # RAI 2
    if channel == 'rai2' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI2HD",Rai Due\n'
        url_rai2 = get_channel_m3u8('rai2')
        if url_rai2 in [403, 404]:
            return url_rai2
        string += url_rai2 + '\n'
    
    # RAI 3
    if channel == 'rai3' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI3HD",Rai Tre\n'
        url_rai3 = get_channel_m3u8('rai3')
        if url_rai3 in [403, 404]:
            return url_rai3
        string += url_rai3 + '\n'
    
    # RAI 4
    if channel == 'rai4' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI4HD",Rai Quattro\n'
        url_rai4 = get_channel_m3u8('rai4')
        if url_rai4 in [403, 404]:
            return url_rai4
        string += url_rai4 + '\n'
    
    # RAI 2
    if channel == 'rai5' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI5HD",Rai Cinque\n'
        url_rai5 = get_channel_m3u8('rai5')
        if url_rai5 in [403, 404]:
            return url_rai5
        string += url_rai5 + '\n'

    return string

print(produce_m3u())