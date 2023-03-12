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
    
    # RAI 5
    if channel == 'rai5' or channel is None:
        string += '#EXTINF:-1 tvg-id="RAI5HD",Rai Cinque\n'
        url_rai5 = get_channel_m3u8('rai5')
        if url_rai5 in [403, 404]:
            return url_rai5
        string += url_rai5 + '\n'
    
    # RAI Gulp
    if channel == 'raigulp' or channel is None:
        string += '#EXTINF:-1,Rai Gulp\n'
        url_raigulp = get_channel_m3u8('raigulp')
        if url_raigulp in [403, 404]:
            return url_raigulp
        string += url_raigulp + '\n'

    # RAI Movie
    if channel == 'raimovie' or channel is None:
        string += '#EXTINF:-1,Rai Movie\n'
        url_raimovie = get_channel_m3u8('raimovie')
        if url_raimovie in [403, 404]:
            return url_raimovie
        string += url_raimovie + '\n'
    
    # RAI News24
    if channel == 'rainews24' or channel is None:
        string += '#EXTINF:-1,Rai News24\n'
        url_rainews24 = get_channel_m3u8('rainews24')
        if url_rainews24 in [403, 404]:
            return url_rainews24
        string += url_rainews24 + '\n'
    
    # RAI Premium
    if channel == 'raipremium' or channel is None:
        string += '#EXTINF:-1,Rai Premium\n'
        url_raipremium = get_channel_m3u8('raipremium')
        if url_raipremium in [403, 404]:
            return url_raipremium
        string += url_raipremium + '\n'

    # RAI Scuola
    if channel == 'raiscuola' or channel is None:
        string += '#EXTINF:-1,Rai Scuola\n'
        url_raiscuola = get_channel_m3u8('raiscuola')
        if url_raiscuola in [403, 404]:
            return url_raiscuola
        string += url_raiscuola + '\n'
    
    # RAI Sport
    if channel == 'raisport' or channel is None:
        string += '#EXTINF:-1,Rai Sport\n'
        url_raisport = get_channel_m3u8('raisport')
        if url_raisport in [403, 404]:
            return url_raisport
        string += url_raisport + '\n'
    
    # RAI Storia
    if channel == 'raistoria' or channel is None:
        string += '#EXTINF:-1,Rai Storia\n'
        url_raistoria = get_channel_m3u8('raistoria')
        if url_raistoria in [403, 404]:
            return url_raistoria
        string += url_raistoria + '\n'
    
    # RAI Yoyo
    if channel == 'raiyoyo' or channel is None:
        string += '#EXTINF:-1,Rai Yoyo\n'
        url_raiyoyo = get_channel_m3u8('raiyoyo')
        if url_raiyoyo in [403, 404]:
            return url_raiyoyo
        string += url_raiyoyo + '\n'

    return string

print(produce_m3u())